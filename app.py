from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# .py files with endpoints import
from controller.register import register
from controller.login import login

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
cors = CORS(app)

#blueprints add
app.register_blueprint(register, url_prefix = "/register")
app.register_blueprint(login, url_prefix = "/login")

#classes import
import model



