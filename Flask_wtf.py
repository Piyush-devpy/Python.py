from flask_wtf import FlaskForm,StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,Length

class RegisterationForm (FlaskForm):
    name = StringField("Full Name", validators = [DataRequired()]),
    email = StringField("Email",validators=[DataRequired(), Email]),
    password = PasswordField("Password",validators = [DataRequired(),Length(min=10)]),
    submit = SubmitField("Register")