from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

from app import views, models

user_datastore = SQLAlchemyUserDatastore(db, models.User, models.Role)
security = Security(app, user_datastore)

# @app.before_first_request
# def create_user():
#     db.create_all()
#     user_datastore.create_user(email='drew.kowalik@gmail.com', password='password', username='bob')
#     db.session.commit()