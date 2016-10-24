from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
# Create user model.
db = SQLAlchemy()
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    real_name = db.Column(db.Unicode(length=255))
    email = db.Column(db.Unicode(length=254))
    login = db.Column(db.Unicode(length=254), unique=True)
    password = db.Column(db.Unicode(length=255))

    # Required for administrative interface
    def __unicode__(self):
        return self.username
