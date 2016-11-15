#-*-coding:utf-8-*-
from flask import url_for, redirect, request, current_app
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView, helpers, expose
from werkzeug.security import generate_password_hash
from flask_login import current_user, login_user, logout_user
from models import User, Role, Device, Platforms_info, Ip, Project, Domain, Port, App
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
    can_export = True
    can_view_details = True
    column_exclude_list = ['password', ]
    column_searchable_list = ( 'real_name', 'login', Role.name)
    column_display_all_relations = True



    def is_accessible(self):
        return current_user.is_authenticated

    def on_model_change(self, form, User, is_created):
        User.password = generate_password_hash(form.password.data)

# Create customized model view class
class RoleModelView(ModelView):
    can_export = True
    can_view_details = True
    column_editable_list = ('description',)
    column_searchable_list = ( 'name', User.login)
    column_display_all_relations = True



# Create customized model view class
class Platforms_infoModelView(ModelView):
    can_export = True
    can_view_details = True
    column_editable_list = ('platform', 'description','url', 
                            'username', 'password', 'ps',
                            )
    column_searchable_list = ('platform', 'description','url', 
                            'username', 'password', 'ps',
                            )
    column_display_all_relations = True



# Create customized model view class
class DeviceModelView(ModelView):
    can_export = True
    can_view_details = True
    column_editable_list = ('device_num', 'device_name', 'idc', 'location', 
                            'used_to','hardware_type', 'brand', 'buy_date',
                            'brand','fast_repair_code', 'cpu', 'memory', 
                            'disk',
                            )
    column_searchable_list = ('device_num', 'device_name', 'idc', 'location', 
                            'used_to','hardware_type', 'brand', 'buy_date',
                            'brand','fast_repair_code', 'cpu', 'memory', 
                            'disk', Ip.ip
                            )
    column_display_all_relations = True



# Create customized model view class
class IpModelView(ModelView):
    can_export = True
    can_view_details = True
    column_editable_list = ('isp','ip', 'use', 'mask', 'mac',
                            'route', 'switch_port', 
                            'username', 'password',
                            )
    column_searchable_list = ('isp','ip', 'use', 'mask', 'mac',
                            'route', 'switch_port', 
                            'username', 'password',
                            )
    column_display_all_relations = True


# Create customized model view class
class ProjectModelView(ModelView):
    can_export = True
    can_view_details = True
    column_editable_list = ('project', )
    column_searchable_list = ( 'project', App.app)
    column_display_all_relations = True

# Create customized model view class
class DomainModelView(ModelView):
    can_export = True
    can_view_details = True
    column_editable_list = ('domain',)
    column_searchable_list = ( 'domain', App.app)
    column_display_all_relations = True

# Create customized model view class
class PortModelView(ModelView):
    can_export = True
    can_view_details = True
    column_editable_list = ('port',)
    column_searchable_list = ( 'port', App.app)
    column_display_all_relations = True

# Create customized model view class
class AppModelView(ModelView):
    can_export = True
    can_view_details = True
    column_editable_list = ('description', 'ps',)
    column_searchable_list = ( 'app', Domain.domain, Port.port)
    column_display_all_relations = True



# Create customized index view class that handles login & registration
class OpsAdminIndexView(AdminIndexView):

    @expose('/')
#    @anon_permission.require(http_exception=403)
#    @admin_denied.require(http_exception=403)
    def index_view(self):
        if not current_user.is_authenticated:
            return redirect(url_for('auth.login'))
#        with admin_permission.require(http_exception=403):

        return super(OpsAdminIndexView, self).index_view()

