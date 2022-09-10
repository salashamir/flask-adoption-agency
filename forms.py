"""Forms for pet site"""

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, Optional, Length, URL, NumberRange

class AddPetForm(FlaskForm):
    """Form for pet addition"""

    name = StringField("Name", validators=[InputRequired(message="Name cannot be blank.")])
    species = SelectField("Species", choices=[("cat", "Cat 😸"), ("dog", "Dog 🐶"), ("turtle", "Turtle 🐢"), ("salamander", "Salamander 🦎"), ("hamster", "Hamster 🐹"), ("porcupine", "Porcupine 🦔")])
    photo_url = StringField('URL for photo', validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=1,max=60)])
    notes = TextAreaField("Notes", validators=[Optional(), Length(min=3)])


class EditPetForm(FlaskForm):
    """Edit existing pet"""
    photo_url = StringField('URL for photo', validators=[Optional(), URL()])
    notes = TextAreaField('Notes', validators=[Optional(), Length(min=5)])
    available = BooleanField("Availability (T/F)?")