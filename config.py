# Create dummy secrey key so we can use sessions
SECRET_KEY = '123456790'

# Create in-memory database
DATABASE_FILE = 'hhlyDevops_db.sqlite'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_FILE
SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = True

