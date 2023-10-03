from flask import jsonify, request, Blueprint

stat_min_bp = Blueprint('min', __name__)

@stat_min_bp.route('/min', methods=['GET', 'POST'])
def mean():
  if request.method == 'GET':
    return jsonify({"help": "https://en.wikipedia.org/wiki/Statistics"})
  elif request.method == 'POST':
    try:
      values: list = request.get_json()["values"]
      if type(values) is not list:
        return jsonify({"error": "You must provide a list of numbers."})
      if values.length > 1000:
          return jsonify({"angry_note": "Get your own computer!"})
      result = min(values)
      return jsonify({"result": result})
    except:
      return jsonify({"error": "An error occurred. Check that the request body has both a 'base' and a 'power' key."})
      