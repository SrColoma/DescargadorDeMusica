<script>
  import Aniadir from "$lib/aniadir/Aniadir.svelte";
  import ListaDescargados from "$lib/listadescargados/ListaDescargados.svelte";
  import ListaParaDescargar from "$lib/listaparadescargar/ListaParaDescargar.svelte";
  import "../app.css";
</script>

<div
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
</div>
