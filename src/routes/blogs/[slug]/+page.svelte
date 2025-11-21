<script>
	import { onMount } from 'svelte';
	import { page } from '$app/stores';

	import Footer from '$lib/Footer.svelte';
	import Fireflies from '$lib/Fireflies.svelte';

	let htmlContent = '';
	let errorMsg = '';
	const slug = $page.params.slug; // grabs the slug from the URL

	onMount(async () => {
		try {
			const res = await fetch(`/blog/${slug}.html`);
			if (!res.ok) throw new Error('Blog not found');
			htmlContent = await res.text();
		} catch (e) {
			console.error(e);
			errorMsg = e.message;
		}
	});
</script>

<main class="page-wrap mx-auto mt-1 w-full max-w-7xl">
	{#if errorMsg}
		<p class="text-red-400">{errorMsg}</p>
	{:else if htmlContent === ''}
		<p class="muted">Loading...</p>
	{:else}
		<!-- Inject blog HTML safely -->
		<div class="prose max-w-full text-white">
			{@html htmlContent}
		</div>
	{/if}
	<Footer />
</main>

<Fireflies />

<style>
	/* optional Tailwind typography styles for Markdown content */
	.prose h1,
	.prose h2,
	.prose h3,
	.prose h4,
	.prose h5,
	.prose h6 {
		color: var(--muted);
	}

	.prose p,
	.prose li,
	.prose blockquote {
		color: var(--muted);
	}

	.prose blockquote {
		border-left: 4px solid var(--green);
		padding-left: 1rem;
		font-style: italic;
	}
</style>
