#-*-coding:utf-8-*-
import os
from flask import Flask, Blueprint, url_for, redirect, current_app, g, render_template, request
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import (LoginManager,
                         login_required, 
                         current_user, 
                         login_user, 
                         logout_user,
                         )
from flask_bootstrap import Bootstrap
from models import db
import models
from views import prcp
import views 
from forms import LoginForm
from werkzeug.security import generate_password_hash
from flask_principal import (
                             ActionNeed,
                             AnonymousIdentity,
                             Identity,
                             identity_changed,
                             identity_loaded,
                             Permission,
                             Principal,
                             RoleNeed,
                             Denial,
                             )

# Create Flask application
app = Flask(__name__, static_url_path='/static')
app.config.from_pyfile('config.py')
bootstrap = Bootstrap(app)
db.app = app
db.init_app(app)

# url redirect
auth = Blueprint('auth', __name__)
asset = Blueprint('asset', __name__)


# Initialize flask-login
login_manager = LoginManager(app)
#login_manager.anonymous_user = CustomAnonymousUser

@login_manager.user_loader
def load_user(user_id):
    return db.session.query(models.User).get(user_id)

# Initialize flask-principal
prcp.app = app
prcp.init_app(app)

@identity_loaded.connect
def on_identity_loaded(sender, identity):
    # Get the user information from the db
    user = db.session.query(models.User).get(identity)
    # Update the roles that a user can provide
    for role in user.roles:
        identity.provides.add(RoleNeed(role.name))
    # Save the user somewhere so we only look it up once
    identity.user = user

@app.before_request
def set_identity():
    if  current_user and not current_user.is_anonymous:
        if not hasattr(g, 'identity'):
            g.identity = Identity(current_user.id)
    else:
        if not hasattr(g, 'identity'):
            g.identity = AnonymousIdentity()

# Flask views

@app.route('/')
#@login_required
def index():
    if current_user.is_authenticated:
        return render_template('index.html')
    else:
        return redirect(url_for('auth.login'))
    

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if current_user and current_user.is_authenticated:
        return redirect(url_for('index'))
    if form.validate_on_submit():
        user = form.get_user()
        login_user(user)
        return redirect(url_for('index'))

    return render_template('login.html', form=form)

@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login')) 

@asset.route('/platforminfo', methods=['GET', 'POST'])
def platforminfo():

    return render_template('platforminfo.html')#, form=form)

@asset.route('/deviceinfo', methods=['GET', 'POST'])
def deviceinfo():

    return render_template('deviceinfo.html')#, form=form)
    
@asset.route('/appinfo', methods=['GET', 'POST'])
def appinfo():

    return render_template('appinfo.html')#, form=form)


# Ceate admin
admin = Admin(app, 
              'HHLY-DEVOPS: Admin', 
              index_view=views.OpsAdminIndexView(), 
              base_template='admin_home.html'
              )

# Add view
admin.add_view(views.UserModelView(models.User, db.session))
admin.add_view(views.RoleModelView(models.Role, db.session))
admin.add_view(views.Platforms_infoModelView(models.Platforms_info, db.session))
admin.add_view(views.DeviceModelView(models.Device, db.session))
admin.add_view(views.IpModelView(models.Ip, db.session))
admin.add_view(views.ProjectModelView(models.Project, db.session))
admin.add_view(views.AppModelView(models.App, db.session))


app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(asset, url_prefix='/asset')


