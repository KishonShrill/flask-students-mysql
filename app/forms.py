# app/forms.py
import app.databaseModel as databaseModel
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import InputRequired, Length, DataRequired, Regexp

class SearchForm(FlaskForm):
    # Search Form
    searchCollege = SelectField('Course', choices = [])
    search = StringField('Search', render_kw={"placeholder": "Search..."})
    studentSelection = SelectField('Student Data', choices=[('firstname', 'First Name'), ('lastname', 'Last Name'), 
                                                            ('id', 'School ID'), ('yearlevel', 'Year'), 
                                                            ('gender', 'Gender')])
    
class EditForm(FlaskForm):
    # Edit Form
    editFirstName = StringField('First Name', validators=[DataRequired()])
    editLastName = StringField('Last Name', validators=[DataRequired()])
    editID = StringField('Please enter a valid ID number.', validators=[
        DataRequired(),
        Regexp(r'^\d{4}-\d{4}$', message="Valid ID is 4 first numbers, a hyphen, and 4 last numbers")])
    editYear = SelectField('Year Level', choices=[1,2,3,4,5,6] ,validators=[DataRequired()])
    editGender = SelectField('Select a gender', choices=["M", "F", "NB"], validators=[DataRequired()])
    editCourse = SelectField('Select a course', choices = [])