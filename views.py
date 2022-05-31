from controller.register import register
from controller.login import login
from controller.persons import persons


from app import app

#blueprints add
app.register_blueprint(register, url_prefix = "/register")
app.register_blueprint(login, url_prefix = "/login")
app.register_blueprint(persons, url_prefix = "/persons")