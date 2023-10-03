from flask import Flask, jsonify
from lib.home import home_bp
from lib.arithmetic.index import arithmetic_bp
from lib.sequences.index import sequences_bp
from lib.statistics.index import statistics_bp
app = Flask(__name__, instance_relative_config=True)

app.register_blueprint(home_bp)
app.register_blueprint(sequences_bp)
app.register_blueprint(arithmetic_bp)
app.register_blueprint(statistics_bp)

if __name__ == '__main__':
    app.run(debug=True)
