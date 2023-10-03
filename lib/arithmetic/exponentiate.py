from flask import jsonify, request, Blueprint

exponentiate_bp = Blueprint('exponentiate', __name__)

@exponentiate_bp.route('/exponentiate', methods=['GET', 'POST'])
def exponentiate():
  if request.method == 'GET':
    return jsonify({"help": "https://en.wikipedia.org/wiki/Exponentiation"})
  elif request.method == 'POST':
    try:
      base: float | int = request.get_json()["base"]
      power: float | int = request.get_json()["power"]
      if type(base) is not int and type(base) is not float:
          if type(power) is not int and type(power) is not float:
              return jsonify({"error": "The base and power must be both be numbers"})
          return jsonify({"error": "The base must be a number"})
      if type(power) is not int and type(power) is not float:
              return jsonify({"error": "The power must be a number"})
      if base > 10000 or power > 10:
          return jsonify({"angry_note": "Get your own computer!"})
      result = base ** power
      return jsonify({"result": result})
    except:
      return jsonify({"error": "An error occurred. Check that the request body has both a 'base' and a 'power' key."})
      