import click
from flask.cli import with_appcontext
from app.extensions import db
from app.models.agent import Agent


@click.command("insert_agents")
@with_appcontext
def insert_agents():
    agents = [
        {
            "name": "Brimstone",
            "description": "Controls the battlefield with orbital smokes and tactical abilities.",
            "role": "Controller",
            "image": "https://media.valorant-api.com/agents/brimstone.png"
        },
        {
            "name": "Phoenix",
            "description": "A duelist with fire-based abilities who can heal himself.",
            "role": "Duelist",
            "image": "https://media.valorant-api.com/agents/phoenix.png"
        },
        {
            "name": "Sage",
            "description": "A support agent capable of healing and reviving allies.",
            "role": "Sentinel",
            "image": "https://media.valorant-api.com/agents/sage.png"
        },
        {
            "name": "Sova",
            "description": "A scout who tracks enemies using reconnaissance arrows.",
            "role": "Initiator",
            "image": "https://media.valorant-api.com/agents/sova.png"
        },
        {
            "name": "Viper",
            "description": "Controls areas using poison and toxic gas.",
            "role": "Controller",
            "image": "https://media.valorant-api.com/agents/viper.png"
        },
        {
            "name": "Cypher",
            "description": "Monitors areas using traps and surveillance cameras.",
            "role": "Sentinel",
            "image": "https://media.valorant-api.com/agents/cypher.png"
        },
        {
            "name": "Reyna",
            "description": "A duelist who grows stronger by eliminating enemies.",
            "role": "Duelist",
            "image": "https://media.valorant-api.com/agents/reyna.png"
        },
        {
            "name": "Killjoy",
            "description": "Defends areas using turrets and advanced gadgets.",
            "role": "Sentinel",
            "image": "https://media.valorant-api.com/agents/killjoy.png"
        },
        {
            "name": "Breach",
            "description": "Initiates attacks with abilities that go through walls.",
            "role": "Initiator",
            "image": "https://media.valorant-api.com/agents/breach.png"
        },
        {
            "name": "Omen",
            "description": "Moves through shadows and blocks vision.",
            "role": "Controller",
            "image": "https://media.valorant-api.com/agents/omen.png"
        },
        {
            "name": "Jett",
            "description": "High mobility and deadly precision.",
            "role": "Duelist",
            "image": "https://media.valorant-api.com/agents/jett.png"
        },
        {
            "name": "Raze",
            "description": "An explosive expert.",
            "role": "Duelist",
            "image": "https://media.valorant-api.com/agents/raze.png"
        },
        {
            "name": "Skye",
            "description": "Supports the team with healing and tracking abilities.",
            "role": "Initiator",
            "image": "https://media.valorant-api.com/agents/skye.png"
        },
        {
            "name": "Yoru",
            "description": "Deceives enemies using teleportation and tricks.",
            "role": "Duelist",
            "image": "https://media.valorant-api.com/agents/yoru.png"
        },
        {
            "name": "Astra",
            "description": "Controls the map using cosmic energy.",
            "role": "Controller",
            "image": "https://media.valorant-api.com/agents/astra.png"
        },
        {
            "name": "KAY/O",
            "description": "Suppresses enemy abilities.",
            "role": "Initiator",
            "image": "https://media.valorant-api.com/agents/kayo.png"
        },
        {
            "name": "Chamber",
            "description": "A sharpshooter with defensive gadgets.",
            "role": "Sentinel",
            "image": "https://media.valorant-api.com/agents/chamber.png"
        },
        {
            "name": "Neon",
            "description": "Extreme speed and electric-based attacks.",
            "role": "Duelist",
            "image": "https://media.valorant-api.com/agents/neon.png"
        },
        {
            "name": "Fade",
            "description": "Reveals enemies using fear-based abilities.",
            "role": "Initiator",
            "image": "https://media.valorant-api.com/agents/fade.png"
        },
        {
            "name": "Harbor",
            "description": "Controls water to block vision and protect areas.",
            "role": "Controller",
            "image": "https://media.valorant-api.com/agents/harbor.png"
        },
        {
            "name": "Gekko",
            "description": "Summons creatures to attack and control areas.",
            "role": "Initiator",
            "image": "https://media.valorant-api.com/agents/gekko.png"
        },
        {
            "name": "Deadlock",
            "description": "Controls areas with advanced trapping technology.",
            "role": "Sentinel",
            "image": "https://media.valorant-api.com/agents/deadlock.png"
        },
        {
            "name": "Iso",
            "description": "A duelist focused on isolated one-on-one fights.",
            "role": "Duelist",
            "image": "https://media.valorant-api.com/agents/iso.png"
        },
        {
            "name": "Clove",
            "description": "A controller with death-related abilities.",
            "role": "Controller",
            "image": "https://media.valorant-api.com/agents/clove.png"
        }
    ]

    for data in agents:
        exists = Agent.query.filter_by(name=data["name"]).first()
        if not exists:
            db.session.add(Agent(**data))

    db.session.commit()

    click.echo("Agents inserted properly")
