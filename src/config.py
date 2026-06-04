import os


class Config:
    # SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
<<<<<<< HEAD
        "mysql+pymysql://root:fFHojsfqbaBOwoPkgABElHDqgkFcLPiY@shuttle.proxy.rlwy.net:27918/schema_valorant"
=======
        "mysql+pymysql://root:admin@localhost:3306/schema_valorant"
>>>>>>> main
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
