from flask import Blueprint, Response, jsonify, request
from model import Person

persons = Blueprint("persons", __name__)

@persons.route('/test')
def test():
    return ";)"

@persons.route('/', methods=['GET'])
def getAll():
    persons = Person.query.all()
    return jsonify(persons)

@persons.route('/<id>', methods=['GET'])
def getPerson(id):
    person = Person.query.filter_by(id = id).first()
    return jsonify(person)