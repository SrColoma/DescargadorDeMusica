<script lang="ts">
  import { reproductorStore } from "$lib/Reproductor/ReproductorStore";
</script>

<div class="invisible grid place-items-center v-screen">
  <audio bind:this={reproductorStore.audioPlayer}  autoplay >
    <!-- <source src={reproductorStore.} type="audio/mpeg" /> -->
    Tu navegador no admite la reproducción de audio.
  </audio>
</div>


<!-- <script lang="ts">
  import { reproductorStore } from "./ReproductorStore";
</script>

<div class="grid place-items-center v-screen">
  <audio bind:this={reproductorStore.audioPlayer} controls autoplay >
    <source src={reproductorStore.} type="audio/mpeg" />
    Tu navegador no admite la reproducción de audio.
  </audio>
</div> -->

<!-- <script lang="ts">
  import { reproductorStore } from "./ReproductorStore.ts";
</script>

<div class="grid place-items-center v-screen">
  <audio bind:this={reproductorStore.audioPlayer}>
    <p>Tu navegador no soporta la reproducción de audio.</p>
  </audio>

  <button on:click={playing ? pause : changeAndPlay}>
    {#if $playing}
      Pausar
    {:else}
      Reproducir
    {/if}
  </button>

  <input type="text" bind:value={src} placeholder="URL del audio" />
  <button on:click={changeAndPlay}>Cambiar y Reproducir</button>
</div> -->
