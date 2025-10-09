<script>
  import { onMount } from 'svelte';
  let btnProjects;
  onMount(() => {
    btnProjects.addEventListener('click', e => {
      e.preventDefault();
      document.querySelector('#projects').scrollIntoView({behavior:'smooth', block:'start'});
      setTimeout(()=> window.scrollBy({top:-22, behavior:'smooth'}), 220);
      setTimeout(()=> document.querySelector('#projects').classList.add('pulse-small'), 520);
      setTimeout(()=> document.querySelector('#projects').classList.remove('pulse-small'), 1620);
    });
  });
</script>

<section class="card hero reveal" id="hero">
  <div class="hero-left">
    <h1 class="text-5xl md:text-6xl font-extrabold neon-green">Moondip Konwar</h1>
    <div class="mt-2 text-sm muted flex items-center gap-3">
      <span>@some_useless_person</span>
      <span class="px-2 py-1 rounded-full bg-black/25 text-xs">Vue • Nuxt • Godot • Python • Linux</span>
    </div>

    <p class="mt-4 muted">I build interactive front-ends with <strong class="neon-green">Vue/Nuxt</strong>, craft games in <strong class="neon-green">Godot</strong>, and write Python & MicroPython tools. I like clean UI, deterministic behavior, and terminal-based rituals.<br><br><strong>This site is still in development</strong> and probably forever will. (i am lazy)</p>
    
    <div class="mt-6 flex gap-3">
      <a bind:this={btnProjects} class="inline-flex items-center gap-2 px-4 py-2 rounded-md bg-black/25 hover:bg-black/35" href="#projects">
        View Projects <i class="fa-solid fa-arrow-right ml-1 neon-green"></i>
      </a>
      <a class="inline-flex items-center gap-2 px-4 py-2 rounded-md bg-black/25 hover:bg-black/35" href="#showcase">
        Showcase <i class="fa-solid fa-star ml-1 neon-green"></i>
      </a>
    </div>
  </div>

  <div class="hero-right">
    <div id="mascotWrap" class="reveal" aria-hidden>
      <img src="assets/mascot.jpeg" alt="Mascot" />
      <div class="mascot-spark" aria-hidden></div>
    </div>
  </div>
</section>
