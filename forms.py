from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class LoginForm (FlaskForm):
    username = StringField ("Benutzername", validators=[DataRequired()])
    password = PasswordField ("Passwort", validators =[DataRequired()])
    submit = SubmitField ("Anmelden")

class RegistrationForm (FlaskForm):
    username = StringField ("Benutzername", validators=[DataRequired()])
    password = PasswordField ("Passwort", validators =[DataRequired()])
    password_confirm = PasswordField ("Passwort bestätigen", validators =[DataRequired(), EqualTo("password")])
    submit = SubmitField ("Konto erstellen")
