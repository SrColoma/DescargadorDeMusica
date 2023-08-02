<script lang="ts">
  import { ADescargarStore } from "$lib/listaparadescargar/ListaADescargar";
  let link: string = "";

</script>

<div
  class="w-full max-w-xl p-4 bg-white border border-gray-200 rounded-lg shadow sm:p-6 md:p-8 dark:bg-gray-800 dark:border-gray-700"
>
  <form class="space-y-6" action="#">
    <h5 class="text-xl font-medium text-gray-900 dark:text-white">Add link</h5>
    <div>
      <input
        bind:value={link}
        type="text"
        name="link"
        id="link"
        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full max-w-2xl p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
        required
      />
    </div>
    <div class="flex flex-row-reverse">
      <button
        on:click={() => {ADescargarStore.addvideo(link);link=""}}
        class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-full text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
        >+</button
      >
    </div>
  </form>
</div>

<!-- on:click={() => ADescargarStore.addvideo(link)} -->