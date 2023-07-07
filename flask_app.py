from flask import Flask
from blueprints.collatz import collatz_bp
from blueprints.exponentiate import exponentiate_bp

app = Flask(__name__, instance_relative_config=True)

app.register_blueprint(exponentiate_bp)
app.register_blueprint(collatz_bp)

if __name__ == '__main__':
    app.run(debug=True)
