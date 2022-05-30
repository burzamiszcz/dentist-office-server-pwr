from flask import Blueprint, jsonify, request
from model import Person
from app import db

register = Blueprint("register", __name__)

@register.route('/test')
def test():
    return ";)"

@register.route('/', methods=['POST'])
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
        return jsonify('done')
    except:
        return jsonify('notdone')

