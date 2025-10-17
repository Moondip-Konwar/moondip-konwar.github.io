<script>
	import { onMount } from 'svelte';
	let btnProjects;
	onMount(() => {
		btnProjects.addEventListener('click', (e) => {
			e.preventDefault();
			document.querySelector('#projects').scrollIntoView({ behavior: 'smooth', block: 'start' });
			setTimeout(() => window.scrollBy({ top: -22, behavior: 'smooth' }), 220);
			setTimeout(() => document.querySelector('#projects').classList.add('pulse-small'), 520);
			setTimeout(() => document.querySelector('#projects').classList.remove('pulse-small'), 1620);
		});
	});
</script>

<section class="card hero reveal" id="hero">
	<div class="hero-left">
		<h1 class="neon-green text-5xl font-extrabold md:text-6xl">Moondip Konwar</h1>
		<div class="muted mt-2 flex items-center gap-3 text-sm">
			<span>@some_useless_person</span>
			<span class="rounded-full bg-black/25 px-2 py-1 text-xs"
				>Anime • Linux • Programming • Sorcery</span
			>
		</div>

		<p class="muted mt-4">
			Anime enthusiast, webnovel reader, and music lover. Builds interactive front-ends, crafts
			games, and tinkers with tools, drawn to clean UI, arcane workflows, and terminal-based
			rituals. Occasionally gets lost in <strong>Rain World</strong>.
		</p>
		<blockquote class="my-4 border-l-4 border-green-400 pl-4 text-gray-400 italic">
			Why finish today what you can put off indefinitely?
		</blockquote>
		<strong>This site is still in development</strong> and probably forever will.<br />

		<div class="mt-6 flex gap-3">
			<a
				bind:this={btnProjects}
				class="inline-flex items-center gap-2 rounded-md bg-black/25 px-4 py-2 hover:bg-black/35"
				href="#projects"
			>
				View Projects <i class="fa-solid fa-arrow-right neon-green ml-1"></i>
			</a>
			<a
				class="inline-flex items-center gap-2 rounded-md bg-black/25 px-4 py-2 hover:bg-black/35"
				href="#starred"
			>
				Starred <i class="fa-solid fa-star neon-green ml-1"></i>
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
