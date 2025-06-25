from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from models import db
from config import Config

# Blueprints
from controllers.guest_controller import guest_bp
from controllers.episode_controller import episode_bp
from controllers.appearance_controller import appearance_bp
from controllers.auth_controller import auth_bp
from controllers.user_controller import user_bp

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    return '<h1>Late Show API is alive!</h1>'


# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

# Register blueprints
app.register_blueprint(guest_bp)
app.register_blueprint(episode_bp)
app.register_blueprint(appearance_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)


if __name__ == '__main__':
    app.run(debug=True)
