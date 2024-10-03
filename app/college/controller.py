from flask import render_template, redirect, request, flash, url_for
from . import college_bp
import app.databaseModel as databaseModel
import re as regex
from app.forms import *

@college_bp.route('/colleges')
@college_bp.route('/colleges/')
def index():
    searchForm = SearchForm()
    colleges = databaseModel.DatabaseManager.allColleges()
    return render_template('colleges.html', results=colleges, searchForm=searchForm)

@college_bp.route('/colleges/search', methods=['POST','GET'])
def search():
    searchForm = SearchForm()

    query = request.form.get('search') or request.args.get('q')
    print(f"Query: {query}")

    if query:
        results: str = ''

        results = databaseModel.DatabaseManager.queryCollege(query)

        print(results)
        print("Final Output")
        return render_template("colleges.html", results=results, query=query, searchForm=searchForm)
    else:
        print("Did I go here?")
        return redirect(url_for("colleges.index"))

# CREATE CONTROLLERS
# CREATE CONTROLLERS
# CREATE CONTROLLERS

@college_bp.route('/colleges/create/', methods=['POST','GET'])
def create():
    collegeForm = CollegeForm()
    return render_template('./crud_blueprint/college.html', form=collegeForm)

@college_bp.route('/colleges/create/submit', methods=['POST','GET'])
def createSubmit():
    if request.method == "POST":
        name_regex = regex.compile(r'^[A-Za-z\s]+$')
        code_regex = regex.compile(r'^[A-Z]+$')

        newCollegeName = request.form.get('collegeName')
        newCollegeCode = request.form.get('collegeCode')

        # Input validation
        if not newCollegeName or len(newCollegeName) < 3 or not name_regex.match(newCollegeName):
            flash("Invalid College Name: Only letters and spaces are allowed and must NOT be empty.", "warning")
            return redirect(url_for('colleges.create'))
        if not newCollegeCode or len(newCollegeCode) < 3 or not code_regex.match(newCollegeCode):
            flash("Invalid College Code: CAPITAL letters only and must NOT be empty.", "warning")
            return redirect(url_for('colleges.create'))
        
        isCollegeExist = databaseModel.DatabaseManager.createCollege(newCollegeName, newCollegeCode)

        if isCollegeExist == False:
            flash(f"College <{newCollegeName}> or {newCollegeCode} already exists!", "warning")
            return redirect(url_for('colleges.create'))
        else:
            flash(f"College {newCollegeCode} has been added successfully!", "success")
            return redirect(url_for('colleges.index'))
    
    if request.method == "GET":
        flash("You are not allowed to do that!", "danger")
        return redirect(url_for('colleges.index'))
    
# UPDATE CONTROLLERS
# UPDATE CONTROLLERS
# UPDATE CONTROLLERS

@college_bp.route('/colleges/edit/id=<college_id>', methods=['POST','GET'])
def edit(college_id):
    college_id = college_id or request.args.get('id')
    college = databaseModel.DatabaseManager.queryCollegeWithCode(college_id)

    if college:
        collegeForm = CollegeForm()

        collegeForm.collegeName.data = college[0][0]
        collegeForm.collegeCode.data = college[0][1]

        return render_template('./crud_blueprint/college.html', form=collegeForm, college_id=college_id)
    
    else:
        flash(f"College {college_id} does not exist!", "warning")
        return redirect(url_for('colleges.index'))
    
@college_bp.route('/colleges/edit/id=<college_id>/submit', methods=['POST','GET'])
def editSubmit(college_id):
    if request.method == "POST":
        name_regex = regex.compile(r'^[A-Za-z\s]+$')
        code_regex = regex.compile(r'^[A-Z]+$')

        oldCode = request.form.get('college_id-edit')
        newCollegeName = request.form.get('collegeName')
        newCollegeCode = request.form.get('collegeCode')

        # Input validation
        if not newCollegeName or len(newCollegeName) < 3 or len(newCollegeName) > 255 or not name_regex.match(newCollegeName):
            flash("Invalid College Name: Only letters and spaces are allowed and must NOT be empty.", "warning")
            return redirect(url_for('colleges.edit', college_id=college_id))
        if not newCollegeCode or len(newCollegeCode) < 3 or len(newCollegeCode) > 20 or not code_regex.match(newCollegeCode):
            flash("Invalid College Code: CAPITAL letters only are allowed and must NOT be empty.", "warning")
            return redirect(url_for('colleges.edit', college_id=college_id))
        
        isCommitSuccessful = databaseModel.DatabaseManager.editCollege(oldCode, newCollegeName, newCollegeCode)

        if isCommitSuccessful:
            flash(f"College {newCollegeCode} has been updated successfully!", "success")
            return redirect(url_for('colleges.index'))
        else:
            flash(f"College {newCollegeCode} has NOT updated successfully!", "warning")
            return redirect(url_for('colleges.index'))

    if request.method == "GET":
        flash("You can't illegally edit a record!", "danger")
        return redirect(url_for('colleges.index'))

# DELETE CONTROLLERS
# DELETE CONTROLLERS
# DELETE CONTROLLERS

@college_bp.route('/colleges/delete/', methods=['POST','GET'])
def delete():
    if request.method == "POST":
        delete_item = request.form.get('delete-chosen_id')
        print(f"College to delete: {delete_item}")

        databaseModel.DatabaseManager.deleteColleges(delete_item)

        flash(f"College {delete_item} has been deleted successfully!", "success")
        return redirect(url_for('colleges.index'))

    if request.method == "GET":
        flash("You can't illegally delete a record!", "danger")
        return redirect(url_for('colleges.index'))
        
@college_bp.route('/colleges/delete_checked/', methods=['POST','GET'])
def delete_checked():
    if request.method == "POST":
        checked_items = request.form.getlist('items')
    
        print(f"Checked items for deletion: {checked_items}")

        for program_id in checked_items:
            try:
                databaseModel.DatabaseManager.deleteColleges(program_id)
            except Exception as e:
                flash(f"Failed to delete college with ID: {program_id}", "danger")
                return redirect(url_for('colleges.index'))
            
        flash("Selected items are deleted!", "success")
        return redirect(url_for('colleges.index'))
    
    if request.method == "GET":
        flash("You are not allowed to do that!", "danger")
        return redirect(url_for('colleges.index'))