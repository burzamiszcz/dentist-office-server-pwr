from flask import Blueprint, Response, request

from model import Person, db

register_bp = Blueprint('register', __name__)


@register_bp.route('/test')
def test():
    return ";)"


@register_bp.route('/register', methods=['POST'])
def create():
    try:
        data = request.get_json()

        person = Person(
            username=data['username'],
            email=data['email'],
            password=data['password']
        )

        db.session.add(person)
        db.session.commit()
        return Response(status=200)
    except:
        return Response(status=409)
