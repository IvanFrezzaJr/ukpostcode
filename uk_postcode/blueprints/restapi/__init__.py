from flask import Blueprint

from .resources import IndexResource, CodeResource

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")

def init_app(app):
    app.register_blueprint(bp)
    app.add_url_rule('/', 'index', IndexResource)
    app.add_url_rule('/postcode/<string:code>', 'postcode', CodeResource)