from flask import Flask
from werkzeug.exceptions import HTTPException

from .blueprints import web
from .extensions import database, session, settings
from .functions import error_handler


def create_app():
    app = Flask(__name__)
    settings.init_app(app)

    session.init_app(app)
    database.init_app(app)

    # Register error handler
    app.register_error_handler(HTTPException, error_handler)

    # Register blueprints
    web.init_app(app)

    return app


app = create_app()
