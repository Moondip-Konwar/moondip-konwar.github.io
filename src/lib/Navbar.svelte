
<script>
  let open = false;
</script>

<header class="site-nav page-wrap">
  <div class="nav-inner card">
    <div class="brand">
      <div class="logo neon-green"><i class="fa-solid fa-terminal"></i></div>
      <div>
        <div class="text-sm muted">Moondip Konwar</div>
        <div class="text-xs muted">@some_useless_person</div>
      </div>
    </div>

    <nav class="nav-links" role="navigation" aria-label="main navigation">
      <a href="#about">About</a>
      <a href="#skills">Skills</a>
      <a href="#projects">Projects</a>
      <a href="#starred">Starred</a>
      <a href="#contact">Contact</a>
    </nav>

    <button class="mobile-toggle" aria-expanded={open} aria-controls="mobileMenu"
            on:click={() => open = !open} title="Open menu">
      {@html open ? '<i class="fa-solid fa-xmark fa-lg"></i>' : '<i class="fa-solid fa-bars fa-lg"></i>'}
    </button>
  </div>

  <div id="mobileMenu" class="mobile-menu" class:show={open} role="menu" aria-hidden={!open}>
    <div style="display:flex;flex-direction:column;gap:8px;">
      <a href="#about" role="menuitem" on:click={() => open = false}>About</a>
      <a href="#skills" role="menuitem" on:click={() => open = false}>Skills</a>
      <a href="#projects" role="menuitem" on:click={() => open = false}>Projects</a>
      <a href="#showcase" role="menuitem" on:click={() => open = false}>Showcase</a>
      <a href="#contact" role="menuitem" on:click={() => open = false}>Contact</a>
    </div>
  </div>
</header>
