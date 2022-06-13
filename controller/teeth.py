from flask import Blueprint, Response, jsonify, request
from model import Person, Teeth
from app import db

teeth = Blueprint("teeth", __name__)

@teeth.route('/test')
def test():
    return ";)"

@teeth.route('', methods=['GET'])
def getAll():
    teeth = Person.query.all()
    return jsonify(teeth)

@teeth.route('/<id>', methods=['GET'])
def getTeeth(id):
    teethInfo = Teeth.query.filter_by(patient_id = id).all()
    return jsonify(teethInfo)

@teeth.route('<patient_id>/<tooth_id>', methods=['PUT'])
def putTeeth(patient_id, tooth_id):
    data = request.get_json()
    teethInfo = Teeth.query.filter_by(patient_id = patient_id, tooth = tooth_id).update(data)
    db.session.commit()

    return jsonify(teethInfo)

