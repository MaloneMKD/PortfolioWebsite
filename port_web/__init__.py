from flask import Flask
from port_web.forms import ContactForm
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import os

app = Flask(__name__)

app.config["SECRET_KEY"] = 'b5036c041b52933f929f1e97737c6706'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///messages.db"
app.config["MAIL_SERVER"] = "smtp.googlemail.com"
app.config["PORT"] = 587
app.config["MAIL_USERNAME"] = os.getenv("GMAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.getenv("GMAIL_PASSWORD")
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
mail = Mail(app)


db = SQLAlchemy(app)

from port_web import routes

