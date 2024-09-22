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
    searchForm.searchCollege.choices = [('', 'Select a Course')] + [(course[1], course[0]) for course in courses]
    editForm.editCourse.choices = [(course[1], course[0]) for course in courses]
    return render_template('students.html', results=students, searchForm=searchForm, editForm=editForm, title='List of Students')



@student_bp.route('/students/search/sort=<choices>', methods=['POST','GET'])
def search(choices):
    searchForm = SearchForm()
    editForm = EditForm()
    courses = databaseModel.DatabaseManager.allCourses()
    
    choices = choices or request.args.get('sort')
    query = request.form.get('search') or request.args.get('q')
    college = request.form.get('searchCollege') or request.args.get('college')
    print(f"Choices: {choices} and College: {college} and Query: {query}")

    searchForm.searchCollege.choices = [('', 'Select a Course')] + [(course[1], course[0]) for course in courses]
    editForm.editCourse.choices = [(course[1], course[0]) for course in courses]
    
    if query:
        results: str = ''

        if query and college:
            print("Have query and College")
            match choices:
                case "firstname":
                    results = databaseModel.DatabaseManager.queryStudentFirstNameWithCollege(query,college)
                case "lastname":
                    results = databaseModel.DatabaseManager.queryStudentLastNameWithCollege(query,college)
                case "id":
                    results = databaseModel.DatabaseManager.queryStudentIDWithCollege(query,college)
                case "yearlevel":
                    results = databaseModel.DatabaseManager.queryStudentYearWithCollege(query,college)
                case "gender":
                    results = databaseModel.DatabaseManager.queryStudentGenderWithCollege(query,college)
                case _:
                    return redirect(url_for("student.index"))
                
        elif query and not college:
            print("Have query but no college")
            match choices:
                case "firstname":
                    results = databaseModel.DatabaseManager.queryStudentFirstName(query)
                case "lastname":
                    results = databaseModel.DatabaseManager.queryStudentLastName(query)
                case "id":
                    results = databaseModel.DatabaseManager.queryStudentID(query)
                case "yearlevel":
                    results = databaseModel.DatabaseManager.queryStudentYear(query)
                case "gender":
                    results = databaseModel.DatabaseManager.queryStudentGender(query)
                case _:
                    return redirect(url_for("student.index"))

        print(results)
        print("Final Output")
        return render_template("students.html", results=results, query=query, searchForm=searchForm, editForm=editForm)
    else:
        if college:
            print("No query but have college")
            results = databaseModel.DatabaseManager.queryCollege(college)
            return render_template("students.html", results=results, query=query, searchForm=searchForm, editForm=editForm)
        print("Did I go here?")
        return redirect(url_for("student.index"))

# @student_bp.route('/students/practice/', methods=['POST','GET'])
# def practice():
#     name = request.args.get('name')
#     age = request.args.get('age')
#     return f'Hello, {name}! You are {age} years old.'


# CRUDL CONTROLLERS
# CRUDL CONTROLLERS
# CRUDL CONTROLLERS

@student_bp.route('/students/edit/<student_id>', methods=['POST'])
def edit(student_id):
    student = databaseModel.DatabaseManager.queryStudentID(student_id)
    print(student)
    if student:
        editForm = EditForm()

        editForm.editFirstName.data = student[0][0]  # Assuming student[0] is the first name
        editForm.editLastName.data = student[0][1]   # Assuming student[1] is the last name
        editForm.editID.data = student[0][2]         # Assuming student[2] is the ID
        editForm.editYear.data = student[0][3]       # Assuming student[3] is the year level
        editForm.editGender.data = student[0][4]     # Assuming student[4] is the gender

        courses = databaseModel.DatabaseManager.allCourses()
        editForm.editCourse.choices = [(course[1], course[0]) for course in courses]

        editForm.editCourse.data = student[0][5]  # Assuming student[5] is the current course code

        return render_template('./crud_blueprint/editStudent.html', editForm=editForm)
    
    else:
        return redirect(url_for('student.index'))

@student_bp.route('/students/edit/<student_id>/submit', methods=['POST'])
def editSubmit(student_id):
    if request.method == "POST":
        ...







@student_bp.route('/students/delete/', methods=['POST'])
def delete():
    delete_item = request.form.get('student_id-delete')
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