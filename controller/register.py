from flask import Blueprint

register = Blueprint("register", __name__)

@register.route('/test')
def test():
    return ";)"

@register.route('/register', methods=['POST'])
def create():
    data = request.get_json()

    person = Person(
        username=data['username'],
        email=data['email'],
        password=data['password']
    )

    db.session.add(user)
    db.session.commit()

    return jsonify(user)

