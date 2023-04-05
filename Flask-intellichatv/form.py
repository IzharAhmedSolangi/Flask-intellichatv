from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class QuestionForm(FlaskForm):
    question = StringField('question')
    submit = SubmitField('submit')