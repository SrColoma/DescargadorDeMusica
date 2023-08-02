<script lang="ts">
  import { onMount } from "svelte";
  import Audioplay from "./Audioplay.svelte";

  let apiData: string[] = [];

  onMount(async () => {
    fetch("http://127.0.0.1:5000/externos/getDescargados")
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        apiData = data["list"];
      })
      .catch((error) => {
        console.log(error);
        return [];
      });
  });
</script>

<div
  class="w-full max-w-xl p-4 bg-white border border-gray-200 rounded-lg shadow sm:p-6 md:p-8 dark:bg-gray-800 dark:border-gray-700"
>
  {#await apiData}
    <p>...cargando</p>
  {:then apiData}
    {#each apiData as item}
      <Audioplay nombreaudio={item} />
      <br />
    {/each}
  {/await}
</div>
