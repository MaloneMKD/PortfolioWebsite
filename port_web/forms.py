from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField, SubmitField
from wtforms.validators import InputRequired, Email


class ContactForm(FlaskForm):
    name = StringField("Name:", validators=[InputRequired()])
    email = EmailField("Email:", validators=[InputRequired(), Email()])
    message = TextAreaField("Message:", validators=([InputRequired()]))
    submit = SubmitField("Submit")
