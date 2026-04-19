from app.extensions import db
from app.models.agent import Agent


def get_agents(name=None, role=None):
    query = Agent.query

    if name:
        query = query.filter(Agent.name.ilike(f"%{name}%"))

    if role:
        query = query.filter(Agent.role.ilike(f"%{role}%"))

    # agents = query.all()  # executes the query with the filters defined before

    # Convert each object to a dict and returns a Json
    # return jsonify([a.to_dict() for a in agents])

    return query.all()


def post_agent(data):
    agent = Agent(
        name=data['name'],
        role=data['role'],
        description=data['description'],
        image=data['image']
    )

    db.session.add(agent)
    db.session.commit()

    # return jsonify(agent.to_dict()), 201
    return agent


def get_agent_by_id(id):
    return Agent.query.get(id)


def update_agent(agent, data):

    if 'name' in data:
        agent.name = data['name']
    if 'role' in data:
        agent.role = data['role']
    if 'description' in data:
        agent.description = data['description']
    if 'image' in data:
        agent.image = data['image']

    db.session.commit()

    return agent


def delete_agent(id):
    agent = Agent.query.get(id)

    db.session.delete(agent)
    db.session.commit()
