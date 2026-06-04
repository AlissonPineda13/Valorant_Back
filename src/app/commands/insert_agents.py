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
            "description": "A strategic Controller who deploys orbital smokes, incendiary grenades, and team-wide combat support.",
            "role": "Controller",
            "image": "brimstone.webp"
        },
        {
            "name": "Phoenix",
            "description": "A self-sufficient Duelist who manipulates fire to heal himself and aggressively take fights.",
            "role": "Duelist",
            "image": "phoenix.webp"
        },
        {
            "name": "Sage",
            "description": "A defensive Sentinel capable of healing allies, creating barriers, and resurrecting teammates.",
            "role": "Sentinel",
            "image": "sage.webp"
        },
        {
            "name": "Sova",
            "description": "An Initiator who gathers intelligence and reveals enemy positions with advanced reconnaissance tools.",
            "role": "Initiator",
            "image": "sova.webp"
        },
        {
            "name": "Viper",
            "description": "A Controller who dominates areas using toxic screens, poison clouds, and chemical warfare.",
            "role": "Controller",
            "image": "viper.webp"
        },
        {
            "name": "Cypher",
            "description": "A surveillance-focused Sentinel who secures sites with traps, cameras, and information gathering.",
            "role": "Sentinel",
            "image": "cypher.webp"
        },
        {
            "name": "Reyna",
            "description": "A snowballing Duelist who thrives on eliminations to heal, dismiss, and empower herself.",
            "role": "Duelist",
            "image": "reyna.webp"
        },
        {
            "name": "Killjoy",
            "description": "A technology expert Sentinel who locks down areas using turrets, alarms, and nanoswarms.",
            "role": "Sentinel",
            "image": "killjoy.webp"
        },
        {
            "name": "Breach",
            "description": "An Initiator who disrupts enemies through walls with powerful concussive and crowd-control abilities.",
            "role": "Initiator",
            "image": "breach.webp"
        },
        {
            "name": "Omen",
            "description": "A mysterious Controller who manipulates shadows to teleport, blind opponents, and block vision.",
            "role": "Controller",
            "image": "omen.webp"
        },
        {
            "name": "Jett",
            "description": "A highly mobile Duelist who excels at quick engagements, evasive movement, and precise eliminations.",
            "role": "Duelist",
            "image": "jett.webp"
        },
        {
            "name": "Raze",
            "description": "An explosive Duelist who overwhelms enemies with grenades, rockets, and destructive firepower.",
            "role": "Duelist",
            "image": "raze.webp"
        },
        {
            "name": "Skye",
            "description": "An Initiator who supports teammates with healing, scouting creatures, and area control.",
            "role": "Initiator",
            "image": "skye.webp"
        },
        {
            "name": "Yoru",
            "description": "A deceptive Duelist who uses teleportation, fakeouts, and dimensional abilities to outplay opponents.",
            "role": "Duelist",
            "image": "yoru.webp"
        },
        {
            "name": "Astra",
            "description": "A cosmic Controller who shapes the battlefield with stars, gravity wells, and powerful utility.",
            "role": "Controller",
            "image": "astra.webp"
        },
        {
            "name": "KAY/O",
            "description": "A machine Initiator designed to suppress enemy abilities and create openings for his team.",
            "role": "Initiator",
            "image": "kayo.webp"
        },
        {
            "name": "Chamber",
            "description": "A precision-focused Sentinel who combines deadly firearms with tactical defensive tools.",
            "role": "Sentinel",
            "image": "chamber.webp"
        },
        {
            "name": "Neon",
            "description": "An electrifying Duelist who uses unmatched speed and energy-powered abilities to pressure enemies.",
            "role": "Duelist",
            "image": "neon.webp"
        },
        {
            "name": "Fade",
            "description": "An Initiator who hunts opponents through fear, revealing and tracking enemies across the map.",
            "role": "Initiator",
            "image": "fade.webp"
        },
        {
            "name": "Harbor",
            "description": "A Controller who commands water-based abilities to shield allies and reshape sightlines.",
            "role": "Controller",
            "image": "harbor.webp"
        },
        {
            "name": "Gekko",
            "description": "An Initiator who fights alongside a team of unique creatures that scout, stun, and disrupt enemies.",
            "role": "Initiator",
            "image": "gekko.webp"
        },
        {
            "name": "Deadlock",
            "description": "A Sentinel who uses advanced nanowire technology to trap, isolate, and stop enemy advances.",
            "role": "Sentinel",
            "image": "deadlock.webp"
        },
        {
            "name": "Iso",
            "description": "A Duelist who specializes in isolated engagements, shielding himself and forcing direct confrontations.",
            "role": "Duelist",
            "image": "iso.webp"
        },
        {
            "name": "Clove",
            "description": "A Controller who bends the rules of life and death, remaining impactful even after being eliminated.",
            "role": "Controller",
            "image": "clove.webp"
        },
        {
            "name": "Vyse",
            "description": "A Sentinel who manipulates liquid metal to trap enemies, control space, and punish aggressive pushes.",
            "role": "Sentinel",
            "image": "vyse.webp"
        },
        {
            "name": "Tejo",
            "description": "A tactical Initiator who uses guided missiles and advanced military technology to reveal and pressure opponents.",
            "role": "Initiator",
            "image": "tejo.webp"
        },
        {
            "name": "Waylay",
            "description": "A fast-paced Duelist who bends light to overwhelm enemies with speed, mobility, and aggressive engagements.",
            "role": "Duelist",
            "image": "waylay.webp"
        }
    ]

    for data in agents:
        exists = Agent.query.filter_by(name=data["name"]).first()
        if not exists:
            db.session.add(Agent(**data))

    db.session.commit()

    click.echo("Agents inserted properly")
