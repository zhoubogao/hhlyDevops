#-*-coding:utf-8-*-
from flask import url_for, redirect, request, current_app
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView, helpers, expose
from werkzeug.security import generate_password_hash
from flask_login import current_user, login_user, logout_user
from models import User, Role, Device, Platforms_info, Ip
from forms import LoginForm
from flask_principal import (
                             ActionNeed,
                             AnonymousIdentity,
                             Identity,
                             identity_changed,
                             identity_loaded,
                             Permission,
                             Principal,
                             RoleNeed,
                             Denial
                             )


# Initialize flask-principal
prcp = Principal()

anon_permission = Permission()
admin_permission = Permission(RoleNeed('Admin'))
admin_or_editor = Permission(RoleNeed('Admin'), RoleNeed('Devlop'))
devlop_permission = Permission(RoleNeed('Devlop'))
admin_denied = Denial(RoleNeed('Admin'))




# Create customized model view class
class UserModelView(ModelView):
    can_view_details = True
    column_exclude_list = ['password', ]
    column_list = ('real_name', 'email', 'login', 'roles')
    column_searchable_list = ( User.real_name, User.login)


    def is_accessible(self):
        return current_user.is_authenticated

    def on_model_change(self, form, User, is_created):
        User.password = generate_password_hash(form.password.data)

# Create customized model view class
class DeviceModelView(ModelView):
    column_searchable_list = ( 'device_name', Ip.ip)
    column_list = ('device_name', Ip.ip, 'idc', 'location', 
                   'hardware_type', 'brand', 'buy_date', 
                   'fast_repair_code', 'cpu', 'mem',
                   'disk',)



# Create customized index view class that handles login & registration
class OpsAdminIndexView(AdminIndexView):

    @expose('/')
#    @anon_permission.require(http_exception=403)
#    @admin_denied.require(http_exception=403)
    def index_view(self):
        if not current_user.is_authenticated:
            return redirect(url_for('auth.login'))
        with admin_permission.require(http_exception=403):

            return super(OpsAdminIndexView, self).index_view()

