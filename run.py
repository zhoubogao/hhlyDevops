import os
from app import app, db

def build_first_db():
    """
    Populate a small db with some example entries.
    """

    db.drop_all()
    db.create_all()



    admin_user = User(real_name = u'admin', 
                      email = u'admin@13322.com', 
                      login=u"admin", 
                      password=generate_password_hash(u"admin"))
    db.session.add(admin_user)

    anonymous_user = User(real_name = u'anonymous',
                          email = u'anonymous@13322.com', 
                          login=u"anonymous", 
                          password=generate_password_hash(u"anonymous"))
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