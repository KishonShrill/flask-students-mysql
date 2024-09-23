from flask import render_template, redirect, request, flash, url_for
from . import student_bp
import app.databaseModel as databaseModel
from app.forms import *


@student_bp.route('/students')
@student_bp.route('/students/')
def index():
    searchForm = SearchForm()
    studentForm = StudentForm()
    courses = databaseModel.DatabaseManager.allCourses()
    students = databaseModel.DatabaseManager.allStudents()
    searchForm.searchCollege.choices = [('', 'Select a Course')] + [(course[1], course[0]) for course in courses]
    studentForm.studentCourse.choices = [(course[1], course[0]) for course in courses]
    return render_template('students.html', results=students, searchForm=searchForm, studentForm=studentForm, title='List of Students')



@student_bp.route('/students/search/sort=<choices>', methods=['POST','GET'])
def search(choices):
    searchForm = SearchForm()
    studentForm = StudentForm()
    courses = databaseModel.DatabaseManager.allCourses()
    
    choices = choices or request.args.get('sort')
    query = request.form.get('search') or request.args.get('q')
    college = request.form.get('searchCollege') or request.args.get('college')
    print(f"Choices: {choices} and College: {college} and Query: {query}")

    searchForm.searchCollege.choices = [('', 'Select a Course')] + [(course[1], course[0]) for course in courses]
    studentForm.editCourse.choices = [(course[1], course[0]) for course in courses]
    
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
            print("No query but have college")
            results = databaseModel.DatabaseManager.queryCollege(college)
            return render_template("students.html", results=results, query=query, searchForm=searchForm, studentForm=studentForm)
        print("Did I go here?")
        return redirect(url_for("student.index"))

# CRUDL CONTROLLERS
# CRUDL CONTROLLERS
# CRUDL CONTROLLERS

@student_bp.route('/students/create/', methods=['POST'])
def create():
    studentForm = StudentForm()
    courses = databaseModel.DatabaseManager.allCourses()
    studentForm.studentCourse.choices = [(None, 'Not Enrolled')] + [(course[1], course[0]) for course in courses]

    return render_template('./crud_blueprint/createStudent.html', studentForm=studentForm)

@student_bp.route('/students/create/submit', methods=['POST','GET'])
def createSubmit(student_id):
    if request.method == "POST":
        newFirstName = request.form.get('studentFirstName')
        newLastName = request.form.get('studentLastName')
        newID = request.form.get('studentID')
        newYear = request.form.get('studentYear')
        newGender = request.form.get('studentGender')
        newCourse = request.form.get('studentCourse')

        print(f"FirstName: {newFirstName}, LastName: {newLastName}, newID: {newID}, Year: {newYear}, Gender: {newGender}, Course: {newCourse}")
        databaseModel.DatabaseManager.editStudent(newFirstName, newLastName, newID, newYear, newGender, newCourse)

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
        return redirect(url_for('student.index'))

@student_bp.route('/students/edit/id=<student_id>/submit', methods=['POST','GET'])
def editSubmit(student_id):
    if request.method == "POST":

        oldID = request.form.get('student_id-edit')
        newFirstName = request.form.get('studentFirstName')
        newLastName = request.form.get('studentLastName')
        newID = request.form.get('studentID')
        newYear = request.form.get('studentYear')
        newGender = request.form.get('studentGender')
        newCourse = request.form.get('studentCourse')

        print(f"Old Student ID: {oldID}, FirstName: {newFirstName}, LastName: {newLastName}, newID: {newID}, Year: {newYear}, Gender: {newGender}, Course: {newCourse}")
        isCommitSuccessful = databaseModel.DatabaseManager.editStudent(oldID, newFirstName, newLastName, newID, newYear, newGender, newCourse)

        if isCommitSuccessful:
            flash(f"Student {newID} has been updated successfully!", "success")
            return redirect(url_for('student.index'))
        else:
            flash(f"Student {newID} has NOT updated successfully!", "warning")
            return redirect(url_for('student.index'))
    
    if request.method == "GET":
        flash("You are not allowed to do that!", "danger")
        return redirect(url_for('student.index'))
    


@student_bp.route('/students/delete/', methods=['POST','GET'])
def delete():
    if request.method == "POST":
        delete_item = request.form.get('student_id-delete')
        print(f"Student to delete: {delete_item}")

        # TODO: Database Delete Method

        flash(f"Student {delete_item} has been deleted successfully!", "success")
        return redirect(url_for('student.index'))

    if request.method == "GET":
            flash("You are not allowed to do that!", "danger")
            return redirect(url_for('student.index'))
    
@student_bp.route('/students/delete_checked/', methods=['POST','GET'])
def delete_checked():
    if request.method == "POST":
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
    
    if request.method == "GET":
        flash("You are not allowed to do that!", "danger")
        return redirect(url_for('student.index'))