<script>
  import { createEventDispatcher } from 'svelte';
  export let modalOpen = false;
  export let projects = [];
  export let modalIndex = 0;

  const dispatch = createEventDispatcher();

  $: currentProject = projects[modalIndex] || null;

  function close() {
    console.log('Closing modal');
    dispatch('close'); // tell parent to close
  }

  function clickInside(e) {
    e.stopPropagation();
  }
</script>

{#if modalOpen && currentProject}
  <div
    class="fixed inset-0 z-50 flex items-center justify-center bg-black/60"
    on:click={close}
  >
    <div
      class="bg-gray-900 p-6 rounded-lg max-w-md w-full text-white"
      on:click={clickInside}
    >
      <h2 class="text-xl font-bold mb-2 neon-green">{currentProject.title}</h2>
      <p class="text-sm">{currentProject.desc}</p>
      <div class="mt-4 flex justify-end gap-2">
        <a
          class="px-4 py-2 bg-green-500 rounded hover:bg-green-600"
          href={currentProject.href}
          target="_blank"
          rel="noopener noreferrer"
        >
          Open Repo
        </a>
        <button class="px-4 py-2 bg-gray-700 rounded hover:bg-gray-600" on:click={close}>
          Close
        </button>
      </div>
    </div>
  </div>
{/if}
