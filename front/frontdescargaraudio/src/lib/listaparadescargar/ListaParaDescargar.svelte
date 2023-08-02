<script lang="ts">
  import { ADescargarStore } from "./ListaADescargar";
</script>

<div
  class="w-full max-w-xl p-4 bg-white border border-gray-200 rounded-lg shadow sm:p-6 md:p-8 dark:bg-gray-800 dark:border-gray-700"
>
  <button
    on:click={() => ADescargarStore.descargarvideos()}
    class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-full text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
    >descargar</button
  >
  {#each $ADescargarStore as lista, i}
    <div class="flex">
      <img src={lista.miniatura} alt={lista.nombre} class="h-20 w-auto p-3" />
      <h3 class="text-xl font-thin text-gray-900 dark:text-white">
        {lista.nombre}
      </h3>
    </div>
  {/each}
</div>
