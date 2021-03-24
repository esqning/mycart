from flask_wtf import FlaskForm
from werkzeug.routing import ValidationError
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo

from app.model import User


class LoginFrom(FlaskForm):
    userId = StringField('userId', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    userId = StringField('userId', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password',
                              validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_userId(self, userId):
        user = User.query.filter_by(username=userId.data).first()
        if user is not None:
            raise ValidationError('Please use a different username')


