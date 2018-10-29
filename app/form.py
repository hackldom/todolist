from flask_wtf import Form 
from wtforms import StringField, IntegerField, TextAreaField, TextField, SubmitField
#from wtforms.validators import DataRequired

class AddNoteForm(Form):
    title = StringField('Title')
    description =  TextAreaField('Description')
    submit = SubmitField('Add Note')