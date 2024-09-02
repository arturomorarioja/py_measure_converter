"""
Measure converter API

Author: Arturo Mora-Rioja
Date: September 2024
"""
import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_prefixed_env()

    from . import converter
    app.register_blueprint(converter.bp)

    print(f'Current environment: {os.getenv("ENVIRONMENT")}')
    print(f'Using database: {app.config.get("DATABASE")}')

    return app