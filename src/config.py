import os


class Config:
    # SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://root:admin@localhost:3306/schema_valorant"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
