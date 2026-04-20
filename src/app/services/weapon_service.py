from app.extensions import db
from app.models.weapon import Weapon


def get_weapons(name=None, category=None):
    query = Weapon.query

    if name:
        query = query.filter(Weapon.name.ilike(f"%{name}%"))

    if category:
        query = query.filter(Weapon.category.ilike(f"%{category}%"))

    # weapons = query.all()  # executes the query with the filters defined before

    # Convert each object to a dict and returns a Json
    # return jsonify([a.to_dict() for a in weapons])

    return query.all()


def post_weapon(data):
    weapon = Weapon(
        name=data['name'],
        category=data['category'],
        head_damage=data['head_damage'],
        body_damage=data['body_damage'],
        leg_damage=data['leg_damage'],
        price=data['price'],
        image=data['image']
    )

    db.session.add(weapon)
    db.session.commit()

    # return jsonify(weapon.to_dict()), 201
    return weapon


def get_weapon_by_id(id):
    return Weapon.query.get(id)


def update_weapon(weapon, data):

    if 'name' in data:
        weapon.name = data['name']
    if 'category' in data:
        weapon.category = data['category']
    if 'head_damage' in data:
        weapon.head_damage = data['head_damage']
    if 'body_damage' in data:
        weapon.body_damage = data['body_damage']
    if 'leg_damage' in data:
        weapon.leg_damage = data['leg_damage']
    if 'price' in data:
        weapon.price = data['price']
    if 'image' in data:
        weapon.image = data['image']

    db.session.commit()

    return weapon


def delete_weapon(id):
    weapon = Weapon.query.get(id)

    db.session.delete(weapon)
    db.session.commit()
