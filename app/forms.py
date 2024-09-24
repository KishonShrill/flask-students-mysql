# app/forms.py
import app.databaseModel as databaseModel
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import InputRequired, Length, DataRequired, Regexp

class SearchForm(FlaskForm):
    # Search Form
    searchCollege = SelectField('College', choices = [])
    searchCourse = SelectField('Course', choices = [])
    search = StringField('Search', render_kw={"placeholder": "Search..."})
    studentSelection = SelectField('Student Data', choices=[
        ('firstname', 'First Name'), ('lastname', 'Last Name'), 
        ('id', 'School ID'), ('yearlevel', 'Year'), 
        ('gender', 'Gender')])
    courseSelection = SelectField('Course Data', choices=[
        ('coursename', 'Programs'), ('coursecode', 'Course Code'),
        ('collegecode', 'College')])
    collegeSelection = SelectField('College Data', choices=[
        ('collegename', 'College'), ('collegecode', 'Code')])
    
class StudentForm(FlaskForm):
    # Edit Form
    studentFirstName = StringField('First Name', validators=[DataRequired()])
    studentLastName = StringField('Last Name', validators=[DataRequired()])
    studentID = StringField('Please enter a valid ID number.', validators=[
        DataRequired(),
        Length(min=9, max=9)])
    studentYear = SelectField('Year Level', choices=[1,2,3,4,5,6] ,validators=[DataRequired()])
    studentGender = SelectField('Select a gender', choices=["M", "F", "NB"], validators=[DataRequired()])
    studentCourse = SelectField('Select a course', choices = [], validators=[DataRequired()])