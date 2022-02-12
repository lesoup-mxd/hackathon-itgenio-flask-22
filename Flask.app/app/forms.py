from flask_wtf import FlaskForm 
from wtforms import StringField
from flask import Flask
from wtforms import validators
from wtforms.fields.core import DecimalField, IntegerField, SelectField
from wtforms.fields.simple import FileField, SubmitField, TextAreaField
from wtforms.validators import Length, InputRequired, NumberRange
from flask_wtf.file import FileAllowed


app = Flask(__name__)

class QuestionForm(FlaskForm):
    name = StringField(
        'Name of question', 
        validators=[ InputRequired(), 
        Length(min=1, max=64, message='Need to be from 1 to 64 symbols') 
        ]
    )
    author = StringField(
        'Author',
        validators=[InputRequired()]
        )
    
    theQuestion = StringField(
        'Question',
        validators=[InputRequired()]
        )

    answer = StringField(
        'answer',
        validators=[InputRequired()]
        )
        
    submit = SubmitField('Ok')
