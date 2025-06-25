from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required  # ✅ Import added
from models.episode import Episode
from models import db

episode_bp = Blueprint('episode_bp', __name__)

@episode_bp.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([episode.to_dict_basic() for episode in episodes])

@episode_bp.route('/episodes/<int:id>', methods=['GET'])
def get_episode_by_id(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({'error': 'Episode not found'}), 404
    
    appearances = [a.to_dict_basic() for a in episode.appearances]
    episode_data = episode.to_dict_basic()
    episode_data['appearances'] = appearances
    
    return jsonify(episode_data)

@episode_bp.route('/episodes/<int:id>', methods=['DELETE'])
@jwt_required()  # ✅ REQUIRED by spec
def delete_episode(id):
    episode = Episode.query.get(id)
    if not episode:
        return jsonify({'error': 'Episode not found'}), 404

    db.session.delete(episode)
    db.session.commit()
    
    return jsonify({'message': 'Episode deleted successfully'}), 200
