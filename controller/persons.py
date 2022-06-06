from flask import Blueprint, Response, jsonify

from model import Person, db

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

@persons.route('/<id>', methods=['DELETE'])
def deletePerson(id):
    try:
        person = Person.query.filter_by(id = id).first()
        db.session.delete(person)
        db.session.commit()
        return Response(status=200)
    except:
        return Response(status=409)