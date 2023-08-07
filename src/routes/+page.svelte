<script>
  import { fade } from 'svelte/transition';

  let firstMessage = "¡Feliz cumple Saaaam 🦊💟!"
  let currentText = firstMessage;
  let newText = '¡26 bonis!';

  function toggleText() {
    currentText = currentText === firstMessage ? newText : firstMessage;
  }

  const interval = setInterval(toggleText, 3999);
</script>

<div class="content">
  <a href="/coupon" class="link-main">
    <div class="kuromi" />
  </a>
  <h1 class="happy-birthday" transition:fade>
    {currentText}
  </h1>
  <a href="/gift" class="link-main">
    <img src="/images/kuromi2.gif" alt="Kuromi" />
  </a>
</div>
