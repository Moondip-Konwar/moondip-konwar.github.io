<script>
  import { onMount } from 'svelte';
  import Modal from './Modal.svelte';

  export let title = 'Repositories';
  export let apiUrl = '';
  export let note = '';
  export let icon = 'fa-solid fa-code-branch';
  export let id = 'projects';

  let repos = [];
  let modalOpen = false;
  let modalIndex = 0;
  let loading = true;
  let error = null;

  // Pagination
  let visibleCount = 8; // 2 rows (desktop)
  let visibleCountMobile = 6;
  let increment = 8; // adds 2 rows per click

  function getInitialCount() {
    return typeof window !== 'undefined' && window.innerWidth < 768 ? visibleCountMobile : visibleCount;
  }

  // Weighted sort: 70% stars + 30% recency
  function sortRepos(a, b) {
    const now = Date.now();
    const ageA = now - new Date(a.updated).getTime();
    const ageB = now - new Date(b.updated).getTime();
    const normAge = (age) => 1 / (1 + age / (1000 * 60 * 60 * 24 * 30)); // month decay
    const scoreA = a.stars * 0.7 + normAge(ageA) * 1000 * 0.3;
    const scoreB = b.stars * 0.7 + normAge(ageB) * 1000 * 0.3;
    return scoreB - scoreA;
  }

  onMount(async () => {
    visibleCount = getInitialCount();
    if (typeof window !== 'undefined') {
      window.addEventListener('resize', () => {
        visibleCount = getInitialCount();
      });
    }

    try {
      const res = await fetch(apiUrl);
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();

      repos = data
        .map(repo => ({
          title: repo.name,
          href: repo.html_url,
          desc: repo.description || 'No description provided.',
          stars: repo.stargazers_count,
          lang: repo.language,
          updated: repo.updated_at,
        }))
        .sort(sortRepos);
    } catch (e) {
      console.error('Failed to fetch repos:', e);
      error = e.message;
    } finally {
      loading = false;
    }
  });

  function showMore() {
    visibleCount += increment;
  }
</script>

<section class="card mt-6 reveal" id={id}>
  <div class="flex items-center justify-between mb-3">
    <h2 class="text-2xl flex items-center gap-2 neon-green">
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
      {#each repos.slice(0, visibleCount) as p, i (p.title)}
        <button
          class="project-card text-left px-6 py-3 cursor-pointer"
          on:click={() => { modalIndex = i; modalOpen = true; }}
        >
          <h3 class="font-semibold text-lg neon-green">{p.title}</h3>
          <p class="muted mt-1 text-sm line-clamp-2">{p.desc}</p>
          <div class="flex items-center gap-3 mt-2 text-xs muted">
            {#if p.lang}
              <span><i class="fa-solid fa-code"></i> {p.lang}</span>
            {/if}
            <span><i class="fa-regular fa-clock"></i> Updated {new Date(p.updated).toLocaleDateString()}</span>
          </div>
        </button>
      {/each}
    </div>

    {#if repos.length > visibleCount}
      <div class="text-center mt-5">
        <button
          class="show-more-btn"
          on:click={showMore}
        >
          Show More
        </button>
      </div>
    {/if}
  {/if}

  <Modal {modalOpen} {modalIndex} projects={repos} on:close={() => modalOpen = false} />
</section>

<style>
  .projects-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 1rem;
  }

  .project-card {
    background: linear-gradient(180deg, var(--glass), rgba(255, 255, 255, 0.01));
    border: 1px solid rgba(255, 255, 255, 0.03);
    border-radius: 14px;
    transition: transform 0.2s, box-shadow 0.3s, border-color 0.2s;
    padding: 1rem 1.5rem;
  }

  .project-card:hover {
    transform: translateY(-6px);
    border-color: rgba(34, 255, 120, 0.12);
    box-shadow: 0 10px 30px rgba(34, 255, 120, 0.08);
  }

  .neon-green {
    color: var(--green);
    text-shadow: 0 0 14px rgba(34, 255, 120, 0.14), 0 0 36px rgba(34, 255, 120, 0.03);
  }

  .muted {
    color: var(--muted);
    opacity: 0.85;
  }

  .show-more-btn {
    color: var(--green);
    border: 1px solid rgba(34, 255, 120, 0.18);
    background: rgba(255, 255, 255, 0.02);
    padding: 8px 16px;
    border-radius: 10px;
    transition: all 0.25s ease;
  }

  .show-more-btn:hover {
    background: rgba(34, 255, 120, 0.1);
    color: var(--bg-1);
    box-shadow: 0 0 14px rgba(34, 255, 120, 0.25);
  }

  @media(max-width: 768px) {
    .projects-grid {
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    }
  }
</style>
