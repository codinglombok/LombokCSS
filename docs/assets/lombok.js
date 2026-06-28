/* LombokCSS — lombok.js (optional, ~1.5KB). Zero dependencies.
   Enhances: dropdowns, tabs, modals, toasts, table sort, navbar toggle.
   Everything degrades gracefully if JS is off (details/dialog are native). */
(function () {
  "use strict";
  var d = document;

  /* Dropdowns: toggle [data-dropdown] -> nearest .dropdown gets .is-open */
  d.addEventListener("click", function (e) {
    var t = e.target.closest("[data-dropdown-toggle]");
    var open = d.querySelector(".dropdown.is-open");
    if (open && (!t || !open.contains(t))) open.classList.remove("is-open");
    if (t) {
      e.preventDefault();
      var dd = t.closest(".dropdown");
      if (dd) { dd.classList.toggle("is-open");
        t.setAttribute("aria-expanded", dd.classList.contains("is-open")); }
    }
  });
  d.addEventListener("keydown", function (e) {
    if (e.key === "Escape") { var o = d.querySelector(".dropdown.is-open"); if (o) o.classList.remove("is-open"); }
  });

  /* Tabs: [role=tablist] with buttons whose aria-controls -> panel id */
  d.querySelectorAll('[role="tablist"]').forEach(function (list) {
    var tabs = list.querySelectorAll('[role="tab"]');
    tabs.forEach(function (tab) {
      tab.addEventListener("click", function () {
        tabs.forEach(function (x) {
          x.setAttribute("aria-selected", "false");
          var p = d.getElementById(x.getAttribute("aria-controls"));
          if (p) p.hidden = true;
        });
        tab.setAttribute("aria-selected", "true");
        var panel = d.getElementById(tab.getAttribute("aria-controls"));
        if (panel) panel.hidden = false;
      });
    });
  });

  /* Modal: [data-modal-open="id"] / [data-modal-close]; uses native <dialog> */
  d.addEventListener("click", function (e) {
    var op = e.target.closest("[data-modal-open]");
    if (op) { var m = d.getElementById(op.getAttribute("data-modal-open")); if (m && m.showModal) m.showModal(); }
    var cl = e.target.closest("[data-modal-close]");
    if (cl) { var dlg = cl.closest("dialog"); if (dlg) dlg.close(); }
  });
  /* click on backdrop closes */
  d.querySelectorAll("dialog.modal").forEach(function (dlg) {
    dlg.addEventListener("click", function (e) { if (e.target === dlg) dlg.close(); });
  });

  /* Navbar toggle (.navbar-toggle button toggles .is-open on .navbar) */
  d.addEventListener("click", function (e) {
    var b = e.target.closest(".navbar-toggle");
    if (b) { var nav = b.closest(".navbar"); if (nav) nav.classList.toggle("is-open"); }
  });

  /* Drawer / Offcanvas: [data-drawer-open="id"] / [data-drawer-close] */
  function closeDrawer(dr) {
    dr.classList.remove("is-open");
    var ov = d.getElementById(dr.id + "-overlay") || dr.nextElementSibling;
    if (ov && ov.classList.contains("drawer-overlay")) ov.classList.remove("is-open");
  }
  d.addEventListener("click", function (e) {
    var op = e.target.closest("[data-drawer-open]");
    if (op) {
      var dr = d.getElementById(op.getAttribute("data-drawer-open"));
      if (dr) { dr.classList.add("is-open");
        var ov = d.getElementById(dr.id + "-overlay") || dr.nextElementSibling;
        if (ov && ov.classList.contains("drawer-overlay")) ov.classList.add("is-open"); }
    }
    var cl = e.target.closest("[data-drawer-close], .drawer-overlay");
    if (cl) { var open = d.querySelector(".drawer.is-open"); if (open) closeDrawer(open); }
  });

  /* Popover: [data-popover-toggle] -> nearest .popover gets .is-open */
  d.addEventListener("click", function (e) {
    var t = e.target.closest("[data-popover-toggle]");
    var open = d.querySelector(".popover.is-open");
    if (open && (!t || !open.contains(t))) {
      open.classList.remove("is-open");
      var b = open.querySelector("[data-popover-toggle]"); if (b) b.setAttribute("aria-expanded", "false");
    }
    if (t) {
      e.preventDefault();
      var pop = t.closest(".popover");
      if (pop) { pop.classList.toggle("is-open");
        t.setAttribute("aria-expanded", pop.classList.contains("is-open")); }
    }
  });
  d.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      var dr = d.querySelector(".drawer.is-open"); if (dr) closeDrawer(dr);
      var po = d.querySelector(".popover.is-open"); if (po) po.classList.remove("is-open");
    }
  });

  /* Toast API: Lombok.toast("msg", {variant:"success", timeout:3000}) */
  window.Lombok = window.Lombok || {};
  window.Lombok.toast = function (msg, opts) {
    opts = opts || {};
    var region = d.querySelector(".toast-region");
    if (!region) { region = d.createElement("div"); region.className = "toast-region"; region.setAttribute("aria-live", "polite"); d.body.appendChild(region); }
    var el = d.createElement("div");
    el.className = "toast" + (opts.variant ? " alert-" + opts.variant : "");
    el.setAttribute("role", "status");
    el.textContent = msg;
    region.appendChild(el);
    setTimeout(function () { el.remove(); }, opts.timeout || 3500);
    return el;
  };

  /* Carousel: prev/next buttons + dots; scroll by one slide width */
  d.querySelectorAll(".carousel").forEach(function (c) {
    var track = c.querySelector(".carousel-track");
    if (!track) return;
    function step() {
      var slide = track.querySelector(".carousel-slide");
      var gap = parseFloat(getComputedStyle(track).columnGap || getComputedStyle(track).gap || 16) || 16;
      return slide ? slide.getBoundingClientRect().width + gap : track.clientWidth;
    }
    var dir = (d.documentElement.getAttribute("dir") === "rtl") ? -1 : 1;
    var prev = c.querySelector(".carousel-prev"), next = c.querySelector(".carousel-next");
    if (prev) prev.addEventListener("click", function () { track.scrollBy({ left: -step() * dir, behavior: "smooth" }); });
    if (next) next.addEventListener("click", function () { track.scrollBy({ left: step() * dir, behavior: "smooth" }); });
    var dots = c.querySelectorAll(".carousel-dots > *");
    dots.forEach(function (dot, i) {
      dot.addEventListener("click", function () { track.scrollTo({ left: step() * i * dir, behavior: "smooth" }); });
    });
    if (dots.length) track.addEventListener("scroll", function () {
      var idx = Math.round(Math.abs(track.scrollLeft) / step());
      dots.forEach(function (x, i) { x.classList.toggle("is-active", i === idx); });
    }, { passive: true });
  });

  /* Table sort: <th aria-sort> click sorts its column (string/number aware) */
  d.querySelectorAll("table.table thead th[aria-sort]").forEach(function (th) {
    th.addEventListener("click", function () {
      var table = th.closest("table"), tbody = table.tBodies[0];
      var idx = Array.prototype.indexOf.call(th.parentNode.children, th);
      var asc = th.getAttribute("aria-sort") !== "ascending";
      th.parentNode.querySelectorAll("th[aria-sort]").forEach(function (o) { o.setAttribute("aria-sort", "none"); });
      th.setAttribute("aria-sort", asc ? "ascending" : "descending");
      var rows = Array.prototype.slice.call(tbody.rows);
      rows.sort(function (a, b) {
        var x = a.cells[idx].textContent.trim(), y = b.cells[idx].textContent.trim();
        var nx = parseFloat(x), ny = parseFloat(y);
        var r = (!isNaN(nx) && !isNaN(ny)) ? nx - ny : x.localeCompare(y);
        return asc ? r : -r;
      });
      rows.forEach(function (r) { tbody.appendChild(r); });
    });
  });
})();
