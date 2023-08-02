<script>
  import ReproductorComp from "$lib/Reproductor/ReproductorComp.svelte";
  import Aniadir from "$lib/aniadir/Aniadir.svelte";
  import ListaDescargados from "$lib/listadescargados/ListaDescargados.svelte";
  import ListaParaDescargar from "$lib/listaparadescargar/ListaParaDescargar.svelte";
  import "../app.css";

  let currentSong = 'cancion1.mp3';
</script>


<div class="grid grid-cols-2 gap-2  m-4">
  <div class="justify-self-end overflow-y-auto max-h-screen -" >
    <ListaDescargados />
  </div>
  <div class="justify-self-start">
    <div class="flex flex-col gap-2">
      <Aniadir />
      <ListaParaDescargar />

    </div>
  </div>
</div>
<div class="sticky bottom-0">
  <ReproductorComp/>

</div>


<!-- <div
  class="grid grid-cols-2 grid-rows-2 gap-2 "
>
  <div class="row-span-2 h-max">
    <div class="flex justify-end">
        <ListaDescargados/>

    </div>
  </div>
  <div>
    <Aniadir />
  </div>
  <div class="col-start-2 row-start-2">
    <ListaParaDescargar />
  </div>
</div> -->
