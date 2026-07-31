import { test, expect } from "@playwright/test";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const LOMBOK_JS = path.resolve(__dirname, "../dist/lombok.js");

/**
 * Render markup FIRST, then inject dist/lombok.js — the order a real page uses.
 *
 * Order matters and is itself part of the contract: tabs, carousels, sortable
 * tables and dialog backdrops are wired once at parse time via querySelectorAll,
 * so markup injected after the script is inert. Dropdown, modal open/close,
 * drawer, popover and navbar use delegated listeners on `document` and do work
 * for markup added later.
 *
 * These tests deliberately load NO CSS. They assert behaviour (classes, ARIA,
 * DOM order, scroll offsets), never appearance — visual.spec.js owns appearance.
 * The only exception is the carousel, which needs a scroll container; it gets
 * its own inline stylesheet with fixed numbers so the step maths is exact.
 */
async function mount(page, body, { dir = "ltr", head = "" } = {}) {
  await page.setContent(
    `<!doctype html><html><head><meta charset="utf-8">${head}</head><body>${body}</body></html>`,
  );
  if (dir !== "ltr") {
    await page.evaluate((value) => document.documentElement.setAttribute("dir", value), dir);
  }
  await page.addScriptTag({ path: LOMBOK_JS });
}

// Every test doubles as a smoke test for uncaught exceptions.
const thrown = new WeakMap();
test.beforeEach(({ page }) => {
  const errors = [];
  thrown.set(page, errors);
  page.on("pageerror", (e) => errors.push(e.message));
});
test.afterEach(({ page }) => {
  expect(thrown.get(page) ?? []).toEqual([]);
});

/* ------------------------------------------------------------------ dropdown */

const DROPDOWN = `
  <div class="dropdown" id="dd-a">
    <button data-dropdown-toggle aria-expanded="false" id="dd-a-btn">Menu A</button>
    <div class="dropdown-menu"><a href="#" id="dd-a-item">Item A</a></div>
  </div>
  <div class="dropdown" id="dd-b">
    <button data-dropdown-toggle aria-expanded="false" id="dd-b-btn">Menu B</button>
    <div class="dropdown-menu"><a href="#" id="dd-b-item">Item B</a></div>
  </div>
  <p id="outside">outside</p>`;

test.describe("dropdown", () => {
  test("toggle opens and closes, keeping aria-expanded in sync", async ({ page }) => {
    await mount(page, DROPDOWN);
    const dd = page.locator("#dd-a");
    const btn = page.locator("#dd-a-btn");

    await btn.click();
    await expect(dd).toHaveClass(/is-open/);
    await expect(btn).toHaveAttribute("aria-expanded", "true");

    await btn.click();
    await expect(dd).not.toHaveClass(/is-open/);
    await expect(btn).toHaveAttribute("aria-expanded", "false");
  });

  test("clicking outside closes it and resets aria-expanded", async ({ page }) => {
    await mount(page, DROPDOWN);
    await page.locator("#dd-a-btn").click();
    await page.locator("#outside").click();
    await expect(page.locator("#dd-a")).not.toHaveClass(/is-open/);
    await expect(page.locator("#dd-a-btn")).toHaveAttribute("aria-expanded", "false");
  });

  test("Escape closes it and resets aria-expanded", async ({ page }) => {
    await mount(page, DROPDOWN);
    await page.locator("#dd-a-btn").click();
    await page.keyboard.press("Escape");
    await expect(page.locator("#dd-a")).not.toHaveClass(/is-open/);
    await expect(page.locator("#dd-a-btn")).toHaveAttribute("aria-expanded", "false");
  });

  // Pinned, not aspirational: any click that is not on a toggle closes the open
  // dropdown, including clicks on its own items. That is what a menu wants, but
  // it also means a dropdown cannot host interactive content (an input inside
  // one would close the menu on focus-click). Changing that is an API decision.
  test("clicking a menu item closes the dropdown", async ({ page }) => {
    await mount(page, DROPDOWN);
    await page.locator("#dd-a-btn").click();
    await page.locator("#dd-a-item").click();
    await expect(page.locator("#dd-a")).not.toHaveClass(/is-open/);
    await expect(page.locator("#dd-a-btn")).toHaveAttribute("aria-expanded", "false");
  });

  test("opening a second dropdown closes the first", async ({ page }) => {
    await mount(page, DROPDOWN);
    await page.locator("#dd-a-btn").click();
    await page.locator("#dd-b-btn").click();
    await expect(page.locator("#dd-a")).not.toHaveClass(/is-open/);
    await expect(page.locator("#dd-a-btn")).toHaveAttribute("aria-expanded", "false");
    await expect(page.locator("#dd-b")).toHaveClass(/is-open/);
    await expect(page.locator("#dd-b-btn")).toHaveAttribute("aria-expanded", "true");
  });

  test("works for markup injected after the script (delegated listener)", async ({ page }) => {
    await mount(page, `<div id="host"></div>`);
    await page.evaluate(() => {
      document.getElementById("host").innerHTML =
        '<div class="dropdown" id="late"><button data-dropdown-toggle aria-expanded="false" id="late-btn">L</button></div>';
    });
    await page.locator("#late-btn").click();
    await expect(page.locator("#late")).toHaveClass(/is-open/);
  });
});

