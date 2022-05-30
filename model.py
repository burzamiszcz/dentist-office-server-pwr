from app import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)

class Calendar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20), unique = False)
    patient_id = db.Column(db.Integer, unique = False, nullable = True)

class Office(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique = False)
    city = db.Column(db.String(80), unique = False)
    street = db.Column(db.String(80), unique = False)
    street_number = db.Column(db.String(80), unique = False)
    phone_number = db.Column(db.String(80), unique = False)
    email = db.Column(db.String(80), unique = False)

class Services(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique = False)
    cost = db.Column(db.String(80), unique = False)

class Teeth(db.Model):
    patient_id = db.Column(db.Integer, primary_key=True)
    tooth = db.Column(db.String(80), unique = False)
    status = db.Column(db.String(80), unique = False)
    tooth_info = db.Column(db.String(80), unique = False)

if __name__ == "__main__":
    # Run this file directly to create the database tables.
    db.create_all()
