from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,EqualTo,Email 

class UserForm(FlaskForm):
    name = StringField('Olivia_Davies', validators=[DataRequired()])
    email = StringField('oliviadavies@gmail.com', validators=[DataRequired(),Email()])
    password = PasswordField('welcome1', validators=[DataRequired()])
    confirm_pass = PasswordField('welcome1', validators=[DataRequired(), EqualTo('welcome1')])
    submit = SubmitField()

    class LoginForm(FlaskForm):
        email  = StringField('oliviadavies@gmail.com', validators=[DataRequired()])
        password = PasswordField('welcome1', validators=[DataRequired()])
        submit = SubmitField()
