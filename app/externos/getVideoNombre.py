import threading
import time
from flask import request, jsonify
from pytube import YouTube
import os
import string
import unicodedata
from app.externos import bp

# {
#   "url": "https://youtu.be/fx9VygrLek4?list=RDMMfx9VygrLek4"
# }

@bp.route('/getVideoNombre', methods=['POST'])
def getVideoNombre():
    # Obtener la lista de videos del JSON enviado
    data = request.get_json()
    url = data['url']

    yt = YouTube(url)
    video_title = yt.title
    video_duration = yt.length
    video_miniatura_url =yt.thumbnail_url

    # Eliminar caracteres no permitidos del título del video
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    video_title = ''.join(c for c in video_title if c in valid_chars)
    video_title = unicodedata.normalize('NFKD', video_title).encode('ASCII', 'ignore').decode('utf-8')

    return jsonify({'nombre': video_title, 'duracion': video_duration, 'miniatura': video_miniatura_url, 'url': url})