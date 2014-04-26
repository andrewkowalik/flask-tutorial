import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgres://localhost/test'

CSRF_ENABLED = True
SECRET_KEY = 'secret_key'
SECURITY_PASSWORD_HASH = 'bcrypt'
SECURITY_PASSWORD_SALT = 'something'
SECURITY_REGISTERABLE = True
SECURITY_SEND_REGISTER_EMAIL = False