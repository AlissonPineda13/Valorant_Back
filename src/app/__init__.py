import os

from flask import Flask
from flask.cli import load_dotenv
from flask_cors import CORS
from config import Config
from app.extensions import db, migrate
from flasgger import Swagger
from .controllers.agent_controller import *
from .controllers.weapon_controller import *
from .commands.insert_agents import *
from .commands.insert_weapons import *


def create_app():
    app = Flask(__name__,static_folder="static")
    CORS(app)
    app.config.from_object(Config)
    # Configure apikey to be used on put, post, delete requests
    load_dotenv()

    db.init_app(app)
    migrate.init_app(app, db)

    # Registering blueprint

    app.register_blueprint(agent_bp)
    app.register_blueprint(weapon_bp)

    # Swagger config
    swagger = Swagger(app)

    app.cli.add_command(insert_agents)
    app.cli.add_command(insert_weapons)

    return app
