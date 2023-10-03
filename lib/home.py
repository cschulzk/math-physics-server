from flask import Blueprint, jsonify
home_bp = Blueprint('home', __name__, url_prefix='')

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
            },
            "statistics": {
                "basic": {
                  "mean": {},
                  "median": {},
                  "range": {},
                  "max": {},
                  "min": {}                    
                } 
            }
        }
    })
    