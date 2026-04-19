from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

# pip install flask flask-sqlalchemy pymysql - Package to connect(config) DB
