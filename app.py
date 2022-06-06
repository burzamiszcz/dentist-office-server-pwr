from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
cors = CORS(app)
db = SQLAlchemy(app)
# from .app import app 

if __name__ == "__main__":
    from views import *

    app.run(debug=True)




