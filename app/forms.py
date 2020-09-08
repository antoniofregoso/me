from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, HiddenField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Email, Length

class LeadForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('About me', validators=[Length(min=0, max=140)])
    utm_campaign = HiddenField()
    utm_source = HiddenField()
    utm_medium = HiddenField()
    utm_term = HiddenField()
    utm_content = HiddenField() 
    submit = SubmitField('Enviar')

class NewsletterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Inscribir')