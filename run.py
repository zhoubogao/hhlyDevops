#-*-coding:utf-8-*-
import os
from app import app
from models import db , User, Role
from werkzeug.security import generate_password_hash
def build_first_db():
    """
    Populate a small db with some example entries.
    """
    db.drop_all()
    db.create_all()

    anonymous = Role(name = u'Anonymous', description = u'匿名用户')
    admin = Role(name = u'Admin', description = u'管理员')
    develop = Role(name = 'Develop', description = u'开发人员')
    test = Role(name = 'Test', description = u'测试人员')
    ops = Role(name = 'Ops', description = u'运维人员')

    admin_user = User(real_name = u'admin', 
                      email = u'admin@13322.com', 
                      login=u"admin", 
                      password=generate_password_hash(u"admin"),
                      roles=[admin]
                      )

    anonymous_user = User(real_name = u'anonymous',
                          email = u'anonymous@13322.com', 
                          login=u"anonymous", 
                          password=generate_password_hash(u"anonymous"),
                          roles=[anonymous]
                          )

    db.session.add(anonymous)
    db.session.add(admin)
    db.session.add(develop)
    db.session.add(test)
    db.session.add(ops)
    db.session.add(admin_user)
    db.session.add(anonymous_user)

    db.session.commit()
    return


if __name__ == '__main__':

    # Build a sample db on the fly, if one does not exist yet.
    app_dir = os.path.realpath(os.path.dirname(__file__))
    database_path = os.path.join(app_dir, app.config['DATABASE_FILE'])
    if not os.path.exists(database_path):
        build_first_db()
    # Start app
    app.run(debug=True)