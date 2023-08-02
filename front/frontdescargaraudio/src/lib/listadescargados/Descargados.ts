import { writable } from "svelte/store";


function ListaDescargados() {
  const { subscribe, set, update } = writable<string[]>([]);

  async function searchDescargados() {
    try {
        fetch("http://127.0.0.1:5000/externos/getDescargados")
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          let apiData = data["list"];
          set(apiData);
        })
        .catch((error) => {
          console.log(error);
          return [];
        });
    } catch (error) {
      console.error("Error al añadir el video:", error);
    }
  }

  return {
    searchDescargados,
    subscribe,
    set,
    update,
  };
}

export const Descargados = ListaDescargados();
