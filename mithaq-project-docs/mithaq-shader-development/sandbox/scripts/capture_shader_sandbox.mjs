import http from 'node:http';
import { readFile } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { createRequire } from 'node:module';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const sandboxRoot = path.resolve(__dirname, '..');
const projectRoot = path.resolve(sandboxRoot, '..');
const distRoot = path.join(sandboxRoot, 'dist');
const captureRoot = path.join(projectRoot, 'captures');
const runtimeRequire = createRequire('C:/Users/User/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/.pnpm/playwright@1.60.0/node_modules/playwright/package.json');
const { chromium } = runtimeRequire('playwright');

const mime = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png',
  '.svg': 'image/svg+xml',
};

const server = http.createServer(async (req, res) => {
  const url = new URL(req.url ?? '/', 'http://127.0.0.1');
  const rawPath = decodeURIComponent(url.pathname === '/' ? '/index.html' : url.pathname);
  const target = path.normalize(path.join(distRoot, rawPath));
  const safeTarget = target.startsWith(distRoot) && existsSync(target) ? target : path.join(distRoot, 'index.html');
  try {
    const body = await readFile(safeTarget);
    res.writeHead(200, { 'content-type': mime[path.extname(safeTarget)] ?? 'application/octet-stream' });
    res.end(body);
  } catch (error) {
    res.writeHead(500, { 'content-type': 'text/plain' });
    res.end(String(error));
  }
});

await new Promise((resolve) => server.listen(5186, '127.0.0.1', resolve));

const captures = [
  ['ripple-demo.png', '/?mode=ripple&progress=0.58'],
  ['fracture-lines-demo.png', '/?mode=fracture&progress=0.68'],
  ['seal-emergence-demo.png', '/?mode=seal&progress=0.72'],
  ['atmospheric-particles-demo.png', '/?mode=particles&progress=0.64'],
  ['combined-shader-sandbox.png', '/?mode=combined&progress=0.70'],
];

const browserExecutable = 'C:/Users/User/AppData/Local/ms-playwright/chromium_headless_shell-1217/chrome-headless-shell-win64/chrome-headless-shell.exe';
const browser = await chromium.launch({ headless: true, executablePath: browserExecutable });
const page = await browser.newPage({ viewport: { width: 1440, height: 960 }, deviceScaleFactor: 1 });
const consoleMessages = [];
const pageErrors = [];
page.on('console', (msg) => {
  const text = msg.text();
  if (msg.type() === 'error' || /shader|webgl|error/i.test(text)) {
    consoleMessages.push({ type: msg.type(), text });
  }
});
page.on('pageerror', (error) => pageErrors.push(error.message));

for (const [fileName, route] of captures) {
  await page.goto(`http://127.0.0.1:5186${route}`, { waitUntil: 'networkidle' });
  await page.waitForSelector('canvas');
  await page.waitForTimeout(1200);
  await page.screenshot({ path: path.join(captureRoot, fileName), fullPage: true });
}

await browser.close();
server.close();

const result = {
  captures: captures.map(([fileName]) => path.join(captureRoot, fileName)),
  consoleMessages,
  pageErrors,
};

console.log(JSON.stringify(result, null, 2));
