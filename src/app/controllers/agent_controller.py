from flask import Blueprint, jsonify, request
from app.models.agent import Agent
from app.extensions import db
from app.services.agent_service import *

agent_bp = Blueprint("agent_bp", __name__, url_prefix="/agents")


@agent_bp.route('', methods=['GET'])
def get_agents_route():
    """
    Get agents with optional filters
    ---
    tags:
      - Agents
    parameters:
      - in: query
        name: name
        type: string
        required: false
      - in: query
        name: role
        type: string
        required: false
    responses:
      200:
        description: A list of agents
    """

    name = request.args.get('name')
    role = request.args.get('role')

    agents = get_agents(name, role)
    # Convert each object to a dict and returns a Json
    return jsonify([a.to_dict() for a in agents])


@agent_bp.route('', methods=['POST'])
def post_agent_route():
    """
    Post a new agents
    ---
    tags:
      - Agents
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - name
            - role
          properties:
            name:
              type: string
              example: Jett
            role:
              type: string
              example: Duelist
            description:
              type: string
              example: A fefeosjgosdg...
            image:
              type: string
              example: test
    responses:
      201:
        description: Agent created successfully
        schema:
          type: object
          properties:
            name:
              type: string
            role:
              type: string
            description:
              type: string
            image:
              type: string
      400:
        description: Invalid input
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data"}), 400

    if 'name' not in data or 'role' not in data:
        return jsonify({"error": "name and role are required"}), 400

    agent = post_agent(data)
    return jsonify(agent.to_dict()), 201


@agent_bp.route('/<int:id>', methods=['PUT'])
def update_agent_route(id):
    """
    Update an agent
    ---
    tags:
      - Agents
    parameters:
      - in: path
        name: id
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - name
            - role
            - description
            - image
          properties:
            name:
              type: string
              example: Jett
            role:
              type: string
              example: Duelist
            description:
              type: string
              example: A fefeosjgosdg...
            image:
              type: string
              example: test

    responses:
      200:
        description: Agent updated successfully
      404:
        description: Agent not found
    """
    agent = get_agent_by_id(id)

    if not agent:
        return jsonify({"error": "Agent not found"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"error": "No input data"}), 400

    agent = update_agent(agent, data)

    return jsonify(agent.to_dict()), 200


@agent_bp.route('/<int:id>', methods=['DELETE'])
def delete_agent_route(id):
    """
    Delete an agent
    ---
    tags:
      - Agents
    parameters:
      - in: path
        name: id
        type: integer
        required: true
    responses:
      200:
        description: Agent deleted successfully
      404:
        description: Agent not found
    """

    agent = get_agent_by_id(id)

    if not agent:
        return jsonify({"error": "Agent not found"}), 404

    agent = delete_agent(id)
    return jsonify({"message": "Agent deleted successfully"}), 200
