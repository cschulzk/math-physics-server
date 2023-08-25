from flask import Blueprint, jsonify
from blueprints.sequences.collatz import collatz_bp
home_bp = Blueprint('home', __name__, url_prefix='')
home_bp.register_blueprint(collatz_bp)

@home_bp.route('/', methods=['GET'])
def hello():
    return jsonify({
        "message": "Welcome to the math/physics API!",
        "routes": {
            "arithmetic": {
                "exponentiate": {}
            },
            "sequences": {
                "collatz": {}
            }
        }
    })
    