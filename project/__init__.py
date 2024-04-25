from os import path
from flask import Flask
from flask_caching import Cache
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "my_database.db"
cache = Cache()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sexy_presentation'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['CACHE_TYPE'] = 'simple'
    cache.init_app(app) 
    db.init_app(app)

    from project.views import views
    from project.auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    

    from .models import User
    
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
