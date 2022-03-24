from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)



@app.route('/create/<username>/<password>')
def create(username, password):
    user = User(username = username, password = password)
    db.session.add(user)
    db.session.commit()
    return f"user <b>{username}</b> created successfully"


@app.route('/select/<username>')
def select(username):
    user = User.query.filter_by(username=username).first()
    return f"The password is <b>{user.password}</b>"
