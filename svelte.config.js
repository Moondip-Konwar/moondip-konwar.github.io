import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
  preprocess: vitePreprocess(),

  kit: {
    adapter: adapter({
      // default options: pages/build/assets inside 'build' folder
      pages: 'build',
      assets: 'build',
      fallback: null
    }),
    paths: {
      base: process.env.GITHUB_PAGES ? '/moondip-konwar.github.io' : '',
    }
  }
};

export default config;
