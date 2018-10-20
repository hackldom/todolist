from flask_wtf import Form 
from wtforms import StringField, IntegerField
#from wtforms.validators import DataRequired

class PostData(Form):
    title = StringField('title')
    desc =  StringField('desc')