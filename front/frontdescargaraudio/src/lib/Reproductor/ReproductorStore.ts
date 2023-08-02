import { writable } from "svelte/store";

interface Reproductor {
  changeAndPlay: (url: string) => void;
  audioPlayer: HTMLAudioElement | null;
  subscribe: any;
  set: any;
  update: any;
}

function reproductor(): Reproductor {
  const { subscribe, set, update } = writable("");
  let audioPlayer: HTMLAudioElement | null = null;

  return {
    changeAndPlay: (url: string) => {
      if (!audioPlayer) {
        audioPlayer = new Audio();
      }

      if (audioPlayer) {
        audioPlayer.pause();
        audioPlayer.src = url;
        audioPlayer.load();
        audioPlayer.play();
      }
    },
    audioPlayer,
    subscribe,
    set,
    update,
  };
}

export const reproductorStore = reproductor();
