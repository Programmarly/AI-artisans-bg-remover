from flask import Flask, jsonify, request
from backend.routes import init_routes
from flask_cors import CORS
from flask_talisman import Talisman
def create_app():
    app = Flask(__name__)
    CORS(app)
    # Talisman(app)
    app.config.from_object('backend.config.Config')
    
    # Initialize routes
    init_routes(app)

    return app
