'''
class Agent:
    def __init__(self, id, name, description, role, image):
        self.id = id
        self.name = name
        self.description = description
        self.role = role
        self.image = image
'''

from app.extensions import db


class Agent(db.Model):
    __tablename__ = "agents"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), unique=True, nullable=False)
    description = db.Column(db.String(140), nullable=False)
    role = db.Column(db.String(45), nullable=False)
    image = db.Column(db.String(500), nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
