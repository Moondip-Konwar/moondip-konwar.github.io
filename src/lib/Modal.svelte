<script>
  import { createEventDispatcher } from 'svelte';
  export let modalOpen = false;
  export let projects = [];
  export let modalIndex = 0;

  const dispatch = createEventDispatcher();
  $: currentProject = projects[modalIndex] || null;

  function close() {
    dispatch('close');
  }

  function clickInside(e) {
    e.stopPropagation();
  }
</script>

{#if modalOpen && currentProject}
  <div
    class="modal-overlay"
    on:click={close}
  >
    <div
      class="modal-box card"
      on:click={clickInside}
    >
      <h2 class="text-xl font-bold mb-3 neon-green">{currentProject.title}</h2>
      <p class="muted text-sm leading-relaxed">{currentProject.desc}</p>

      <div class="mt-5 flex justify-end gap-3">
        <a
          class="modal-btn primary"
          href={currentProject.href}
          target="_blank"
          rel="noopener noreferrer"
        >
          Open Repo
        </a>
        <button class="modal-btn" on:click={close}>
          Close
        </button>
      </div>
    </div>
  </div>
{/if}

<style>
  /* --- Overlay --- */
  .modal-overlay {
    position: fixed;
    inset: 0;
    z-index: 80;
    background: rgba(0, 0, 0, 0.7);
    backdrop-filter: blur(8px);
    display: flex;
    align-items: center;
    justify-content: center;
    animation: fadeIn 0.25s ease-out;
  }

  /* --- Modal box --- */
  .modal-box {
    width: 90%;
    max-width: 480px;
    border-radius: 16px;
    padding: 22px;
    background: linear-gradient(180deg, rgba(255, 255, 255, 0.03), rgba(255, 255, 255, 0.015));
    border: 1px solid rgba(255, 255, 255, 0.04);
    box-shadow: 0 14px 48px rgba(0, 0, 0, 0.7),
                0 0 24px rgba(34, 255, 120, 0.06);
    transform: translateY(6px);
    animation: slideUp 0.25s cubic-bezier(.16, .9, .2, 1);
  }

  /* --- Buttons --- */
  .modal-btn {
    padding: 0.5rem 1.2rem;
    border-radius: 8px;
    font-weight: 600;
    border: 1px solid rgba(255, 255, 255, 0.08);
    background: rgba(255, 255, 255, 0.03);
    color: var(--muted);
    transition: all 0.25s ease;
  }

  .modal-btn:hover {
    border-color: rgba(34, 255, 120, 0.2);
    color: var(--green);
    transform: translateY(-2px);
  }

  .modal-btn.primary {
    background: linear-gradient(180deg, rgba(34, 255, 120, 0.12), rgba(34, 255, 120, 0.08));
    border-color: rgba(34, 255, 120, 0.18);
    color: var(--green);
  }

  .modal-btn.primary:hover {
    background: rgba(34, 255, 120, 0.18);
    box-shadow: 0 0 12px rgba(34, 255, 120, 0.18);
  }

  /* --- Animations --- */
  @keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
  }

  @keyframes slideUp {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
  }
</style>
