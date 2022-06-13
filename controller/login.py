from flask import Blueprint, Response, request, jsonify
from model import Person

login = Blueprint("login", __name__)

@login.route('/test')
def test():
    return ";)"

@login.route('', methods=['POST'])
def select():
    data = request.get_json()
    username = data['username']
    password = data['password']

    try:
        user = Person.query.filter_by(username = username).first()
        if user.password == password:
            return jsonify(user)
        else:
            return Response("{\"message\":\"user login unsuccessully\"}", status=500, mimetype='application/json')

    except:
        return Response("{\"message\":\"user login unsuccessully\"}", status=500, mimetype='application/json')
