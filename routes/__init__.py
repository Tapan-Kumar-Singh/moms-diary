from flask import Blueprint
from .user_routes import user_bp
from .personal_account_routes import personal_account_bp

def register_blueprints(app):
    app.register_blueprint(user_bp)
    app.register_blueprint(personal_account_bp)
