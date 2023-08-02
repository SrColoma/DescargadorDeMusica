from flask import Flask, send_file
from app.externos import bp

@bp.route('/audio/<filename>', methods=['GET'])
def get_audio(filename):
    audio_directory = 'descargas'
    audio_file_path = f'{audio_directory}/{filename}'
    
    return send_file(audio_file_path, mimetype='audio/mpeg')
