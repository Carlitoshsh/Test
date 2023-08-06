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
      const response = await fetch("data/coupons.json");
      items = await response.json();
    }
  
  </script>
  
  <div class="content">
    <div class="gift">
      <a href="/">Volver</a>
      <img src="/images/kuromi3.gif" alt="Kuromi">
      <h2>¿Quieres comprar algo aqui?</h2>
      <div class="grid-container">
        {#each items as concert}
          <a class="grid-item-with-logo" href={concert.url} target="_blank">
            <img src="{concert.logo}" alt="{concert.name}" />
            <span>{concert.name}</span>
          </a>
        {/each}
      </div>
    </div>
  </div>
  