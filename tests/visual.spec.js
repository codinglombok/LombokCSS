import { test, expect } from "@playwright/test";
import { pathToFileURL } from "node:url";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const docs = (file) => pathToFileURL(path.resolve(__dirname, "../docs", file)).href;

const STYLES = [
  "modern-corporate-flat",
  "resonant-stark",
  "neo-brutalism",
  "semantic-minimalist",
  "glassmorphism",
];

// 1) Buttons block must look right in every design style (light, LTR).
for (const style of STYLES) {
  test(`buttons · ${style}`, async ({ page }) => {
    await page.goto(`${docs("components.html")}?style=${style}&theme=light&dir=ltr`);
    const block = page.locator(".docs-content .example").first();
    await block.scrollIntoViewIfNeeded();
    await expect(block).toHaveScreenshot(`buttons-${style}.png`);
  });
}

// 1b) Alerts must stay readable in every style (regression guard for contrast).
for (const style of STYLES) {
  test(`alerts · ${style}`, async ({ page }) => {
    await page.goto(`${docs("components.html")}?style=${style}&theme=light&dir=ltr`);
    const block = page
      .locator(".docs-content .example")
      .filter({ has: page.locator(".alert") })
      .first();
    await block.scrollIntoViewIfNeeded();
    await expect(block).toHaveScreenshot(`alerts-${style}.png`);
  });
}

// 2) Dark mode + RTL on the default style.
test("buttons · corporate dark", async ({ page }) => {
  await page.goto(`${docs("components.html")}?style=modern-corporate-flat&theme=dark&dir=ltr`);
  const block = page.locator(".docs-content .example").first();
  await block.scrollIntoViewIfNeeded();
  await expect(block).toHaveScreenshot("buttons-corporate-dark.png");
});

test("buttons · corporate rtl", async ({ page }) => {
  await page.goto(`${docs("components.html")}?style=modern-corporate-flat&theme=light&dir=rtl`);
  const block = page.locator(".docs-content .example").first();
  await block.scrollIntoViewIfNeeded();
  await expect(block).toHaveScreenshot("buttons-corporate-rtl.png");
});

// 3) Native validation styling becomes visible after invalid input.
test("forms · invalid email reveals error", async ({ page }) => {
  await page.goto(`${docs("forms.html")}?style=modern-corporate-flat&theme=light&dir=ltr`);
  await page.fill("#fv1", "not-an-email");
  await page.locator("#fv2").click(); // blur the email field
  const field = page.locator("#fv1").locator("xpath=ancestor::div[contains(@class,'field')]");
  await field.scrollIntoViewIfNeeded();
  await expect(field).toHaveScreenshot("forms-invalid-email.png");
});
