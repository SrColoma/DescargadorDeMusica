from flask import Blueprint
from flask_cors import CORS

bp = Blueprint('externos', __name__)
cors = CORS(bp,resources={r"/*": {"origins": "*", "headers":["Content-Type", "Authorization"]}})

from app.externos import descargar_audio
from app.externos import getVideoNombre
from app.externos import getDescargados
from app.externos import get_audio