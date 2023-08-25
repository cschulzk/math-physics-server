from flask import Flask, jsonify
from blueprints.home import home_bp
from blueprints.arithmetic.index import arithmetic_bp
from blueprints.sequences.index import sequences_bp
app = Flask(__name__, instance_relative_config=True)

app.register_blueprint(home_bp)
app.register_blueprint(sequences_bp)
app.register_blueprint(arithmetic_bp)

if __name__ == '__main__':
    app.run(debug=True)
