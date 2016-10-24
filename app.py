#-*-coding:utf-8-*-
import os
from flask import Flask, url_for, redirect
import flask_admin as admin
import flask_login as login

from models import db , User
from views import OpsUserModelView, OpsRoleModelView, OpsAdminIndexView

# Create Flask application
app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)

def init_login():
    login_manager = login.LoginManager()
#    login_manager.anonymous_user = testU
    login_manager.init_app(app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)
# Initialize flask-login
init_login()


# Flask views
@app.route('/')
def index():
    return redirect(url_for('admin.index'))


# Create admin
admin = admin.Admin(app, 
                    'HHLY-DEVOPS: Admin-Background', 
                    index_view=OpsAdminIndexView(), 
                    base_template='my_master.html'
                    )

# Add view
admin.add_view(OpsUserModelView(User, db.session))


