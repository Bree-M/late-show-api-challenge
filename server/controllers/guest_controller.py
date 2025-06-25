from flask import Blueprint, jsonify
from models.guest import Guest
from models import db

guest_bp = Blueprint('guest_bp', __name__)

@guest_bp.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([guest.to_dict_basic() for guest in guests])