/* ---------------------------------------------------------------------- tabs */

const TABS = `
  <div role="tablist" id="list-1">
    <button role="tab" aria-selected="true" aria-controls="p1" id="t1">One</button>
    <button role="tab" aria-selected="false" aria-controls="p2" id="t2">Two</button>
  </div>
  <div id="p1">Panel one</div>
  <div id="p2" hidden>Panel two</div>

  <div role="tablist" id="list-2">
    <button role="tab" aria-selected="true" aria-controls="q1" id="u1">A</button>
    <button role="tab" aria-selected="false" aria-controls="q2" id="u2">B</button>
  </div>
  <div id="q1">Panel A</div>
  <div id="q2" hidden>Panel B</div>`;

test.describe("tabs", () => {
  test("selecting a tab swaps aria-selected and panel visibility", async ({ page }) => {
    await mount(page, TABS);
    await page.locator("#t2").click();

    await expect(page.locator("#t1")).toHaveAttribute("aria-selected", "false");
    await expect(page.locator("#t2")).toHaveAttribute("aria-selected", "true");
    await expect(page.locator("#p1")).toBeHidden();
    await expect(page.locator("#p2")).toBeVisible();
  });

  test("re-clicking the active tab is idempotent", async ({ page }) => {
    await mount(page, TABS);
    await page.locator("#t2").click();
    await page.locator("#t2").click();
    await expect(page.locator("#t2")).toHaveAttribute("aria-selected", "true");
    await expect(page.locator("#p2")).toBeVisible();
  });

  test("tablists are independent of each other", async ({ page }) => {
    await mount(page, TABS);
    await page.locator("#t2").click();
    await expect(page.locator("#u1")).toHaveAttribute("aria-selected", "true");
    await expect(page.locator("#q1")).toBeVisible();
    await expect(page.locator("#q2")).toBeHidden();
  });
});

/* --------------------------------------------------------------------- modal */

const MODAL = `
  <button data-modal-open="m1" id="open-m1">Open</button>
  <button data-modal-open="nope" id="open-missing">Open missing</button>
  <dialog class="modal" id="m1">
    <p id="m1-body">Body</p>
    <button data-modal-close id="close-m1">Close</button>
  </dialog>`;

test.describe("modal", () => {
  test("opens as a modal dialog and closes from the close button", async ({ page }) => {
    await mount(page, MODAL);
    await page.locator("#open-m1").click();
    expect(await page.$eval("#m1", (el) => el.open && el.matches(":modal"))).toBe(true);

    await page.locator("#close-m1").click();
    expect(await page.$eval("#m1", (el) => el.open)).toBe(false);
  });

  test("clicking the backdrop closes it, clicking the body does not", async ({ page }) => {
    await mount(page, MODAL);
    await page.locator("#open-m1").click();

    await page.locator("#m1-body").click();
    expect(await page.$eval("#m1", (el) => el.open)).toBe(true);

    await page.mouse.click(4, 4); // backdrop belongs to the dialog element itself
    expect(await page.$eval("#m1", (el) => el.open)).toBe(false);
  });

  test("a data-modal-open pointing at a missing id is a no-op", async ({ page }) => {
    await mount(page, MODAL);
    await page.locator("#open-missing").click();
    expect(await page.$eval("#m1", (el) => el.open)).toBe(false);
    // the pageerror guard in afterEach asserts nothing threw
  });
});

/* ------------------------------------------------------------------- navbar */

