import fs from 'node:fs/promises';
import path from 'node:path';
import { pathToFileURL } from 'node:url';

const playwrightModule = await import(
  pathToFileURL(
    'C:/Users/User/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/.pnpm/playwright@1.61.1/node_modules/playwright/index.mjs',
  ).href
);
const { chromium } = playwrightModule;

const ROOT = 'D:/Clinets/MITHAQ/MITHAQ/mithaq-project-docs/mithaq-workshop-dossier-assets';
const CAPTURES = path.join(ROOT, 'captures');
const REPORTS = path.join(ROOT, 'reports');
const browserPath = 'C:/Users/User/AppData/Local/ms-playwright/chromium_headless_shell-1228/chrome-headless-shell-win64/chrome-headless-shell.exe';
const baseUrl = process.env.MITHAQ_DOSSIER_URL ?? 'http://127.0.0.1:5340/';

const modes = [
  ['resting', 'dossier-desktop-resting.png'],
  ['hover', 'dossier-desktop-hover.png'],
  ['multiple', 'dossier-multiple-layout.png'],
  ['mobile-light', 'dossier-mobile-light.png'],
  ['selected', 'dossier-selected-reference.png'],
  ['wireframe', 'dossier-wireframe-debug.png'],
];

const browser = await chromium.launch({
  executablePath: browserPath,
  headless: true,
  args: ['--use-angle=swiftshader', '--disable-gpu-sandbox'],
});

const results = [];

for (const [mode, fileName] of modes) {
  const consoleErrors = [];
  const page = await browser.newPage({
    viewport: mode === 'mobile-light' ? { width: 390, height: 844 } : { width: 1440, height: 900 },
    deviceScaleFactor: mode === 'mobile-light' ? 2 : 1,
  });
  page.on('console', (message) => {
    if (message.type() === 'error') {
      consoleErrors.push(message.text());
    }
  });
  page.on('pageerror', (error) => {
    consoleErrors.push(error.message);
  });

  await page.goto(`${baseUrl}?mode=${mode}`, { waitUntil: 'networkidle', timeout: 45000 });
  await page.waitForTimeout(2800);
  const metrics = await page.evaluate(() => window.__MITHAQ_DOSSIER_METRICS__ ?? null);
  await page.screenshot({ path: path.join(CAPTURES, fileName), fullPage: true });
  results.push({
    mode,
    capture: `captures/${fileName}`,
    consoleErrors,
    metrics,
  });
  await page.close();
}

await browser.close();

await fs.writeFile(
  path.join(REPORTS, 'dossier-sandbox-validation.json'),
  JSON.stringify(
    {
      timestamp: new Date().toISOString(),
      baseUrl,
      browser: 'Chromium headless shell via Playwright',
      results,
    },
    null,
    2,
  ),
);

console.log(JSON.stringify({ captures: results.length, errors: results.flatMap((item) => item.consoleErrors).length }));
