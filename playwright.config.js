import { defineConfig } from "@playwright/test";

// Locally we reuse a preinstalled Chromium via PW_CHROMIUM_PATH.
// In CI (official Playwright container) the bundled browser is used.
const executablePath = process.env.PW_CHROMIUM_PATH || undefined;

export default defineConfig({
  testDir: "./tests",
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: 0,
  reporter: process.env.CI ? [["github"], ["list"]] : [["list"]],
  use: {
    viewport: { width: 1000, height: 760 },
    deviceScaleFactor: 1,
    reducedMotion: "reduce",
    launchOptions: executablePath ? { executablePath } : {},
  },
  expect: {
    toHaveScreenshot: {
      animations: "disabled",
      caret: "hide",
      // Tolerate sub-pixel/antialiasing differences across environments.
      threshold: 0.25,
      maxDiffPixelRatio: 0.03,
    },
  },
  projects: [{ name: "chromium", use: { browserName: "chromium" } }],
});
