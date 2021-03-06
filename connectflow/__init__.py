import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

##########################
#### DATABASE SETUP ######
##########################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

#########################
#### LOGIN CONFIGS ######
#########################
login_manager = LoginManager() 
login_manager.init_app(app)
login_manager.login_view = 'users.login'

#########################
#### BLUEPRINT SETUP ####
#########################
from connectflow.core.views import core
from connectflow.error.views import error
from connectflow.users.views import users
from connectflow.numbers.views import numbers
from connectflow.pservers.views import pservers
from connectflow.vservers.views import vservers
from connectflow.customers.views import customers
from connectflow.partners.views import partners
from connectflow.networks.views import networks
from connectflow.ap.views import ap

app.register_blueprint(core)
app.register_blueprint(error)
app.register_blueprint(users)
app.register_blueprint(numbers)
app.register_blueprint(pservers)
app.register_blueprint(vservers)
app.register_blueprint(customers)
app.register_blueprint(partners)
app.register_blueprint(networks)
app.register_blueprint(ap)