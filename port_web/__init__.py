from flask import Flask
from port_web.forms import ContactForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = 'b5036c041b52933f929f1e97737c6706'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///messages.db"

db = SQLAlchemy(app)

from port_web import routes

