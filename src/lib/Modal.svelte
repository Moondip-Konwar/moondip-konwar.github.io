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

{#if modalOpen}
  <div class="modal-overlay fixed inset-0 bg-black/60 backdrop-blur-sm flex items-center justify-center z-50"
       on:click={() => close()}>
    <div class="modal-card bg-gray-900 rounded-xl p-6 w-11/12 max-w-lg relative"
         on:click|stopPropagation>
      <button class="modal-close absolute top-3 right-3 text-xl" aria-label="Close modal" on:click={close}>
        &times;
      </button>

      <div class="flex items-center gap-4">
        <div class="w-12 h-12 rounded-lg bg-black/30 grid place-items-center">
          <i class={currentProject.iconClass + ' fa-lg neon-green'}></i>
        </div>
        <div>
          <h2 class="text-xl font-semibold neon-green">{currentProject.title}</h2>
          <p class="muted mt-1">{currentProject.desc}</p>
          <div class="mt-2 flex gap-2 flex-wrap">
            {#each currentProject.tags || [] as t}
              <span class="px-2 py-1 rounded-full bg-black/20 text-xs">{t}</span>
            {/each}
          </div>
        </div>
      </div>

      {#if currentProject.href}
        <div class="mt-4">
          <a href={currentProject.href} target="_blank" rel="noopener noreferrer"
             class="px-4 py-2 rounded-md bg-black/25 hover:bg-black/35">
            Visit Project
          </a>
        </div>
      {/if}
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
