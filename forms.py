from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import InputRequired, Length, EqualTo


class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=3, max=80)])
    password = PasswordField(validators=[InputRequired(), Length(min=4)])
    confirm = PasswordField(validators=[InputRequired(), EqualTo('password')])
    city = StringField()
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired()])
    password = PasswordField(validators=[InputRequired()])
    submit = SubmitField('Login')


class CreateQuizForm(FlaskForm):
    title = StringField(validators=[InputRequired(), Length(min=3, max=120)])
    main_genre_id = SelectField(coerce=int, choices=[], validate_choice=False)
    subgenre_id = SelectField(coerce=int, choices=[], validate_choice=False)
    difficulty = SelectField(choices=['Easy', 'Medium', 'Hard'])
    submit = SubmitField('Create')

    

