from flask import Flask
from flask_cors import CORS

from controller.register import register_bp
from controller.login import login_bp
from model import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(register_bp)
app.register_blueprint(login_bp)

cors = CORS(app)
db.init_app(app)
# from .app import app 

if __name__ == "__main__":
    from views import *

    app.run(debug=True)




