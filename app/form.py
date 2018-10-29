from flask_wtf import Form 
from wtforms import StringField, IntegerField, TextAreaField, TextField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets import ListWidget, CheckboxInput

class AddNoteForm(Form):
    title = StringField('Title', validators=[DataRequired("Please enter the Title")])
    description =  TextAreaField('Description', validators=[DataRequired("Please Enter some Description")])
    #widget = ListWidget(prefix_label=False)
    ready = CheckboxInput('Is it Done?')
    submit = SubmitField('Add Note')