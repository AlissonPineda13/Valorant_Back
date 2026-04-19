from flask import Flask
from config import Config
from app.extensions import db, migrate
from flasgger import Swagger
from .controllers.agent_controller import *


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar blueprint

    app.register_blueprint(agent_bp)

    # Swagger config
    swagger = Swagger(app)

    return app
