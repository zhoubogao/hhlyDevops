from flask import url_for, redirect, render_template, request
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView, helpers, expose
import flask_login as login
from models import User
from forms import LoginForm
# Create customized model view class
class OpsUserModelView(ModelView):
    can_view_details = True
    column_exclude_list = ['password', ]


    def is_accessible(self):
        return login.current_user.is_authenticated

    def on_model_change(self, form, User, is_created):
        User.password = generate_password_hash(form.password.data)

# Create customized model view class
class OpsRoleModelView(ModelView):

    column_list = ['name', 'parents']
    form_columns = ['name', 'parents']   

# Create customized index view class that handles login & registration
class OpsAdminIndexView(AdminIndexView):

    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        return super(OpsAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
#    @rbac.allow(['administrator'], methods=['GET', 'POST'])
    def login_view(self):
        # handle user login
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login.login_user(user)

        if login.current_user.is_authenticated:
            return redirect(url_for('.index'))
        self._template_args['form'] = form
        return super(OpsAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))
