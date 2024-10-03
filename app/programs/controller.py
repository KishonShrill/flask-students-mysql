from flask import render_template, redirect, request, flash, url_for
from . import courses_bp
import app.databaseModel as databaseModel
import re as regex
from app.forms import *


@courses_bp.route('/programs')
@courses_bp.route('/programs/')
def index():
    searchForm = SearchForm()
    programForm = ProgramForm()
    courses = databaseModel.DatabaseManager.allCourses()
    colleges = databaseModel.DatabaseManager.allColleges()
    searchForm.searchOption.choices = [('', 'Select a College')] + [(college[1], college[0]) for college in colleges]
    return render_template('programs.html', results=courses, searchForm=searchForm, programForm=programForm)

@courses_bp.route('/programs/search', methods=['POST','GET'])
def search():
    searchForm = SearchForm()
    programForm = ProgramForm()
    colleges = databaseModel.DatabaseManager.allColleges()

    query = request.form.get('search') or request.args.get('q')
    college = request.form.get('searchCourse') or request.args.get('college')
    print(f"College: {college} and Query: {query}")

    searchForm.searchOption.choices = [('', 'Select a College')] + [(college[1], college[0]) for college in colleges]

    if query:
        results: str = ''

        if query and college:
            print("Course with College")
            results = databaseModel.DatabaseManager.queryCourseWithCollege(query,college)
        elif query and not college:
            print("Course with no College")
            results = databaseModel.DatabaseManager.queryCourseWithNoCollege(query)

        print(results)
        print("Final Output")
        return render_template("programs.html", results=results, query=query, searchForm=searchForm, programForm=programForm)
    else:
        if college:
            flash(f"Searching by {college}", "info")
            results = databaseModel.DatabaseManager.queryCourse(college)
            return render_template("programs.html", results=results, query=query, searchForm=searchForm, programForm=programForm)
        else:
            print("Did I go here?")
            return redirect(url_for("programs.index"))

# CREATE CONTROLLERS
# CREATE CONTROLLERS
# CREATE CONTROLLERS

@courses_bp.route('/programs/create/', methods=['POST','GET'])
def create():
    programForm = ProgramForm()
    colleges = databaseModel.DatabaseManager.allColleges()
    programForm.programCollege.choices = [(college[1], college[0]) for college in colleges]
    return render_template('./crud_blueprint/program.html', form=programForm)

@courses_bp.route('/programs/create/submit', methods=['POST','GET'])
def createSubmit():
    if request.method == "POST":
        name_regex = regex.compile(r'^[A-Za-z\s]+$')
        code_regex = regex.compile(r'^[A-Za-z]+$')

        newProgramName = request.form.get('programName')
        newProgramCode = request.form.get('programCode')
        newProgramCollege = request.form.get('programCollege')

        # Input validation
        if not newProgramName or len(newProgramName) < 3 or not name_regex.match(newProgramName):
            flash("Invalid Program Name: Only letters and spaces are allowed and must NOT be empty.", "warning")
            return redirect(url_for('programs.create'))
        if not newProgramCode or len(newProgramCode) < 3 or not code_regex.match(newProgramCode):
            flash("Invalid Program Code: Only letters are allowed and must NOT be empty.", "warning")
            return redirect(url_for('programs.create'))
        
        isCourseExist = databaseModel.DatabaseManager.createProgram(newProgramName, newProgramCode, newProgramCollege)

        if isCourseExist == False:
            flash(f"Program {newProgramCode} already exists!", "warning")
            return redirect(url_for('programs.create'))
        else:
            flash(f"Program {newProgramCode} has been added successfully!", "success")
            return redirect(url_for('programs.index'))
    
    if request.method == "GET":
        flash("You are not allowed to do that!", "danger")
        return redirect(url_for('student.index'))

# UPDATE CONTROLLERS
# UPDATE CONTROLLERS
# UPDATE CONTROLLERS

@courses_bp.route('/programs/edit/id=<program_id>', methods=['POST','GET'])
def edit(program_id):
    program_id = program_id or request.args.get('id')
    program = databaseModel.DatabaseManager.queryCourseWithCode(program_id)

    if program:
        programForm = ProgramForm()

        programForm.programName.data = program[0][0]
        programForm.programCode.data = program[0][1]

        courses = databaseModel.DatabaseManager.allColleges()
        programForm.programCollege.choices = [(course[1], course[0]) for course in courses]
        programForm.programCollege.data = program[0][2]

        return render_template('./crud_blueprint/program.html', form=programForm, program_id=program_id)
    
    else:
        flash(f"Program {program_id} does not exist!", "warning")
        return redirect(url_for('programs.index'))
    
@courses_bp.route('/programs/edit/id=<program_id>/submit', methods=['POST','GET'])
def editSubmit(program_id):
    if request.method == "POST":
        name_regex = regex.compile(r'^[A-Za-z\s]+$')
        code_regex = regex.compile(r'^[A-Za-z]+$')

        oldCode = request.form.get('course_id-edit')
        newProgramName = request.form.get('programName')
        newProgramCode = request.form.get('programCode')
        newProgramCollege = request.form.get('programCollege')

        # Input validation
        if not newProgramName or len(newProgramName) < 3 or len(newProgramName) > 255 or not name_regex.match(newProgramName):
            flash("Invalid Program Name: Only letters and spaces are allowed and must NOT be empty.", "warning")
            return redirect(url_for('programs.edit', program_id=program_id))
        if not newProgramCode or len(newProgramCode) < 3 or len(newProgramCode) > 20 or not code_regex.match(newProgramCode):
            flash("Invalid Program Code: CAPITAL letters only are allowed and must NOT be empty.", "warning")
            return redirect(url_for('programs.edit', program_id=program_id))
        
        isCommitSuccessful = databaseModel.DatabaseManager.editProgram(oldCode, newProgramName, newProgramCode, newProgramCollege)

        if isCommitSuccessful:
            flash(f"Program {newProgramCode} has been updated successfully!", "success")
            return redirect(url_for('programs.index'))
        else:
            flash(f"Program {newProgramCode} has NOT updated successfully!", "warning")
            return redirect(url_for('programs.index'))

    if request.method == "GET":
        flash("You can't illegally edit a record!", "danger")
        return redirect(url_for('programs.index'))

# DELETE CONTROLLERS
# DELETE CONTROLLERS
# DELETE CONTROLLERS

@courses_bp.route('/programs/delete/', methods=['POST','GET'])
def delete():
    if request.method == "POST":
        delete_item = request.form.get('delete-chosen_id')
        print(f"Program to delete: {delete_item}")

        databaseModel.DatabaseManager.deleteProgram(delete_item)

        flash(f"Program {delete_item} has been deleted successfully!", "success")
        return redirect(url_for('programs.index'))

    if request.method == "GET":
        flash("You can't illegally delete a record!", "danger")
        return redirect(url_for('programs.index'))
    
@courses_bp.route('/programs/delete_checked/', methods=['POST','GET'])
def delete_checked():
    if request.method == "POST":
        checked_items = request.form.getlist('items')
    
        print(f"Checked items for deletion: {checked_items}")

        for program_id in checked_items:
            try:
                databaseModel.DatabaseManager.deleteProgram(program_id)
            except Exception as e:
                flash(f"Failed to delete program with ID: {program_id}", "danger")
                return redirect(url_for('programs.index'))
            
        flash("Selected items are deleted!", "success")
        return redirect(url_for('programs.index'))
    
    if request.method == "GET":
        flash("You are not allowed to do that!", "danger")
        return redirect(url_for('programs.index'))