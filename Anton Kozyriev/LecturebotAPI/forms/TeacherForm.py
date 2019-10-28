from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, validators


class TeacherForm(FlaskForm):
    Name = StringField("Teacher's name: ", [
        validators.DataRequired("Teacher's name cannot be empty!")
    ], render_kw={"placeholder": "Teacher's name: "})

    Birthday = IntegerField("Birthday: ", [
        validators.DataRequired("Birthday cannot be empty!"),
        validators.NumberRange(min=1980)
    ], render_kw={"placeholder": "Birthday: "})

    Salary = IntegerField("Salary: ", [
        validators.DataRequired("Salary cannot be empty!"),
        validators.NumberRange(min=0)
    ], render_kw={"placeholder": "Salary: "})

    Position = StringField("Position: ", [
        validators.DataRequired("Position cannot be empty!")
    ], render_kw={"placeholder": "Position: "})

    Submit = SubmitField("Add")
