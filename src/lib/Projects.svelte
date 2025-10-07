<script>
  import Modal from './Modal.svelte';

  let projects = [
    { title: 'Cognivue', href: 'https://moondip-konwar.github.io/Cognivue/', iconClass: 'fa-solid fa-brain', desc: 'Interactive front-end demo with visualizations and UX experiments.', tags: ['Vue','UX'] },
    { title: 'Todo App', href: 'https://github.com/Moondip-Konwar/Todo-App', iconClass: 'fa-solid fa-list-check', desc: 'Reactive todo app with clean UI and simple state management.', tags: ['Vanilla','Productivity'] },
  ];

  let modalOpen = false;
  let modalRef;

  function openModal(i) {
    modalRef.open(i);
  }
</script>

<section id="projects" class="card mt-6 reveal">
  <div class="flex items-center justify-between">
    <h2 class="text-2xl neon-green">Projects</h2>
    <div class="muted text-sm">(projects loaded via JS)</div>
  </div>

  <div class="projects-grid mt-4" aria-live="polite">
    {#each projects as p, i}
      <button class="project-card reveal" type="button" on:click={() => openModal(i)}>
        <div class="flex items-start gap-3">
          <div class="w-12 h-12 rounded-lg bg-black/30 grid place-items-center">
            <i class={p.iconClass + ' fa-lg neon-green'}></i>
          </div>
          <div class="min-w-0">
            <h3 class="font-semibold">{p.title}</h3>
            <p class="muted text-sm mt-1">{p.desc}</p>
          </div>
        </div>
      </button>
    {/each}
  </div>

  <Modal bind:this={modalRef} {projects} bind:modalOpen />
</section>
