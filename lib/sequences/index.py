from flask import Blueprint, jsonify
from lib.sequences.collatz import collatz_bp
sequences_bp = Blueprint('sequences', __name__, url_prefix='/sequences')
sequences_bp.register_blueprint(collatz_bp)

@sequences_bp.route('/', methods=['GET'])
def sequences():
    return jsonify({
        "message": "Welcome to the sequences route.",
    })
    