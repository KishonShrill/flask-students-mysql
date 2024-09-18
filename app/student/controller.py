from flask import render_template, redirect, request, flash, url_for
from . import student_bp
import app.databaseModel as databaseModel
from app.forms import *


@student_bp.route('/students')
def index():
    searchForm = SearchForm()
    editForm = EditForm()
    courses = databaseModel.DatabaseManager.allCourses()
    students = databaseModel.DatabaseManager.allStudents()
    searchForm.querySelection.choices = [('', 'Select a Course')] + [(course[1], course[0]) for course in courses]
    editForm.editCourse.choices = [(course[1], course[0]) for course in courses]
    return render_template('students.html', results=students, searchForm=searchForm, editForm=editForm, title='List of Students')

@student_bp.route('/students/search/', methods=['POST','GET'])
def search():
    searchForm = SearchForm()
    editForm = EditForm()
    courses = databaseModel.DatabaseManager.allCourses()
    query = request.form['search']
    college = request.form['querySelection']
    print(f"Picked College: {college}")

    searchForm.querySelection.choices = [('', 'Select a Course')] + [(course[1], course[0]) for course in courses]
    editForm.editCourse.choices = [(course[1], course[0]) for course in courses]
    if query:
        choices = searchForm.studentSelection.data
        results: str = ''

        if query and college:
            print(f"This is first asdkljh stage")
            match choices:
                case "FirstName":
                    results = databaseModel.DatabaseManager.queryStudentFirstNameWithCollege(query,college)
                case "LastName":
                    results = databaseModel.DatabaseManager.queryStudentLastNameWithCollege(query,college)
                case "ID":
                    results = databaseModel.DatabaseManager.queryStudentIDWithCollege(query,college)
                case "YearLevel":
                    results = databaseModel.DatabaseManager.queryStudentYearWithCollege(query,college)
                case "Gender":
                    results = databaseModel.DatabaseManager.queryStudentGenderWithCollege(query,college)
                case _:
                    return redirect(url_for("student.index"))
                
        elif query and not college:
            print(f"This is second stage")
            match choices:
                case "FirstName":
                    results = databaseModel.DatabaseManager.queryStudentFirstName(query)
                case "LastName":
                    results = databaseModel.DatabaseManager.queryStudentLastName(query)
                case "ID":
                    results = databaseModel.DatabaseManager.queryStudentID(query)
                case "YearLevel":
                    results = databaseModel.DatabaseManager.queryStudentYear(query)
                case "Gender":
                    results = databaseModel.DatabaseManager.queryStudentGender(query)
                case _:
                    return redirect(url_for("student.index"))

        return render_template("students.html", results=results, query=query, searchForm=searchForm, editForm=editForm)
    else:
        return redirect(url_for("student.index"))
    
# CRUDL CONTROLLERS
# CRUDL CONTROLLERS
# CRUDL CONTROLLERS

@student_bp.route('/students/edit/', methods=['POST'])
def edit():
    courses = databaseModel.DatabaseManager.allCourses()
    editForm = EditForm()
    editForm.editCourse.choices = [(course[1], course[0]) for course in courses]
    if editForm.validate_on_submit():
        firstname = request.form.get('editFirstName')
        lastname = request.form.get('editLastName')
        newID = request.form.get('editID')
        year = request.form.get('editYear')
        gender = request.form.get('editGender')
        course = request.form.get('editCourse')
        oldID = request.form.get('student_id-edit')
        
        print(f"Student: {firstname}, {lastname}, {newID}, {year}, {gender}, {course}")
        databaseModel.DatabaseManager.editStudent(oldID, firstname, lastname, newID, year, gender, course)
        
        return redirect(url_for('student.index'))
    else:
        print(editForm.errors)
        flash(editForm.errors)
    return redirect(url_for('student.index'))

@student_bp.route('/students/delete/', methods=['POST'])
def delete():
    delete_item = request.form.get('student_id')
    print(f"Student to delete: {delete_item}")
    return redirect(url_for('student.index'))
    
@student_bp.route('/students/delete_checked/', methods=['POST'])
def delete_checked():
    # Get the list of checked items from the searchForm
    checked_items = request.form.getlist('items')
    
    # Print the checked items to the console (or do something else like delete them from the database)
    print(f"Checked items for deletion: {checked_items}")

    # Assuming you have a SQLAlchemy model to interact with the database
    # for item in checked_items:
        # Query the database and delete the item
        # Example (assuming item represents an ID):
        # MyModel.query.filter_by(id=item).delete()

    # Commit the changes to the database
    # db.session.commit()

    # Redirect back to the main page (or show a confirmation page)
    return redirect(url_for('student.index'))


# @student_bp.route('/students/search/<query>')
# def query(choices, query, searchForm):
#     return render_template('students.html', results=results, query=query, searchForm=searchForm, title='Query of Students')