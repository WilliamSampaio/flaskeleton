from flask import Blueprint

api = Blueprint('api', __name__)


@api.route('/')
def index():
    return {'blueprint': 'API'}, 200


def init_app(app):
    app.register_blueprint(api, url_prefix='/api')
