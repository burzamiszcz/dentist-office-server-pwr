from calendar import calendar
from flask import Blueprint, Response, jsonify, request
from model import Calendar, Person
from app import db

calendar = Blueprint("calendar", __name__)

@calendar.route('/test')
def test():
    return ";)"

@calendar.route('', methods=['GET'])
def getAll():
    calendar = Calendar.query.all()
    return jsonify(calendar)

@calendar.route('/<id>', methods=['GET'])
def getCalendarForPatient(id):
    person = Person.query.filter_by(id = id).first()
    if person.credential == "doctor":
        calendar = Calendar.query.filter_by(patient_id = id).first()
    elif person.credential == "patient":
        calendar = Calendar.query.filter_by(doctor_id = id).first()

    return jsonify(calendar)

@calendar.route('/<id>', methods=['DELETE'])
def deleteCalendar(id):
    try:
        calendar = calendar.query.filter_by(id = id).first()
        db.session.delete(calendar)
        db.session.commit()
        return Response(status=200)
    except:
        return Response(status=409)

@calendar.route('/addservice', methods=['POST'])
def addCalendar():
    data = request.get_json()
    print(data)
    service = Calendar(
        date=data['date'],
        patient_id=data['patient_id'],
        doctor_id=data['doctor_id']
    )

    db.session.add(service)
    db.session.commit()


    return Response(status=200)
