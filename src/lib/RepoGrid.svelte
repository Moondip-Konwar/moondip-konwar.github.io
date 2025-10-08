<script>
  import { onMount } from 'svelte';
  import Modal from './Modal.svelte';

  export let title = 'Repositories';
  export let apiUrl = '';
  export let note = '';
  export let icon = 'fa-solid fa-code-branch';

  let repos = [];
  let modalOpen = false;
  let modalIndex = 0;
  let loading = true;
  let error = null;

  onMount(async () => {
    try {
      const res = await fetch(apiUrl);
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();

      repos = data.map(repo => ({
        title: repo.name,
        href: repo.html_url,
        desc: repo.description || 'No description provided.',
        stars: repo.stargazers_count,
        lang: repo.language,
      }));
    } catch (e) {
      console.error('Failed to fetch repos:', e);
      error = e.message;
    } finally {
      loading = false;
    }
  });
</script>

<section class="card mt-6 reveal">
  <div class="flex items-center justify-between mb-3">
    <h2 class="text-2xl neon-green flex items-center gap-2">
      <i class={icon}></i> {title}
    </h2>
    {#if note}<div class="muted text-sm">{note}</div>{/if}
  </div>

  {#if loading}
    <div class="text-center py-8 muted text-sm">
      <i class="fa-solid fa-spinner fa-spin"></i> Loading...
    </div>
  {:else if error}
    <div class="text-center py-8 text-red-400 text-sm">
      <i class="fa-solid fa-triangle-exclamation"></i> {error}
    </div>
  {:else}
    <div class="projects-grid mt-4">
      {#each repos as p, i (p.title)}
        <button
          class="project-card card text-left px-6 py-3 cursor-pointer"
          on:click={() => { modalIndex = i; modalOpen = true; }}
        >
          <h3 class="font-semibold text-lg neon-green">{p.title}</h3>
          <p class="muted mt-1 text-sm line-clamp-2">{p.desc}</p>
          <div class="flex items-center gap-3 mt-2 text-xs opacity-80">
            {#if p.lang}
              <span><i class="fa-solid fa-code"></i> {p.lang}</span>
            {/if}
                  </div>
        </button>
      {/each}
    </div>
  {/if}

  <Modal {modalOpen} {modalIndex} projects={repos} on:close={() => modalOpen = false} />
</section>
