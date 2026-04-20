'''
class Weapon:
    def __init__(self, id, name, category, head_damage, body_damage, leg_damage, price, image):
        self.id = id
        self.name = name
        self.type = category
        self.head_damage = head_damage
        self.body_damage = body_damage
        self.leg_damage = leg_damage
        self.price = price
        self.image = image
'''

from app.extensions import db


class Weapon(db.Model):
    __tablename__ = "weapons"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), unique=True, nullable=False)
    category = db.Column(db.String(45), nullable=False)
    head_damage = db.Column(db.Integer, nullable=False)
    body_damage = db.Column(db.Integer, nullable=False)
    leg_damage = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(500), nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
