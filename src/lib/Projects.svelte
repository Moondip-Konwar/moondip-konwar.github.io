<script>
import { onMount } from 'svelte';
import Modal from './Modal.svelte';

let projects = [];
let modalOpen = false;
let modalIndex = 0;

onMount(async () => {
  try {
    const res = await fetch('https://api.github.com/users/Moondip-Konwar/repos');
    const data = await res.json();

    projects = data.map(repo => ({
      title: repo.name,
      href: repo.html_url,
      desc: repo.description || 'No description provided.',
    }));

    console.log('Projects loaded:', projects);
  } catch (e) {
    console.error('Failed to fetch projects:', e);
  }
});
</script>

<section id="projects" class="card mt-6 reveal">
  <div class="flex items-center justify-between">
    <h2 class="text-2xl neon-green">Projects</h2>
    <div class="muted text-sm">(loaded from GitHub)</div>
  </div>

  <div class="projects-grid mt-4">
    {#each projects as p, i (p.title)}
      <button class="project-card card text-left px-6 py-3 cursor-pointer"
        on:click={() => { modalIndex = i; modalOpen = true; console.log('Clicked project:', p); }}>
        <h3 class="font-semibold text-lg neon-green">{p.title}</h3>
        <p class="muted mt-1 text-sm line-clamp-2">{p.desc}</p>
      </button>
    {/each}
  </div>

  <Modal {modalOpen} {modalIndex} {projects} />
</section>
