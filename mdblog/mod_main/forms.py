from flask_wtf import FlaskForm
from wtforms import StringField

from wtforms.validators import Email

class NewsletterForm(FlaskForm):
    email = StringField(validators=[Email()])