test.describe("navbar", () => {
  const NAVBAR = `
    <nav class="navbar" id="nav">
      <button class="navbar-toggle" id="nav-btn"><span id="nav-icon">≡</span></button>
      <div class="navbar-menu"><a href="#">Home</a></div>
    </nav>`;

  test("toggle opens and closes the navbar", async ({ page }) => {
    await mount(page, NAVBAR);
    await page.locator("#nav-btn").click();
    await expect(page.locator("#nav")).toHaveClass(/is-open/);
    await page.locator("#nav-btn").click();
    await expect(page.locator("#nav")).not.toHaveClass(/is-open/);
  });

  test("clicking an element inside the toggle still toggles", async ({ page }) => {
    await mount(page, NAVBAR);
    await page.locator("#nav-icon").click();
    await expect(page.locator("#nav")).toHaveClass(/is-open/);
  });
});

/* ------------------------------------------------------------------- drawer */

test.describe("drawer", () => {
  // The overlay is an empty div and this suite loads no CSS, so it would collapse
  // to zero height and Playwright would refuse to click it. Give it a box, nothing
  // more — the real .drawer-overlay rules stay the business of visual.spec.js.
  const DRAWER_CSS = `<style>.drawer-overlay { width: 120px; height: 40px; }</style>`;

  const BY_ID = `
    <button data-drawer-open="dr" id="open-dr">Open</button>
    <div class="drawer" id="dr"><button data-drawer-close id="close-dr">×</button></div>
    <div class="drawer-overlay" id="dr-overlay"></div>`;

  const BY_SIBLING = `
    <button data-drawer-open="ds" id="open-ds">Open</button>
    <div class="drawer" id="ds">panel</div>
    <div class="drawer-overlay" id="ds-overlay-sibling"></div>`;

  test("opens drawer and overlay found by the id convention", async ({ page }) => {
    await mount(page, BY_ID, { head: DRAWER_CSS });
    await page.locator("#open-dr").click();
    await expect(page.locator("#dr")).toHaveClass(/is-open/);
    await expect(page.locator("#dr-overlay")).toHaveClass(/is-open/);
  });

  test("falls back to the next sibling as overlay", async ({ page }) => {
    await mount(page, BY_SIBLING, { head: DRAWER_CSS });
    await page.locator("#open-ds").click();
    await expect(page.locator("#ds")).toHaveClass(/is-open/);
    await expect(page.locator("#ds-overlay-sibling")).toHaveClass(/is-open/);
  });

  test("close button closes drawer and overlay together", async ({ page }) => {
    await mount(page, BY_ID, { head: DRAWER_CSS });
    await page.locator("#open-dr").click();
    await page.locator("#close-dr").click();
    await expect(page.locator("#dr")).not.toHaveClass(/is-open/);
    await expect(page.locator("#dr-overlay")).not.toHaveClass(/is-open/);
  });

  test("clicking the overlay closes the drawer", async ({ page }) => {
    await mount(page, BY_ID, { head: DRAWER_CSS });
    await page.locator("#open-dr").click();
    await page.locator("#dr-overlay").click();
    await expect(page.locator("#dr")).not.toHaveClass(/is-open/);
    await expect(page.locator("#dr-overlay")).not.toHaveClass(/is-open/);
  });

  test("Escape closes the drawer", async ({ page }) => {
    await mount(page, BY_ID, { head: DRAWER_CSS });
    await page.locator("#open-dr").click();
    await page.keyboard.press("Escape");
    await expect(page.locator("#dr")).not.toHaveClass(/is-open/);
    await expect(page.locator("#dr-overlay")).not.toHaveClass(/is-open/);
  });
});

/* ------------------------------------------------------------------ popover */

const POPOVER = `
  <div class="popover" id="pop">
    <button data-popover-toggle aria-expanded="false" id="pop-btn">Info</button>
    <div class="popover-body" id="pop-body">Text</div>
  </div>
  <div class="dropdown" id="dd">
    <button data-dropdown-toggle aria-expanded="false" id="dd-btn">Menu</button>
  </div>
  <p id="elsewhere">elsewhere</p>`;

