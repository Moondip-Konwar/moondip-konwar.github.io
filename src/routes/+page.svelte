<script>
  import Navbar from '$lib/Navbar.svelte';
  import Hero from '$lib/Hero.svelte';
  import About from '$lib/About.svelte';
  import Skills from '$lib/Skills.svelte';
  import Projects from '$lib/Projects.svelte';
  import Starred from '$lib/Starred.svelte';
  import Showcase from '$lib/Showcase.svelte';
  import Contact from '$lib/Contact.svelte';
  import Footer from '$lib/Footer.svelte';
  import Fireflies from '$lib/Fireflies.svelte';
</script>

<Navbar />
<main class="page-wrap max-w-7xl mx-auto">
  <Hero />
  <About />
  <Skills />
  <Projects />
  <Starred />
  <Contact />
  <Footer />
</main>

<Fireflies />
