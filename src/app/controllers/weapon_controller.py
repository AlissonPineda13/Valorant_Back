from flask import Blueprint, jsonify, request
from app.models.weapon import Weapon
from app.extensions import db
from app.services.weapon_service import *

weapon_bp = Blueprint("weapon_bp", __name__, url_prefix="/weapons")


@weapon_bp.route('', methods=['GET'])
def get_weapons_route():
    """
    Get weapons with optional filters
    ---
    tags:
      - Weapons
    parameters:
      - in: query
        name: name
        type: string
        required: false
      - in: query
        name: category
        type: string
        required: false
    responses:
      200:
        description: A list of weapons
    """

    name = request.args.get('name')
    category = request.args.get('category')

    weapons = get_weapons(name, category)
    # Convert each object to a dict and returns a Json
    return jsonify([a.to_dict() for a in weapons])


@weapon_bp.route('', methods=['POST'])
def post_weapon_route():
    """
    Post a new weapon
    ---
    tags:
      - Weapons
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
            - category
            - head_damage
            - body_damage
            - leg_damage
            - price
            - image
          properties:
            name:
              type: string
              example: Classic
            category:
              type: string
              example: Sidearms
            head_damage: 
              type:  number
              example: 78
            body_damage: 
              type:  number
              example: 26
            leg_damage:
              type:  number
              example: 22.1
            price:
              type:  number
              example: 0
            image:
              type: string
              example: test
    responses:
      201:
        description: Weapon created successfully
        schema:
          type: object
          properties:
            name:
              type: string
            category:
              type: string
            head_damage:
              type:  number
            body_damage:
              type:  number
            leg_damage:
              type:  number
            price:
              type:  number
            image:
              type: string
      400:
        description: Invalid input
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data"}), 400

    if 'name' not in data or 'category' not in data or 'head_damage' not in data or 'body_damage' not in data or 'leg_damage' not in data or 'price' not in data or 'image' not in data:
        return jsonify({"error": "All data is required"}), 400

    weapon = post_weapon(data)
    return jsonify(weapon.to_dict()), 201


@weapon_bp.route('/<int:id>', methods=['PUT'])
def update_weapon_route(id):
    """
    Update an weapon
    ---
    tags:
      - Weapons
    parameters:
      - in: path
        name: id
        type:  number
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - name
            - category
            - head_damage
            - body_damage
            - leg_damage
            - price
            - image
          properties:
            name:
              type: string
              example: Classic
            category:
              type: string
              example: Sidearms
            head_damage: 
              type:  number
              example: 78
            body_damage: 
              type:  number
              example: 26
            leg_damage:
              type:  number
              example: 22.1
            price:
              type:  number
              example: 0
            image:
              type: string
              example: test

    responses:
      200:
        description: Weapon updated successfully
      404:
        description: Weapon not found
    """
    weapon = get_weapon_by_id(id)

    if not weapon:
        return jsonify({"error": "Weapon not found"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"error": "No input data"}), 400

    weapon = update_weapon(weapon, data)

    return jsonify(weapon.to_dict()), 200


@weapon_bp.route('/<int:id>', methods=['DELETE'])
def delete_weapon_route(id):
    """
    Delete an weapon
    ---
    tags:
      - Weapons
    parameters:
      - in: path
        name: id
        type:  number
        required: true
    responses:
      200:
        description: Weapon deleted successfully
      404:
        description: Weapon not found
    """

    weapon = get_weapon_by_id(id)

    if not weapon:
        return jsonify({"error": "Weapon not found"}), 404

    weapon = delete_weapon(id)
    return jsonify({"message": "Weapon deleted successfully"}), 200
