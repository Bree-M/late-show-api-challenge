from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from models.appearance import Appearance
from models import db

appearance_bp = Blueprint('appearance_bp', __name__)

@appearance_bp.route('/appearances', methods=['GET'])
def get_appearances():
    appearances = Appearance.query.all()
    return jsonify([appearance.to_dict_basic() for appearance in appearances])

@appearance_bp.route('/appearances', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    rating = data.get('rating')
    episode_id = data.get('episode_id')
    guest_id = data.get('guest_id')
    errors = []
    if rating is None or not isinstance(rating, int):
        errors.append('Rating is required and must be an integer.')
    if not episode_id or not isinstance(episode_id, int):
        errors.append('Valid episode_id is required.')
    if not guest_id or not isinstance(guest_id, int):
        errors.append('Valid guest_id is required.')
    if errors:
        return jsonify({'errors': errors}), 400
    new_appearance = Appearance(rating=rating, guest_id=guest_id, episode_id=episode_id)
    db.session.add(new_appearance)
    db.session.commit()
    return jsonify(new_appearance.to_dict_basic()), 201