from flask import Blueprint, Response, jsonify, request
from model import Services
from app import db

services = Blueprint("services", __name__)

@services.route('/test')
def test():
    return ";)"

@services.route('', methods=['GET'])
def getAll():
    services = Services.query.all()
    return jsonify(services)

@services.route('/<id>', methods=['GET'])
def getServices(id):
    services = Services.query.filter_by(id = id).first()
    return jsonify(services)

@services.route('/<id>', methods=['DELETE'])
def deleteService(id):
    try:
        services = services.query.filter_by(id = id).first()
        db.session.delete(services)
        db.session.commit()
        return Response(status=200)
    except:
        return Response(status=409)

@services.route('/addservice', methods=['POST'])
def addService():
    data = request.get_json()
    print(data)
    service = Services(
        name=data['name'],
        cost=data['cost'],
    )

    db.session.add(service)
    db.session.commit()


    return Response(status=200)
