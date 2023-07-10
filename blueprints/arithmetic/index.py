from flask import Blueprint, jsonify
from blueprints.arithmetic.exponentiate import exponentiate_bp
arithmetic_bp = Blueprint('arithmetic', __name__, url_prefix='/arithmetic')
arithmetic_bp.register_blueprint(exponentiate_bp)

@arithmetic_bp.route('/', methods=['GET'])
def arithmetic():
    return jsonify({"help": "This is how to use this route."})
    