# app/forms.py
import app.databaseModel as databaseModel
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import InputRequired, Length, DataRequired, Regexp

class SearchForm(FlaskForm):
    # Search Form
    submit = SubmitField('Search')
    querySelection = SelectField('Course', choices = [])
    search = StringField('Search', render_kw={"placeholder": "Search student..."})
    studentSelection = SelectField('Student Data', choices=[('FirstName', 'First Name'), ('LastName', 'Last Name'), 
                                                            ('ID', 'School ID'), ('YearLevel', 'Year'), 
                                                            ('Gender', 'Gender')])
    
class EditForm(FlaskForm):
    # Edit Form
    editFirstName = StringField('First Name', validators=[DataRequired()])
    editLastName = StringField('Last Name', validators=[DataRequired()])
    editID = StringField('ID', validators=[
        DataRequired(),
        Regexp(r'^\d{4}-\d{4}$', message="Valid ID is 4 first numbers, a hyphen, and 4 last numbers")])
    editYear = StringField('Year', validators=[DataRequired()])
    editGender = StringField('Gender', validators=[DataRequired()])
    editCourse = SelectField('Course', choices = [])