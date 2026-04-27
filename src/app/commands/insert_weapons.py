import click
from flask.cli import with_appcontext
from app.models.weapon import Weapon
from app.extensions import db


@click.command("insert_weapons")
@with_appcontext
def insert_weapons():
    weapons = [
        # SIDEARMS
        {
            "name": "Classic",
            "category": "Sidearm",
            "head_damage": 78,
            "body_damage": 26,
            "leg_damage": 22,
            "price": 0,
            "image": "https://media.valorant-api.com/weapons/classic.png"
        },
        {
            "name": "Shorty",
            "category": "Sidearm",
            "head_damage": 36,
            "body_damage": 12,
            "leg_damage": 10,
            "price": 150,
            "image": "https://media.valorant-api.com/weapons/shorty.png"
        },
        {
            "name": "Frenzy",
            "category": "Sidearm",
            "head_damage": 78,
            "body_damage": 26,
            "leg_damage": 22,
            "price": 450,
            "image": "https://media.valorant-api.com/weapons/frenzy.png"
        },
        {
            "name": "Ghost",
            "category": "Sidearm",
            "head_damage": 105,
            "body_damage": 30,
            "leg_damage": 25,
            "price": 500,
            "image": "https://media.valorant-api.com/weapons/ghost.png"
        },
        {
            "name": "Sheriff",
            "category": "Sidearm",
            "head_damage": 160,
            "body_damage": 55,
            "leg_damage": 47,
            "price": 800,
            "image": "https://media.valorant-api.com/weapons/sheriff.png"
        },

        # SMGS
        {
            "name": "Stinger",
            "category": "SMG",
            "head_damage": 67,
            "body_damage": 27,
            "leg_damage": 23,
            "price": 1100,
            "image": "https://media.valorant-api.com/weapons/stinger.png"
        },
        {
            "name": "Spectre",
            "category": "SMG",
            "head_damage": 78,
            "body_damage": 26,
            "leg_damage": 22,
            "price": 1600,
            "image": "https://media.valorant-api.com/weapons/spectre.png"
        },

        # SHOTGUNS
        {
            "name": "Bucky",
            "category": "Shotgun",
            "head_damage": 40,
            "body_damage": 20,
            "leg_damage": 17,
            "price": 850,
            "image": "https://media.valorant-api.com/weapons/bucky.png"
        },
        {
            "name": "Judge",
            "category": "Shotgun",
            "head_damage": 34,
            "body_damage": 17,
            "leg_damage": 14,
            "price": 1850,
            "image": "https://media.valorant-api.com/weapons/judge.png"
        },

        # RIFLES
        {
            "name": "Bulldog",
            "category": "Rifle",
            "head_damage": 115,
            "body_damage": 35,
            "leg_damage": 29,
            "price": 2050,
            "image": "https://media.valorant-api.com/weapons/bulldog.png"
        },
        {
            "name": "Guardian",
            "category": "Rifle",
            "head_damage": 195,
            "body_damage": 65,
            "leg_damage": 49,
            "price": 2250,
            "image": "https://media.valorant-api.com/weapons/guardian.png"
        },
        {
            "name": "Phantom",
            "category": "Rifle",
            "head_damage": 156,
            "body_damage": 39,
            "leg_damage": 33,
            "price": 2900,
            "image": "https://media.valorant-api.com/weapons/phantom.png"
        },
        {
            "name": "Vandal",
            "category": "Rifle",
            "head_damage": 160,
            "body_damage": 40,
            "leg_damage": 34,
            "price": 2900,
            "image": "https://media.valorant-api.com/weapons/vandal.png"
        },

        # SNIPERS
        {
            "name": "Marshal",
            "category": "Sniper",
            "head_damage": 202,
            "body_damage": 101,
            "leg_damage": 85,
            "price": 950,
            "image": "https://media.valorant-api.com/weapons/marshal.png"
        },
        {
            "name": "Operator",
            "category": "Sniper",
            "head_damage": 255,
            "body_damage": 150,
            "leg_damage": 127,
            "price": 4700,
            "image": "https://media.valorant-api.com/weapons/operator.png"
        },

        # HEAVY
        {
            "name": "Ares",
            "category": "Heavy",
            "head_damage": 72,
            "body_damage": 30,
            "leg_damage": 25,
            "price": 1600,
            "image": "https://media.valorant-api.com/weapons/ares.png"
        },
        {
            "name": "Odin",
            "category": "Heavy",
            "head_damage": 95,
            "body_damage": 38,
            "leg_damage": 32,
            "price": 3200,
            "image": "https://media.valorant-api.com/weapons/odin.png"
        }
    ]

    for data in weapons:
        exists = Weapon.query.filter_by(name=data["name"]).first()
        if not exists:
            db.session.add(Weapon(**data))  # geting ready

    db.session.commit()  # saving data

    click.echo("Weapons inserted properly")
