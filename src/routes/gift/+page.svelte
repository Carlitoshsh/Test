<script>
  import { onMount } from "svelte";

  /**
   * @type {any[]}
   */
  let items = [];

  onMount(() => {
    loadData();
  });

  async function loadData() {
    const response = await fetch("data/concerts.json");
    items = await response.json();
  }

</script>

<div class="content">
  <div class="gift">
    <a href="/">Volver</a>
    <img src="/images/kuromi4.gif" alt="Kuromi">
    <h2>¿Quieres música?</h2>
    <div class="grid-container">
      {#each items as concert}
        <a class="grid-item" href={concert.href} target="_blank">
          <img src="{concert.src}" alt="{concert.alt}" />
        </a>
      {/each}
    </div>
  </div>
</div>
