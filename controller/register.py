from flask import Blueprint, Response, jsonify, request
from model import Person
from app import db

register = Blueprint("register", __name__)

@register.route('/test')
def test():
    return ";)"

@register.route('', methods=['POST'])
def create():
    # try:
        data = request.get_json()

        person = Person(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            credential=data["credential"]
        )
        db.session.add(person)
        db.session.commit()

        return Response(status=200)
    # except:
    #     return Response(status=409)

