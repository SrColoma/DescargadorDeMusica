<script lang="ts">
  export let nombreaudio: string;
  let isPlaying: boolean = false;
  let audioUrl: string = ""; // URL del audio obtenida desde el endpoint
  let audioElement: HTMLAudioElement;

  async function fetchAudio(filename: string): Promise<void> {
    try {
      audioUrl = `http://127.0.0.1:5000/externos/audio/${filename}`;

      // Actualizar el atributo src del elemento audio
      if (audioElement) {
        audioElement.src = audioUrl;
      }
      isPlaying = true;
    } catch (error) {
      console.error("Error al obtener el audio:", error);
    }
  }

  function playAudio(): void {
    if (audioElement) {
      audioElement.play();
    }
  }
</script>

<div class="flex">
  
  <div>
    {#if !isPlaying}
      <button
        on:click={() => fetchAudio(nombreaudio)}
        class="h-50 w-24 text-white bg-blue-700 hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 font-medium rounded-full text-sm px-5 py-2.5 text-center mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
      >
        🎧 Escuchar
      </button>
    {/if}
  
  
    {#if audioUrl}
      <div>
        <audio bind:this={audioElement} controls autoplay>
          <source src={audioUrl} type="audio/mpeg" />
          Tu navegador no admite la reproducción de audio.
        </audio>
      </div>
      {/if}
      
    </div>
    <h3 class="text-xl font-thin text-gray-900 dark:text-white">
      {nombreaudio}
    </h3>
</div>
