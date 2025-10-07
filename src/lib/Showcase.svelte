<script>
  let showcase = [
    { title: 'Cognivue (Highlight)', desc: 'A focused demo exploring interactive UI patterns and micro-animations.', link: 'https://moondip-konwar.github.io/Cognivue/', tags: ['Vue','UI'] },
    { title: 'Todo App (Case)', desc: 'Simple reactive todo app that demonstrates state management and design restraint.', link: 'https://github.com/Moondip-Konwar/Todo-App', tags: ['Vanilla','Design'] },
    { title: 'MicroPython LED', desc: 'ESP32/ESP8266 MicroPython script for addressable LED effects — quick hack, huge satisfaction.', link: '#', tags: ['MicroPython','Hardware'] }
  ];
</script>

<section id="showcase" class="card mt-6 reveal">
  <div class="flex items-center justify-between">
    <h2 class="text-2xl neon-green">Showcase</h2>
    <div class="muted text-sm">Tight, editable highlights — low maintenance</div>
  </div>

  <div class="mt-4 showcase-grid" id="showcaseGrid">
    {#each showcase as s}
      <div class="showcase-card reveal">
        <h3 class="font-semibold neon-green">{s.title}</h3>
        <p class="muted mt-2">{s.desc}</p>
        <div class="mt-3 flex gap-2">
          {#each s.tags as t}
            <span class="px-2 py-1 rounded-full bg-black/20 muted">{t}</span>
          {/each}
        </div>
        <div class="mt-3">
          <a href={s.link} class="px-3 py-1 rounded-md bg-black/20">Open</a>
        </div>
      </div>
    {/each}
  </div>
</section>
