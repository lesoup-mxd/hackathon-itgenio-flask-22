import os
from flask_login.utils import login_required
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager 
from flask import render_template



app = Flask(__name__)

@app.route('/home/index1')
@login_required
def index():
    return render_template('home/index.html')

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'basic_flask_project_key'
    APP_NAME = os.environ.get('APP_NAME') or 'Basic Flask Project'
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False


login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Новый текст...'
app.config.from_object(Config)

bootstrap = Bootstrap(app)



db = SQLAlchemy(app)
migrate = Migrate(app, db)

from controllers import home_controller
from controllers import support_controller
from controllers import auth_controller
from app import routes, errors, cookies
from models import user, post

@app.shell_context_processor
def make_shell_context():
    return { 'db': db, 'User': user.User, 'Post': post.Post }