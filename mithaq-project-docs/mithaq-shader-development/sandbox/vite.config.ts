import { defineConfig } from 'vite';

export default defineConfig({
  cacheDir: 'vite-cache',
  server: {
    host: '127.0.0.1',
    port: 5176,
  },
  preview: {
    host: '127.0.0.1',
    port: 4176,
  },
});
