from flask import render_template, redirect, request, flash, url_for
from . import student_bp
import app.databaseModel as databaseModel
import re as regex
from app.forms import *


@student_bp.route('/students')
@student_bp.route('/students/')
def index():
    searchForm = SearchForm()
    studentForm = StudentForm()
    courses = databaseModel.DatabaseManager.allCourses()
    students = databaseModel.DatabaseManager.allStudents()
    searchForm.searchCourse.choices = [('', 'Select a Course')] + [(course[1], course[0]) for course in courses]
    studentForm.studentCourse.choices = [(course[1], course[0]) for course in courses]
    return render_template('students.html', results=students, searchForm=searchForm, studentForm=studentForm)



@student_bp.route('/students/search/sort=<choices>', methods=['POST','GET'])
def search(choices):
    searchForm = SearchForm()
    studentForm = StudentForm()
    courses = databaseModel.DatabaseManager.allCourses()
    
    choices = choices or request.args.get('sort')
    query = request.form.get('search') or request.args.get('q')
    college = request.form.get('searchCourse') or request.args.get('college')
    print(f"Choices: {choices} and College: {college} and Query: {query}")

    searchForm.searchCourse.choices = [('', 'Select a Course')] + [(course[1], course[0]) for course in courses]
    studentForm.studentCourse.choices = [(course[1], course[0]) for course in courses]
    
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
        return render_template("students.html", results=results, query=query, searchForm=searchForm, studentForm=studentForm)
    else:
        if college:
            flash(f"Searching by {college}", "info")
            results = databaseModel.DatabaseManager.queryCollege(college)
            return render_template("students.html", results=results, query=query, searchForm=searchForm, studentForm=studentForm)
        
        elif choices:
            flash(f"Sorting by {choices}", "info")
            results = databaseModel.DatabaseManager.sortBy(choices)
            return render_template("students.html", results=results, query=query, searchForm=searchForm, studentForm=studentForm)
        else:
            print("Did I go here?")
            return redirect(url_for("student.index"))

# CRUDL CONTROLLERS
# CRUDL CONTROLLERS
# CRUDL CONTROLLERS

@student_bp.route('/students/create/', methods=['POST','GET'])
def create():
    studentForm = StudentForm()
    courses = databaseModel.DatabaseManager.allCourses()
    studentForm.studentCourse.choices = [(None, 'Not Enrolled')] + [(course[1], course[0]) for course in courses]

    return render_template('./crud_blueprint/createStudent.html', studentForm=studentForm)

@student_bp.route('/students/create/submit', methods=['POST','GET'])
def createSubmit():
    if request.method == "POST":
        newFirstName = request.form.get('studentFirstName')
        newLastName = request.form.get('studentLastName')
        newID = request.form.get('studentID')
        newYear = request.form.get('studentYear')
        newGender = request.form.get('studentGender')
        newCourse = request.form.get('studentCourse')

        # Input validation
        if not newFirstName or len(newFirstName) < 2:
            flash("Invalid First Name: Only letters and spaces are allowed and must NOT be empty.", "warning")
            return redirect(url_for('student.create'))

        if not newLastName or len(newLastName) < 2:
            flash("Invalid Last Name: Only letters and spaces are allowed and must NOT be empty.", "warning")
            return redirect(url_for('student.create'))

        if not newID or len(newID) != 9:
            flash("ID is required and must be a 9-character ID.", "warning")
            return redirect(url_for('student.create'))

        isStudentExist = databaseModel.DatabaseManager.createStudent(newFirstName, newLastName, newID, newYear, newGender, newCourse)

        if isStudentExist == False:
            flash(f"Student {newID} already exists!", "warning")
            return redirect(url_for('student.create'))
        else:
            flash(f"Student {newID} has been added successfully!", "success")
            return redirect(url_for('student.index'))
    
    if request.method == "GET":
        flash("You are not allowed to do that!", "danger")
        return redirect(url_for('student.index'))



