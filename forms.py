#-*-coding:utf-8-*-
from wtforms import fields, validators
from flask_wtf import Form
from werkzeug.security import check_password_hash
from models import db, User
from wtforms import StringField

class LoginForm(Form):
    login = fields.StringField(u'用户名', validators=[validators.required()])
    password = fields.PasswordField(u'密码', validators=[validators.required()])

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError(u'用户不存在')

        # we're comparing the plaintext pw with the the hash from the db
        if not check_password_hash(user.password, self.password.data):
        # to compare plain text passwords use
        # if user.password != self.password.data:
            raise validators.ValidationError(u'密码错误')

    def get_user(self):
        return db.session.query(User).filter_by(login=self.login.data).first()
