from flask import Blueprint, Response, jsonify, request
from model import Office
from app import db

office = Blueprint("office", __name__)

@office.route('/test')
def test():
    return ";)"

@office.route('', methods=['GET'])
def getAll():
    office = Office.query.all()
    return jsonify(office)

@office.route('/<id>', methods=['GET'])
def getOffice(id):
    office = Office.query.filter_by(id = id).first()
    return jsonify(office)

@office.route('/addOffice', methods=['POST'])
def create():
    # try:
        data = request.get_json()

        office = Office(
            name=data['name'],
            email=data['email'],
            city=data['city'],
            street=data['street'],
            street_number=data['street_number'],
            phone_number=data['phone_number']
        )
        db.session.add(office)
        db.session.commit()

        return Response(status=200)