from flask import jsonify, request, Blueprint

stat_range_bp = Blueprint('range', __name__)

@stat_range_bp.route('/range', methods=['GET', 'POST'])
def mean():
  if request.method == 'GET':
    return jsonify({"help": "https://en.wikipedia.org/wiki/Range_(statistics)"})
  elif request.method == 'POST':
    try:
      values: list = request.get_json()["values"]
      if type(values) is not list:
        return jsonify({"error": "You must provide a list of numbers."})
      if values.length > 1000:
          return jsonify({"angry_note": "Get your own computer!"})
      result = max(values) - min(values)
      return jsonify({"result": result})
    except:
      return jsonify({"error": "An error occurred. Check that the request body has both a 'base' and a 'power' key."})
      