from controller.register import register
from controller.login import login
from controller.persons import persons
from controller.office import office
from controller.services import services
from controller.teeth import teeth
from controller.calendar import calendar


from app import app

#blueprints add
app.register_blueprint(register, url_prefix = "/register")
app.register_blueprint(login, url_prefix = "/login")
app.register_blueprint(persons, url_prefix = "/persons")
app.register_blueprint(office, url_prefix = "/office")
app.register_blueprint(services, url_prefix = "/services")
app.register_blueprint(teeth, url_prefix = "/teeth")
app.register_blueprint(calendar, url_prefix = "/calendar")