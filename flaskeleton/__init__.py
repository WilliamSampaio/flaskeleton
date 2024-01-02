from flask import Flask, render_template
from werkzeug.exceptions import HTTPException

from .extensions import database, session, settings


def error_handler(e):
    data = {}
    desc = e.description
    msg = desc['message'] if 'message' in desc else desc
    data['message'] = f'Error({e.code} - {e.name}): {msg}'
    return (
        render_template('error.html', data=data),
        e.code,
    )


def create_app():
    app = Flask(__name__)
    settings.init_app(app)

    session.init_app(app)
    database.init_app(app)

    app.register_error_handler(HTTPException, error_handler)

    @app.route('/')
    def index():
        return 'Hello World!'

    return app


app = create_app()
