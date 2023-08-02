import threading
import time
from flask import request, jsonify
from pytube import YouTube
import os
import string
import unicodedata
from app.externos import bp

# {
#   "videos": [
#     {
#       "url": "https://www.youtube.com/watch?v=VIDEO_ID1"
#     },
#     {
#       "url": "https://www.youtube.com/watch?v=VIDEO_ID2"
#     },
#     ...
#   ]
# }


@bp.route('/descargar_audio', methods=['POST'])
def descargar_audio():
    try:
        # Obtener la lista de videos del JSON enviado
        data = request.get_json()
        videos = data['videos']

        # Crear el directorio para almacenar los audios descargados
        directorio_descarga = 'descargas'
        if not os.path.exists(directorio_descarga):
            os.makedirs(directorio_descarga)

        # Función para descargar el audio de un video
        def descargar_video(video):

            url = video['url']
            yt = YouTube(url)
            video_title = yt.title

            # Eliminar caracteres no permitidos del título del video
            valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
            video_title = ''.join(c for c in video_title if c in valid_chars)
            video_title = unicodedata.normalize('NFKD', video_title).encode('ASCII', 'ignore').decode('utf-8')

            audio_stream = yt.streams.filter(only_audio=True).first()
            audio_stream.download(output_path=directorio_descarga, filename=video_title + '.mp3')

        # Lista para almacenar los hilos
        threads = []

        # Descargar el audio de cada video en un hilo separado
        for video in videos:
            t = threading.Thread(target=descargar_video, args=(video,))
            threads.append(t)
            t.start()

        # Esperar a que todos los hilos terminen
        for t in threads:
            t.join()

        return jsonify({'message': 'Descarga completada'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# @bp.route('/descargar_audio', methods=['POST'])
# def descargar_audio():
#     try:
#         # Obtener la lista de videos del JSON enviado
#         data = request.get_json()
#         videos = data['videos']

#         # Crear el directorio para almacenar los audios descargados
#         directorio_descarga = 'descargas'
#         if not os.path.exists(directorio_descarga):
#             os.makedirs(directorio_descarga)

#         # Descargar el audio de cada video
#         for video in videos:
#             url = video['url']
#             yt = YouTube(url)
#             video_title = yt.title
#             audio_stream = yt.streams.filter(only_audio=True).first()
#             audio_stream.download(output_path=directorio_descarga, filename=video_title + '.mp3')

#         return jsonify({'message': 'Descarga completada'})

#     except Exception as e:
#         return jsonify({'error': str(e)}), 500