test.describe("popover", () => {
  test("toggles and keeps aria-expanded in sync", async ({ page }) => {
    await mount(page, POPOVER);
    await page.locator("#pop-btn").click();
    await expect(page.locator("#pop")).toHaveClass(/is-open/);
    await expect(page.locator("#pop-btn")).toHaveAttribute("aria-expanded", "true");

    await page.locator("#pop-btn").click();
    await expect(page.locator("#pop")).not.toHaveClass(/is-open/);
    await expect(page.locator("#pop-btn")).toHaveAttribute("aria-expanded", "false");
  });

  test("clicking outside closes it and resets aria-expanded", async ({ page }) => {
    await mount(page, POPOVER);
    await page.locator("#pop-btn").click();
    await page.locator("#elsewhere").click();
    await expect(page.locator("#pop")).not.toHaveClass(/is-open/);
    await expect(page.locator("#pop-btn")).toHaveAttribute("aria-expanded", "false");
  });

  test("Escape closes it and resets aria-expanded", async ({ page }) => {
    await mount(page, POPOVER);
    await page.locator("#pop-btn").click();
    await page.keyboard.press("Escape");
    await expect(page.locator("#pop")).not.toHaveClass(/is-open/);
    await expect(page.locator("#pop-btn")).toHaveAttribute("aria-expanded", "false");
  });

  // Same rule as the dropdown: a click inside the panel still closes it.
  // Worth knowing, because the docs describe the popover as holding any content.
  test("clicking inside the panel closes the popover", async ({ page }) => {
    await mount(page, POPOVER);
    await page.locator("#pop-btn").click();
    await page.locator("#pop-body").click();
    await expect(page.locator("#pop")).not.toHaveClass(/is-open/);
    await expect(page.locator("#pop-btn")).toHaveAttribute("aria-expanded", "false");
  });

  test("opening a popover closes an open dropdown", async ({ page }) => {
    await mount(page, POPOVER);
    await page.locator("#dd-btn").click();
    await page.locator("#pop-btn").click();
    await expect(page.locator("#dd")).not.toHaveClass(/is-open/);
    await expect(page.locator("#dd-btn")).toHaveAttribute("aria-expanded", "false");
    await expect(page.locator("#pop")).toHaveClass(/is-open/);
  });
});

/* -------------------------------------------------------------------- toast */

test.describe("toast", () => {
  test("creates the live region on first call and announces politely", async ({ page }) => {
    await mount(page, `<main></main>`);
    await page.evaluate(() => window.Lombok.toast("Saved"));

    const region = page.locator(".toast-region");
    await expect(region).toHaveCount(1);
    await expect(region).toHaveAttribute("aria-live", "polite");

    const toast = region.locator(".toast");
    await expect(toast).toHaveAttribute("role", "status");
    await expect(toast).toHaveText("Saved");
  });

  test("variant maps to the alert-* class", async ({ page }) => {
    await mount(page, `<main></main>`);
    await page.evaluate(() => window.Lombok.toast("Done", { variant: "success" }));
    await expect(page.locator(".toast")).toHaveClass(/\balert-success\b/);
  });

  test("reuses an existing region instead of creating a second one", async ({ page }) => {
    await mount(page, `<div class="toast-region" id="preset" aria-live="polite"></div>`);
    await page.evaluate(() => {
      window.Lombok.toast("one");
      window.Lombok.toast("two");
    });
    await expect(page.locator(".toast-region")).toHaveCount(1);
    await expect(page.locator("#preset .toast")).toHaveCount(2);
  });

  test("removes itself after the timeout", async ({ page }) => {
    await mount(page, `<main></main>`);
    const attached = await page.evaluate(
      () => window.Lombok.toast("bye", { timeout: 100 }).isConnected,
    );
    expect(attached).toBe(true);
    await expect(page.locator(".toast")).toHaveCount(0);
  });

  test("escapes its message rather than parsing it as HTML", async ({ page }) => {
    await mount(page, `<main></main>`);
    await page.evaluate(() => window.Lombok.toast("<img src=x onerror=alert(1)>"));
    await expect(page.locator(".toast img")).toHaveCount(0);
    await expect(page.locator(".toast")).toHaveText("<img src=x onerror=alert(1)>");
  });
});

/* ----------------------------------------------------------------- carousel */

// Fixed geometry so the expected offsets are exact: slide 200px + gap 16px = 216.
const CAROUSEL_CSS = `<style>
  .carousel-track { display: flex; gap: 16px; overflow-x: auto; width: 400px; scroll-behavior: auto; }
  .carousel-slide { flex: 0 0 200px; height: 60px; }
</style>`;

const CAROUSEL = `
  <div class="carousel">
    <button class="carousel-prev" id="prev">‹</button>
    <div class="carousel-track" id="track">
      <div class="carousel-slide">1</div>
      <div class="carousel-slide">2</div>
      <div class="carousel-slide">3</div>
      <div class="carousel-slide">4</div>
    </div>
    <button class="carousel-next" id="next">›</button>
    <div class="carousel-dots" id="dots">
      <button></button><button></button><button></button><button></button>
    </div>
  </div>`;

