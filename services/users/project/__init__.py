import os # needed for the app_settings to get
          # pulled in as from the container's
          # env variable
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

# init Flask app
app = Flask(__name__);

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# init the db from app
db = SQLAlchemy(app)

# user schema
class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  username = db.Column(db.String(128), nullable=False)
  email = db.Column(db.String(128), nullable=False)
  active = db.Column(db.Boolean(), default=True, nullable=False)

  def __init__(self, username, email):
    self.username = username
    self.email = email

# app routes
@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
      'status':'success',
      'message':'pong!'
    })