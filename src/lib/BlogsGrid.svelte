<script>
  import { onMount } from 'svelte';
  import { goto } from '$app/navigation';

  export let title = 'Blogs';
  export let id = 'blogs';
  export let blogFolder = '/blog/'; // static folder

  let blogs = [];

  // Auto-fetch list of blog HTML files in /static/blog
  onMount(async () => {
    try {
      // SvelteKit cannot list /static files dynamically, so you need a hardcoded index.json
      const res = await fetch('/blog/index.json'); // contains: ["first-blog.html", "second-blog.html"]
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      blogs = data.map(file => ({
        title: file.replace(/-/g, ' ').replace('.html',''), 
        slug: file.replace('.html','')
      }));
    } catch (e) {
      console.error('Failed to load blogs:', e);
    }
  });

  function openBlog(slug) {
    goto(`/blogs/${slug}`);
  }
</script>

<section class="card mt-6 reveal" id={id}>
  <div class="flex items-center justify-between mb-3">
    <h2 class="text-2xl flex items-center gap-2 neon-green">
      <i class="fa-solid fa-book-open"></i> {title}
    </h2>
  </div>

  <div class="projects-grid mt-4">
    {#each blogs as blog (blog.slug)}
      <button
        class="project-card text-left px-6 py-3 cursor-pointer"
        on:click={() => openBlog(blog.slug)}
      >
        <h3 class="font-semibold text-lg neon-green">{blog.title}</h3>
        <p class="muted mt-1 text-sm line-clamp-2">Read the full article</p>
      </button>
    {/each}
  </div>
</section>
