from enum import unique

from sqlalchemy import nullslast
from app import db
from dataclasses import dataclass

@dataclass
class Person(db.Model):
    id: int
    username: str
    email: str
    password: str
    credential = str
    pesel = str
    city = str
    street = str
    street_number = str
    country = str
    phone_number = str
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    credential = db.Column(db.String(120), unique=False, nullable=False)
    pesel = db.Column(db.String(120), unique=False, nullable=True)
    city = db.Column(db.String(120), unique=False, nullable=True)
    street = db.Column(db.String(120), unique=False, nullable=True)
    street_number = db.Column(db.String(120), unique=False, nullable=True)
    country = db.Column(db.String(120), unique=False, nullable=True)
    phone_number = db.Column(db.String(120), unique=False, nullable=True)
    

@dataclass
class Calendar(db.Model):
    id: int
    date: str
    patient_id: int

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20), unique = False)
    patient_id = db.Column(db.Integer, unique = False, nullable = True)

@dataclass
class Office(db.Model):
    id: int
    name: str
    city: str
    street: str
    street_number: str
    phone_number: str
    email: str

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique = False)
    city = db.Column(db.String(80), unique = False)
    street = db.Column(db.String(80), unique = False)
    street_number = db.Column(db.String(80), unique = False)
    phone_number = db.Column(db.String(80), unique = False)
    email = db.Column(db.String(80), unique = False)

@dataclass
class Services(db.Model):
    id: int
    name: str
    cost: str

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique = False)
    cost = db.Column(db.String(80), unique = False)

@dataclass
class Teeth(db.Model):
    patient_id: int
    tooth: str
    status: str
    tooth_info: str

    patient_id = db.Column(db.Integer, primary_key=True)
    tooth = db.Column(db.String(80), primary_key = True, unique = False)
    status = db.Column(db.String(80), unique = False)
    tooth_info = db.Column(db.String(80), unique = False)

if __name__ == "__main__":
    # Run this file directly to create the database tables.
    db.create_all()
