from flask import jsonify, request, Blueprint
collatz_bp = Blueprint('collatz', __name__)

@collatz_bp.route('/collatz', methods=['GET', 'POST'])
def collatz():
  if request.method == 'GET':
    return jsonify({"help": "https://en.wikipedia.org/wiki/Collatz_conjecture"})
  elif request.method == 'POST':
    try:
      start: int = request.get_json()["start"]
      if type(start) is not int and start <= 0:
          return jsonify({"error": "The start must be a positive integer"})
      if start > 100000:
          return jsonify({"angry_note": "Get your own computer!"})

      value = start
      sequence = [start]
      while value != 1:
          if value % 2 == 0:
              value = value//2
          else:
              value = (3 * value + 1)//2
          sequence.append(value)
      return jsonify({"sequence": sequence})
    except:
      return jsonify({"error": "An error occurred. Check that the request body has a 'start' key."})
