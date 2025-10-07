<script>
  import { onMount } from 'svelte';
  const skills = [
    { name:'Vue / Nuxt', icon:'fa-brands fa-vuejs', val:80 },
    { name:'Python', icon:'fa-brands fa-python', val:80 },
    { name:'Godot / GDScript', icon:'fa-solid fa-gamepad', val:90 },
    { name:'Linux / Bash', icon:'fa-brands fa-linux', val:40 },
    { name:'Piano / Music', icon:'fa-solid fa-music', val:90 },
    { name:'C / C++', icon:'fa-solid fa-code', val:60 },
    { name:'MicroPython', icon:'fa-brands fa-python', val:70 },
    { name:'Dev Tools', icon:'fa-solid fa-terminal', val:72 },
  ];
  onMount(()=>{
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry=>{
        if(entry.isIntersecting){
          entry.target.classList.add('show');
          entry.target.id==='skills' && document.querySelectorAll('.skill-fill').forEach(sf=> sf.style.width = sf.dataset.val + '%');
        } else {
          entry.target.classList.remove('show');
          entry.target.id==='skills' && document.querySelectorAll('.skill-fill').forEach(sf=> sf.style.width='0%');
        }
      });
    }, { threshold:0.12 });
    document.querySelectorAll('.reveal').forEach(el=> observer.observe(el));
    observer.observe(document.getElementById('skills'));
  });
</script>

<section id="skills" class="card mt-6 reveal">
  <h2 class="text-2xl neon-green">Skills</h2>
  <div class="mt-4 skills-grid">
    {#each skills as s}
      <div class="skill-card">
        <i class="{s.icon} fa-2x neon-green"></i>
        <div class="skill-name">{s.name}</div>
        <div class="mt-3 skill-bar"><div class="skill-fill" data-val={s.val}></div></div>
      </div>
    {/each}
  </div>
</section>
