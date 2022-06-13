from flask import Blueprint, Response, jsonify, request
from model import Person
from app import db

persons = Blueprint("persons", __name__)

@persons.route('/test')
def test():
    return ";)"

@persons.route('', methods=['GET'])
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

@persons.route('/addPerson', methods=['POST'])
def addPerson():
    data = request.get_json()
    teethd =     [['ld8', 'ld7', 'ld6', 'ld5', 'ld4', 'ld3', 'ld2', 'ld1'],
                ['pd1', 'pd2', 'pd3', 'pd4', 'pd5', 'pd6', 'pd7', 'pd8']]

    teethg =    [['lg8', 'lg7', 'lg6', 'lg5', 'lg4', 'lg3', 'lg2', 'lg1'], 
                ['pg1', 'pg2', 'pg3', 'pg4', 'pg5', 'pg6', 'pg7', 'pg8']]
                
    person = Person(
        username=data['username'],
        email=data['email'],
        password=data['password'],
        credential=data['credential'],
        pesel=data['pesel'],
        city=data['city'],
        street=data['street'],
        street_number=data['street_number'],
        country=data['country'],
        phone_number=data['phone_number']
    )

    db.session.add(person)
    db.session.commit()


    return Response(status=200)
