from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# .py files with another endpoints
from controller.register import register

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
cors = CORS(app)
app.register_blueprint(register, url_prefix = "/register")

import model


@app.route('/login', methods=['POST'])
def select():
    data = request.get_json()
    username = data['username']
    password = data['password']

    try:
        user = User.query.filter_by(username = username).first()
        if user.passowrd == password:
            return Response("{'message':'user has been logged succesfully'}", status=200, mimetype='application/json')
        else:
            return Response("{'message':'user login unsuccessully'}", status=500, mimetype='application/json')

    except:
        return Response("{'message':'user login unsuccessully'}", status=500, mimetype='application/json')


    return jsonify(username=username, password=password)
