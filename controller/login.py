from flask import Blueprint

login = Blueprint("login", __name__)

@login.route('/test')
def test():
    return ";)"

@login.route('/login', methods=['POST'])
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