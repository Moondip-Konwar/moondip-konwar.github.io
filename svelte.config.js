import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

const config = {
  preprocess: vitePreprocess(),

  kit: {
    adapter: adapter({
      pages: 'build',
      assets: 'build',
      fallback: 'index.html'
    }),
    paths: {
      base: process.env.GITHUB_PAGES ? '/moondip-konwar.github.io' : ''
    },
    prerender: {
      entries: ['*'],
      handleMissingId: 'warn'
    }
  }
};

export default config;
