import { Descargados } from "$lib/listadescargados/Descargados";
import { writable } from "svelte/store";
// import {Descargados} 

type VideoData = {
  duracion: number;
  miniatura: string;
  nombre: string;
  url: string;
};

function ADescargar() {
  const { subscribe, set, update } = writable<VideoData[]>([]);
  let descargados: string[] = [];
  let aDescargar: VideoData[] = [];

  subscribe((value) => {
    aDescargar = value;
  });

  Descargados.subscribe((value) => {
    descargados = value;
  });

  async function addvideo(videoURL: string) {
    try {
      
      const response = await fetch(
        "http://127.0.0.1:5000/externos/getVideoNombre",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            url: videoURL,
          }),
        }
      );
      
      const data = await response.json(); // Esperar a que se resuelva la promesa JSON

      if (descargados.includes(data.nombre + ".mp3") || aDescargar.map((e) => e.nombre).includes(data.nombre)) {
        return;
      }else{
        update((n: VideoData[]) => [...n, data]);

      }

    } catch (error) {
      console.error("Error al añadir el video:", error);
    }
  }

  async function descargarvideos() {

    // # {
    //   #   "videos": [
    //   #     {
    //   #       "url": "https://www.youtube.com/watch?v=VIDEO_ID1"
    //   #     },
    //   #     {
    //   #       "url": "https://www.youtube.com/watch?v=VIDEO_ID2"
    //   #     },
    //   #     ...
    //   #   ]
    //   # }
    const response = await fetch(
      "http://127.0.0.1:5000/externos/descargar_audio",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          videos: aDescargar.map((e) => {
            return { url: e.url };
          }),
        }),
      }
    );
    console.log("Descargando videos...");
    const data = await response.json(); // Esperar a que se resuelva la promesa JSON
    console.log("Videos descargados");
    console.log(data);
  }

  return {
    descargarvideos,
    addvideo,
    subscribe,
    set,
    update,
  };
}

export const ADescargarStore = ADescargar();
