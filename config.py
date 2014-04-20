import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgres://localhost/test'

CSRF_ENABLED = True
SECRET_KEY = 'secret_key'