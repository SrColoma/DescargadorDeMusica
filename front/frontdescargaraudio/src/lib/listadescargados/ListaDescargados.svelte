<script lang="ts">
  import { onMount } from "svelte";
  import Audioplay from "./Audioplay.svelte";
  import { Descargados } from "./Descargados";


  onMount(async () => {
    Descargados.searchDescargados();
  });
</script>

<div
  class="overflow-y-auto w-full max-w-xl p-4 bg-white border border-gray-200 rounded-lg shadow sm:p-6 md:p-8 dark:bg-gray-800 dark:border-gray-700"
>

  {#each $Descargados as video}
    <Audioplay nombreaudio={video} />
    <br />
  {/each}
</div>
