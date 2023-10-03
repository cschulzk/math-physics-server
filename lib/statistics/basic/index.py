from flask import Blueprint, jsonify
from lib.statistics.basic.mean import stat_mean_bp
from lib.statistics.basic.max import stat_max_bp
from lib.statistics.basic.min import stat_min_bp
from lib.statistics.basic.median import stat_median_bp
from lib.statistics.basic.range import stat_range_bp

basic_statistics_bp = Blueprint('basic_statistics', __name__, url_prefix='/basic')
basic_statistics_bp.register_blueprint(stat_mean_bp)
basic_statistics_bp.register_blueprint(stat_max_bp)
basic_statistics_bp.register_blueprint(stat_min_bp)
basic_statistics_bp.register_blueprint(stat_median_bp)
basic_statistics_bp.register_blueprint(stat_range_bp)

@basic_statistics_bp.route('/', methods=['GET'])
def basic_statistics():
    return jsonify({
        "message": "Welcome to the basic statistics route.",
    })
    