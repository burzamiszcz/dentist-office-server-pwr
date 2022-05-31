from flask import Blueprint, Response, request
from model import Person

login = Blueprint("login", __name__)

@login.route('/test')
def test():
    return ";)"

@login.route('/', methods=['POST'])
def select():
    data = request.get_json()
    username = data['username']
    password = data['password']

    try:
        user = Person.query.filter_by(username = username).first()
        if user.password == password:
            return Response("{'message':'user has been logged succesfully'}", status=200, mimetype='application/json')
        else:
            return Response("{'message':'user login unsuccessully'}", status=500, mimetype='application/json')

    except:
        return Response("{'message':'user login unsuccessully'}", status=500, mimetype='application/json')
