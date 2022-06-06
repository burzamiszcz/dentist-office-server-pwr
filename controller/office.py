from flask import Blueprint, Response, jsonify, request
from model import Office
from app import db

office = Blueprint("office", __name__)

@office.route('/test')
def test():
    return ";)"

@office.route('/', methods=['GET'])
def getAll():
    office = Office.query.all()
    return jsonify(office)

@office.route('/<id>', methods=['GET'])
def getOffice(id):
    office = Office.query.filter_by(id = id).first()
    return jsonify(office)