const scrollLeft = (page) =>
  expect.poll(() => page.$eval("#track", (t) => Math.round(t.scrollLeft)), { timeout: 3000 });

test.describe("carousel", () => {
  test("next advances exactly one slide, not the whole track", async ({ page }) => {
    await mount(page, CAROUSEL, { head: CAROUSEL_CSS });
    await page.locator("#next").click();
    await scrollLeft(page).toBe(216);
    await page.locator("#next").click();
    await scrollLeft(page).toBe(432);
  });

  test("prev steps back one slide", async ({ page }) => {
    await mount(page, CAROUSEL, { head: CAROUSEL_CSS });
    await page.locator("#next").click();
    // Settle before clicking again: scrollBy is relative to the live scroll
    // position, so a second click mid-animation advances from wherever the
    // animation happens to be, not from the previous slide boundary.
    await scrollLeft(page).toBe(216);
    await page.locator("#next").click();
    await scrollLeft(page).toBe(432);
    await page.locator("#prev").click();
    await scrollLeft(page).toBe(216);
  });

  test("dot jumps to its own index", async ({ page }) => {
    await mount(page, CAROUSEL, { head: CAROUSEL_CSS });
    await page.locator("#dots > button").nth(2).click();
    await scrollLeft(page).toBe(432);
  });

  test("scrolling marks the matching dot active", async ({ page }) => {
    await mount(page, CAROUSEL, { head: CAROUSEL_CSS });
    await page.locator("#next").click();
    await expect(page.locator("#dots > button").nth(1)).toHaveClass(/is-active/);
    await expect(page.locator("#dots > button").nth(0)).not.toHaveClass(/is-active/);
  });

  test("direction inverts under dir=rtl", async ({ page }) => {
    await mount(page, CAROUSEL, { head: CAROUSEL_CSS, dir: "rtl" });
    await page.locator("#next").click();
    await scrollLeft(page).toBe(-216);
  });
});

/* --------------------------------------------------------------- table sort */

const TABLE = `
  <table class="table" id="tbl">
    <thead>
      <tr>
        <th aria-sort="none" id="th-name">Name</th>
        <th aria-sort="none" id="th-qty">Qty</th>
        <th id="th-note">Note</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Cherry</td><td>10</td><td>c</td></tr>
      <tr><td>apple</td><td>2</td><td>a</td></tr>
      <tr><td>Banana</td><td>33</td><td>b</td></tr>
    </tbody>
  </table>`;

const column = (page, index) =>
  page.$$eval(`#tbl tbody tr`, (rows, i) => rows.map((r) => r.cells[i].textContent), index);

test.describe("table sort", () => {
  test("sorts numerically, not lexically", async ({ page }) => {
    await mount(page, TABLE);
    await page.locator("#th-qty").click();
    // lexical order would be 10, 2, 33
    expect(await column(page, 1)).toEqual(["2", "10", "33"]);
    await expect(page.locator("#th-qty")).toHaveAttribute("aria-sort", "ascending");
  });

  test("second click reverses direction", async ({ page }) => {
    await mount(page, TABLE);
    await page.locator("#th-qty").click();
    await page.locator("#th-qty").click();
    expect(await column(page, 1)).toEqual(["33", "10", "2"]);
    await expect(page.locator("#th-qty")).toHaveAttribute("aria-sort", "descending");
  });

  test("sorts strings by collation, so case does not split the alphabet", async ({ page }) => {
    await mount(page, TABLE);
    await page.locator("#th-name").click();
    // a naive ASCII sort would put "apple" last
    expect(await column(page, 0)).toEqual(["apple", "Banana", "Cherry"]);
  });

  test("sorting another column resets the previous aria-sort", async ({ page }) => {
    await mount(page, TABLE);
    await page.locator("#th-qty").click();
    await page.locator("#th-name").click();
    await expect(page.locator("#th-qty")).toHaveAttribute("aria-sort", "none");
    await expect(page.locator("#th-name")).toHaveAttribute("aria-sort", "ascending");
  });

  test("a header without aria-sort is inert", async ({ page }) => {
    await mount(page, TABLE);
    const before = await column(page, 2);
    await page.locator("#th-note").click();
    expect(await column(page, 2)).toEqual(before);
  });

  test("row cells stay together when rows move", async ({ page }) => {
    await mount(page, TABLE);
    await page.locator("#th-qty").click();
    expect(await column(page, 0)).toEqual(["apple", "Cherry", "Banana"]);
    expect(await column(page, 2)).toEqual(["a", "c", "b"]);
  });
});
