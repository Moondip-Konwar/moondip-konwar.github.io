<script>
  export let projects = [];
  export let modalOpen = false;
  let current = 0;

  function open(index) {
    current = index;
    modalOpen = true;
  }

  function close() {
    modalOpen = false;
  }

  $: currentProject = projects[current] || {};
</script>
{#if modalOpen && projects[modalIndex]}
  <div class="modal-overlay fixed inset-0 bg-black/70 flex items-center justify-center z-50" on:click={() => modalOpen = false}>
    <div 
      class="modal-content bg-gray-900 p-6 rounded-md w-11/12 max-w-lg relative" 
      on:click|stopPropagation
    >
      {console.log('Rendering modal for:', projects[modalIndex])}
      <button class="absolute top-2 right-2 text-gray-400 hover:text-white" on:click={() => modalOpen = false}>✕</button>

      <h2 class="text-xl font-bold neon-green mb-2">{projects[modalIndex].title}</h2>
      <p class="mb-3">{projects[modalIndex].desc}</p>
      <div class="flex flex-wrap gap-2 mb-3">
        {#each projects[modalIndex].tags as tag}
          <span class="px-2 py-0.5 bg-gray-800 rounded text-xs">{tag}</span>
        {/each}
      </div>
      <a 
        href={projects[modalIndex].href} 
        target="_blank" 
        class="inline-block mt-2 px-4 py-2 bg-neon-green text-black font-semibold rounded hover:brightness-125 transition"
      >
        View Project
      </a>
    </div>
  </div>
{/if}

<style>
  .modal-overlay {
    animation: fadeIn 0.2s ease forwards;
  }
  .modal-card {
    animation: popIn 0.2s ease forwards;
  }

  @keyframes fadeIn { from {opacity:0;} to {opacity:1;} }
  @keyframes popIn { from {opacity:0; transform:scale(0.9);} to {opacity:1; transform:scale(1);} }
</style>
