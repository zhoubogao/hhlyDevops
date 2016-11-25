#-*-coding:utf-8-*-
# Create dummy secrey key so we can use sessions
SECRET_KEY = '123456790'

# Create in-memory database
DATABASE_FILE = '../hhlyDevops_db.sqlite'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_FILE
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_ON_TEARDOWN = True

#flask-bootstrap config
BOOTSTRAP_USE_MINIFIED = True
BOOTSTRAP_SERVE_LOCAL = True  #not default
BOOTSTRAP_CDN_FORCE_SSL = True
BOOTSTRAP_QUERYSTRING_REVVING = True