@student_bp.route('/students/edit/id=<student_id>', methods=['POST','GET'])
def edit(student_id):
    student_id = student_id or request.args.get('id')
    student = databaseModel.DatabaseManager.queryStudentID(student_id)
    print(student)
    if student:
        studentForm = StudentForm()

        studentForm.studentFirstName.data = student[0][0]  # Assuming student[0] is the first name
        studentForm.studentLastName.data = student[0][1]   # Assuming student[1] is the last name
        studentForm.studentID.data = student[0][2]         # Assuming student[2] is the ID
        studentForm.studentYear.data = student[0][3]       # Assuming student[3] is the year level
        studentForm.studentGender.data = student[0][4]     # Assuming student[4] is the gender

        courses = databaseModel.DatabaseManager.allCourses()
        studentForm.studentCourse.choices = [("None", 'Not Enrolled')] + [(course[1], course[0]) for course in courses]

        studentForm.studentCourse.data = student[0][5]  # Assuming student[5] is the current course code

        return render_template('./crud_blueprint/editStudent.html', studentForm=studentForm, student_id=student_id)
    
    else:
        flash(f"Student {student_id} does not exist!", "warning")
        return redirect(url_for('student.index'))

@student_bp.route('/students/edit/id=<student_id>/submit', methods=['POST','GET'])
def editSubmit(student_id):
    if request.method == "POST":
        name_regex = regex.compile(r'^[A-Za-z\s]+$')

        oldID = request.form.get('student_id-edit')
        newFirstName = request.form.get('studentFirstName')
        newLastName = request.form.get('studentLastName')
        newID = request.form.get('studentID')
        newYear = request.form.get('studentYear')
        newGender = request.form.get('studentGender')
        newCourse = request.form.get('studentCourse')

        # Input validation
        if not newFirstName or len(newFirstName) < 2 or not name_regex.match(newFirstName):
            flash("Invalid First Name: Only letters and spaces are allowed and must NOT be empty.", "warning")
            return redirect(url_for('student.edit', student_id=student_id))

        if not newLastName or len(newLastName) < 2 or not name_regex.match(newLastName):
            flash("Invalid Last Name: Only letters and spaces are allowed and must NOT be empty.", "warning")
            return redirect(url_for('student.edit', student_id=student_id))

        if not newID or len(newID) != 9:
            flash("ID is required and must be a 9-character ID.", "warning")
            return redirect(url_for('student.edit', student_id=student_id))

        isCommitSuccessful = databaseModel.DatabaseManager.editStudent(oldID, newFirstName, newLastName, newID, newYear, newGender, newCourse)

        if isCommitSuccessful:
            flash(f"Student {newID} has been updated successfully!", "success")
            return redirect(url_for('student.index'))
        else:
            flash(f"Student {newID} has NOT updated successfully!", "warning")
            return redirect(url_for('student.index'))
    
    if request.method == "GET":
        flash("You can't illegally edit a record!", "danger")
        return redirect(url_for('student.index'))
    


@student_bp.route('/students/delete/', methods=['POST','GET'])
def delete():
    if request.method == "POST":
        delete_item = request.form.get('student_id-delete')
        print(f"Student to delete: {delete_item}")

        databaseModel.DatabaseManager.deleteStudent(delete_item)

        flash(f"Student {delete_item} has been deleted successfully!", "success")
        return redirect(url_for('student.index'))

    if request.method == "GET":
        flash("You can't illegally delete a record!", "danger")
        return redirect(url_for('student.index'))
    
@student_bp.route('/students/delete_checked/', methods=['POST','GET'])
def delete_checked():
    if request.method == "POST":
        checked_items = request.form.getlist('items')
    
        # Print the checked items to the console (or do something else like delete them from the database)
        print(f"Checked items for deletion: {checked_items}")

        # Loop through each checked item and delete the corresponding student from the database
        for student_id in checked_items:
            try:
                databaseModel.DatabaseManager.deleteStudent(student_id)
                print(f"Deleted student with ID: {student_id}")
            except Exception as e:
                print(f"Error deleting student with ID: {student_id} - {e}")
                flash(f"Failed to delete student with ID: {student_id}", "danger")
                return redirect(url_for('student.index'))

        # Redirect back to the main page (or show a confirmation page)
        return redirect(url_for('student.index'))
    
    if request.method == "GET":
        flash("You are not allowed to do that!", "danger")
        return redirect(url_for('student.index'))