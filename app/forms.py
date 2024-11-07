# app/forms.py
import app.databaseModel as databaseModel
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, SubmitField, SelectField, ValidationError
from wtforms.validators import InputRequired, Length, DataRequired, Regexp

class SearchForm(FlaskForm):
    # Search Form
    searchOption = SelectField('College', choices = [])
    search = StringField('Search', render_kw={"placeholder": "Search..."})
    studentSelection = SelectField('Student Data', choices=[
        ('firstname', 'First Name'), ('lastname', 'Last Name'), 
        ('id', 'School ID'), ('yearlevel', 'Year'), 
        ('gender', 'Gender')])
    
class StudentForm(FlaskForm):
    studentFirstName = StringField('First Name', validators=[DataRequired()])
    studentLastName = StringField('Last Name', validators=[DataRequired()])
    studentID = StringField('Please enter a valid ID number.', validators=[
        DataRequired(),
        Length(min=9, max=9)])
    studentYear = SelectField('Year Level', choices=[1,2,3,4,5,6] ,validators=[DataRequired()])
    studentGender = SelectField('Select a gender', choices=["Male", "Female", "Non-Binary"], validators=[DataRequired()])
    studentCourse = SelectField('Select a course', choices = [], validators=[DataRequired()])
    studentUpload = FileField('Profile picture')

class ProgramForm(FlaskForm):
    programName = StringField('Program Name', validators=[DataRequired()])
    programCode = StringField('Program Code', validators=[DataRequired()])
    programCollege = SelectField('Select a college', choices = [], validators=[DataRequired()])

class CollegeForm(FlaskForm):
    collegeName = StringField('College Name', validators=[DataRequired()])
    collegeCode = StringField('College Code', validators=[DataRequired()])

