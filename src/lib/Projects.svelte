<script>
import { onMount } from 'svelte';
import Modal from './Modal.svelte';

let projects = [];
let modalOpen = false;
let modalIndex = 0;

onMount(async () => {
  const res = await fetch('https://api.github.com/users/Moondip-Konwar/repos');
  const data = await res.json();
  console.log('GitHub API response:', data);

  projects = data.map(repo => ({
    title: repo.name,
    href: repo.html_url,
    desc: repo.description || 'No description provided.',
    tags: repo.topics || [],
    iconClass: repo.fork ? 'fa-solid fa-code-branch' : 'fa-brands fa-github'
  }));
  console.log('Processed projects:', projects);
});
</script>

<section id="projects" class="card mt-6 reveal">
  <div class="flex items-center justify-between">
    <h2 class="text-2xl neon-green">Projects</h2>
    <div class="muted text-sm">(projects loaded via JS)</div>
  </div>

  <div class="projects-grid mt-4">
    {#each projects as p, i (p.title)}
      <button class="project-card flex items-start gap-3 p-3 bg-gray-800/50 rounded" type="button"
        on:click={() => { modalIndex = i; modalOpen = true; console.log('Clicked project:', p); }}>
        <div class="w-12 h-12 rounded-lg grid place-items-center bg-black/40">
          <i class={p.iconClass + ' fa-lg neon-green'}></i>
        </div>
        <div class="min-w-0">
          <h3 class="font-semibold">{p.title}</h3>
          <p class="muted text-sm mt-1">{p.desc}</p>
          <div class="mt-1 flex flex-wrap gap-1 text-xs text-gray-400">
            {#each p.tags as tag}
              <span class="px-2 py-0.5 bg-gray-700 rounded">{tag}</span>
            {/each}
          </div>
        </div>
      </button>
    {/each}
  </div>

  <Modal {modalOpen} {modalIndex} {projects} />
</section>
