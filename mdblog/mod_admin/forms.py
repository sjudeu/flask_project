from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import TextAreaField
from wtforms import HiddenField
from wtforms.validators import InputRequired

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = PasswordField("Password", validators=[InputRequired()])

class ArticleForm(FlaskForm):
    title = StringField("Title", validators=[InputRequired()])
    content = TextAreaField("Content")
    html_render = HiddenField()

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField("Old Password", validators=[InputRequired()])
    new_password = PasswordField("New Password", validators=[InputRequired()])

