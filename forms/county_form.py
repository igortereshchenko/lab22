from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, validators, SubmitField


class CountryForm(FlaskForm):
   id = HiddenField("Id")

   name = StringField("Name: ",[
                                    validators.DataRequired("Please enter skill name."),
   ])

   president = StringField("President : ", [
       validators.DataRequired("Please enter skill name."),
   ])

   population = StringField("Population: ", [
       validators.NumberRange(1000),
   ])

   year_creation = StringField("Year: ", [
       validators.NumberRange(max = 2019),
   ])

   submit = SubmitField("Save")