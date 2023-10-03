from flask import Blueprint, jsonify
from lib.statistics.basic.index import basic_statistics_bp

statistics_bp = Blueprint('statistics', __name__, url_prefix='/statistics')
statistics_bp.register_blueprint(basic_statistics_bp)

@statistics_bp.route('/', methods=['GET'])
def arithmetic():
    return jsonify({
        "message": "Welcome to the statistics route.",
    })
    