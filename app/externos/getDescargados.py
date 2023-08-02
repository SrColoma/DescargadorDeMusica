import threading
import time
from flask import request, jsonify
from pytube import YouTube
import os
import string
import unicodedata
from app.externos import bp


@bp.route('/getDescargados', methods=['GET'])
def getDescargados():
    
    carpeta_descargas = 'descargas'  # Ruta a la carpeta descargas

    if not os.path.exists(carpeta_descargas):
        return jsonify({"error": "La carpeta de descargas no existe"})

    nombres_archivos = os.listdir(carpeta_descargas)
    return jsonify({"list": nombres_archivos})