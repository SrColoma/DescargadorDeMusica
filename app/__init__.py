from flask import Flask, send_file,send_from_directory
from flask_cors import CORS
import os

# from config import Config

def create_app():
    app = Flask("SrServer", static_folder='static')
    # app.config.from_object(config_class)

    CORS(app,resources={r"/*": {"origins": "*", "headers":["Content-Type", "Authorization"]}})
    

    from app.externos import bp as externos_bp
    app.register_blueprint(externos_bp, url_prefix='/externos')

    # --------------------------------------

    print('---------------ENDPOINTS------------------')
    for rule in app.url_map.iter_rules():
        print(str(rule))

    print('---------------/ENDPOINTS------------------')

    # --------------------------------------


    # Register error handlers here
    @app.errorhandler(404)
    def page_not_found(e):
        return '<h1>404</h1><p>El endpoint no existe o lo estas escribiendo mal</p>', 404
    
    @app.errorhandler(500)
    def internal_server_error(e):
        return '<h1>500</h1><p>error del servidor culpa a alfred</p>', 500
    
    # --------------------------------------
    # test page
    @app.route('/test/')
    def test_page():
        return '<h1>TEST</h1>'

    return app