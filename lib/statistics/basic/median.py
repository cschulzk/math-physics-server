from flask import jsonify, request, Blueprint

stat_median_bp = Blueprint('median', __name__)

@stat_median_bp.route('/median', methods=['GET', 'POST'])
def mean():
  if request.method == 'GET':
    return jsonify({"help": "https://en.wikipedia.org/wiki/Median"})
  elif request.method == 'POST':
    try:
      values: list = request.get_json()["values"]
      if type(values) is not list:
        return jsonify({"error": "You must provide a list of numbers."})
      if values.length > 1000:
          return jsonify({"angry_note": "Get your own computer!"})
      result = 1 # Do the calculation here
      return jsonify({"result": result})
    except:
      return jsonify({"error": "An error occurred. Check that the request body has both a 'base' and a 'power' key."})
      