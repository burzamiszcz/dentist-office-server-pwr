from xml.dom.minidom import Identified
from flask import Blueprint, Response, jsonify, request
from model import Person, Teeth
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
    # teethInfo = Teeth.query.filter_by(patient_id = id).all()
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

@persons.route('/addDoctor', methods=['POST'])
def create():
    # try:
        data = request.get_json()

        person = Person(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            credential="doctor",
            first_name=data['first_name'],
            last_name=data['last_name'],
            phone_number=data['phone_number']
        )
        db.session.add(person)
        db.session.commit()

        return Response(status=200)
    # except:
    #     return Response(status=409)

@persons.route('/addPatient', methods=['POST'])
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
        first_name=data['first_name'],
        last_name=data['last_name'],
        credential="patient",
        pesel=data['pesel'],
        city=data['city'],
        street=data['street'],
        street_number=data['street_number'],
        country=data['country'],
        phone_number=data['phone_number'],
        note = ""
    )

    db.session.add(person)
    db.session.commit()

    id = person.id

    for x in teethd:
        for tooth in x:
            toothToDb = Teeth(
                        patient_id = id,
                        tooth = tooth,
                        status = "0",
                        tooth_info = ""
                    )
            db.session.add(toothToDb)

    for x in teethg:
        for tooth in x:
            toothToDb = Teeth(
                patient_id = id,
                tooth = tooth,
                status = "0",
                tooth_info = ""
            )
            db.session.add(toothToDb)
    db.session.commit()
    return Response(status=200)

@persons.route('/addNote/<id>', methods=['PUT'])
def putNote(id):
    data = request.get_json()
    Person.query.filter_by(id = id).update(data)
    db.session.commit()

    return Response(status=200)
