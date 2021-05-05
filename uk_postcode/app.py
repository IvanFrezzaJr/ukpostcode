from flask import Flask
from uk_postcode.blueprints import restapi

def create_app():
    app = Flask(__name__)
    restapi.init_app(app)
    return app

