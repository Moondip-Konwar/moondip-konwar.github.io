<script>
  import RepoGrid from './RepoGrid.svelte';
</script>

<RepoGrid
  title="Starred Repositories"
  apiUrl="https://api.github.com/users/Moondip-Konwar/starred"
  note="(your starred GitHub repos)"
  icon="fa-solid fa-star"
  id="starred"
/>
