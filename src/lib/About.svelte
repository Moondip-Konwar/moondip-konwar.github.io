<section id="about" class="card reveal mt-6">
	<h2 class="neon-green text-2xl">About Me</h2>
	<p class="muted mt-3" id="about-text">
		Working on brittle ideas and hoping they survive long enough to be called code. Builds messy
		front-ends, tries out doomed Godot prototypes, and scripts tiny Python automations that save 2
		minutes a week. Still rates too much anime on MAL and probably always will.
	</p>

	<style>
		/* Keyframes for floating & rotating letters */
		@keyframes floatRotate {
			0% {
				transform: translate(0, 0) rotate(0deg);
			}
			25% {
				transform: translate(-5px, 5px) rotate(-5deg);
			}
			50% {
				transform: translate(5px, -5px) rotate(5deg);
			}
			75% {
				transform: translate(-3px, -3px) rotate(-3deg);
			}
			100% {
				transform: translate(0, 0) rotate(0deg);
			}
		}

		/* Style for letter spans */
		#about-text span {
			display: inline-block;
			animation-name: floatRotate;
			animation-iteration-count: infinite;
			animation-timing-function: linear;
		}
	</style>

	<script>
		const paragraph = document.getElementById('about-text');
		const text = paragraph.textContent;
		paragraph.textContent = '';

		// Wrap each letter in a span
		text.split('').forEach((char) => {
			const span = document.createElement('span');
			span.textContent = char;

			// Random animation duration & delay for chaotic effect
			const duration = 1 + Math.random() * 2; // 1s → 3s
			const delay = Math.random(); // 0s → 1s
			span.style.animationDuration = `${duration}s`;
			span.style.animationDelay = `${delay}s`;

			paragraph.appendChild(span);
		});
	</script>
</section>
