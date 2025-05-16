from flask import Flask
from chatbot.app.routes import main as main_blueprint

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SECRET_KEY'] = 'supersecretkey'
    app.register_blueprint(main_blueprint)
    return app
