from flask import Blueprint
from flask_restx import Api

from .routes import ns

api_bp = Blueprint('api', __name__)

api = Api(
    api_bp,
    version='0.1.4',
    title='Flaskeleton ToDo API',
    description='Flaskeleton ToDo API',
    doc='/apidoc',
)


def init_app(app):
    api.add_namespace(ns)
    app.register_blueprint(api_bp)
