from flask import render_template, redirect, request, flash, url_for
from . import student_bp
import app.databaseModel as databaseModel
import re as regex
from app.forms import *
import os
import math

import cloudinary.api
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
from werkzeug.utils import secure_filename


@student_bp.route('/students')
@student_bp.route('/students/')
def index():
    searchForm = SearchForm()
    studentForm = StudentForm()
    
    # PAGINATION
    courses = databaseModel.DatabaseManager.allCourses()
    items_per_page = 14
    current_page  = int(request.args.get('page', 1))
    students, total_items = databaseModel.DatabaseManager.allStudents(current_page)
    total_pages = math.ceil(total_items / items_per_page)
    # PAGINATION
    
    searchForm.searchOption.choices = [('', 'Select a Course:')] + [(course[1], course[0]) for course in courses]
    studentForm.studentCourse.choices = [(course[1], course[0]) for course in courses]
    return render_template('students.html', results=students, searchForm=searchForm, studentForm=studentForm, total_pages=total_pages, current_page=current_page)

@student_bp.route('/students/search/sort=<choices>', methods=['POST','GET'])
def search(choices):
    searchForm = SearchForm()
    studentForm = StudentForm()
    courses = databaseModel.DatabaseManager.allCourses()
    
    items_per_page = 14
    choices = choices or request.args.get('sort')
    query = request.form.get('search') or request.args.get('q')
    course = request.form.get('searchOption') or request.args.get('course')
    current_page  = int(request.args.get('page', 1))
    global total_items, total_pages
    print(f"Choices: {choices} and Course: {course} and Query: {query}")

    searchForm.searchOption.choices = [('', 'Select a Course:')] + [(course[1], course[0]) for course in courses]
    studentForm.studentCourse.choices = [(course[1], course[0]) for course in courses]
    
    if query:
        results: str = ''

        if query and course:
            print("Have query and Course")
            match choices:
                case "firstname":
                    results, total_items = databaseModel.DatabaseManager.queryStudentFirstNameWithCourse(query,course,current_page)
                    total_pages = math.ceil(total_items / items_per_page)
                case "lastname":
                    results, total_items = databaseModel.DatabaseManager.queryStudentLastNameWithCourse(query,course,current_page)
                    total_pages = math.ceil(total_items / items_per_page)
                case "id":
                    results, total_items = databaseModel.DatabaseManager.queryStudentIDWithCourse(query,course,current_page)
                    total_pages = math.ceil(total_items / items_per_page)
                case "yearlevel":
                    results, total_items = databaseModel.DatabaseManager.queryStudentYearWithCourse(query,course,current_page)
                    total_pages = math.ceil(total_items / items_per_page)
                case "gender":
                    results, total_items = databaseModel.DatabaseManager.queryStudentGenderWithCourse(query,course,current_page)
                    total_pages = math.ceil(total_items / items_per_page)
                case _:
                    return redirect(url_for("student.index"))
                
        elif query and not course:
            print("Have query but no course")
            match choices:
                case "firstname":
                    results, total_items = databaseModel.DatabaseManager.queryStudentFirstName(query, current_page)
                    total_pages = math.ceil(total_items / items_per_page)
                case "lastname":
                    results, total_items = databaseModel.DatabaseManager.queryStudentLastName(query, current_page)
                    total_pages = math.ceil(total_items / items_per_page)
                case "id":
                    results, total_items = databaseModel.DatabaseManager.queryStudentWithID(query, current_page)
                    total_pages = math.ceil(total_items / items_per_page)
                case "yearlevel":
                    results, total_items = databaseModel.DatabaseManager.queryStudentYear(query, current_page)
                    total_pages = math.ceil(total_items / items_per_page)
                case "gender":
                    results, total_items = databaseModel.DatabaseManager.queryStudentGender(query, current_page)
                    total_pages = math.ceil(total_items / items_per_page)
                case _:
                    return redirect(url_for("student.index"))

        print(results)
        print("Final Output")
        return render_template("students.html", 
                               results=results, 
                               query=query, 
                               searchForm=searchForm, 
                               studentForm=studentForm, 
                               total_pages=total_pages, 
                               current_page=current_page,
                               choices=choices, course=course
                               )
    else:
        if course:
            results, total_items = databaseModel.DatabaseManager.queryStudentWithCourse(course, current_page)
            total_pages = math.ceil(total_items / items_per_page)
            return render_template("students.html", results=results, query=query, searchForm=searchForm, studentForm=studentForm, total_pages=total_pages, current_page=current_page, choices=choices, course=course)
        
        elif choices:
            results, total_items = databaseModel.DatabaseManager.sortBy(choices, current_page)
            total_pages = math.ceil(total_items / items_per_page)
            return render_template("students.html", results=results, query=query, searchForm=searchForm, studentForm=studentForm, total_pages=total_pages, current_page=current_page, choices=choices, course=course)
        else:
            return redirect(url_for("student.index"))

# CREATE CONTROLLERS
# CREATE CONTROLLERS
# CREATE CONTROLLERS

@student_bp.route('/students/create/', methods=['POST','GET'])
def create():
    studentForm = StudentForm()
    courses = databaseModel.DatabaseManager.allCourses()
    studentForm.studentCourse.choices = [(None, 'Not Enrolled')] + [(course[1], course[0]) for course in courses]
    return render_template('./crud_blueprint/student.html', form=studentForm)

@student_bp.route('/students/create/submit', methods=['POST','GET'])
def createSubmit():
    form = StudentForm()

    if request.method == "POST":
        name_regex = regex.compile(r'^[A-Za-z\s]+$')
        id_regex = regex.compile(r'^\d{4}-\d{4}$')

        newFirstName = request.form.get('studentFirstName')
        newLastName = request.form.get('studentLastName')
        newID = request.form.get('studentID')
        newYear = request.form.get('studentYear')
        newGender = request.form.get('studentGender')
        newCourse = request.form.get('studentCourse')

        # Save the profile picture file and initialize cloudinary_url
        cloudinary_url: str = ""
        profile_picture = form.studentUpload.data
        

        if profile_picture:
            # Secure the filename
            filename = secure_filename(profile_picture.filename)

            # Upload to Cloudinary
            try:
                filename = os.path.splitext(filename)[0]
                upload_result = cloudinary.uploader.upload(profile_picture, public_id=filename)
                cloudinary_url = upload_result.get('secure_url')  # Get the URL of the uploaded image

                # Modify the URL by inserting the transformation string
                transformation = "c_auto,g_auto,h_500,w_500"
                cloudinary_url = cloudinary_url.replace("/upload/", f"/upload/{transformation}/")
                
                # TODO: cloudinary_url into database
                print(f"cloudinary_url: {cloudinary_url}")

                flash(f"Profile picture uploaded successfully!", "success")
            except Exception as e:
                flash(f"An error occurred during file upload: {str(e)}", "danger")
                return redirect(url_for('student.create'))

        # Input validation
        if not newFirstName or len(newFirstName) < 2 or len(newFirstName) > 199 or not name_regex.match(newFirstName):
            flash("Invalid First Name: Only letters and spaces are allowed and must NOT be empty.", "warning")
            return redirect(url_for('student.create'))
        if not newLastName or len(newLastName) < 2 or len(newLastName) > 199 or not name_regex.match(newLastName):
            flash("Invalid Last Name: Only letters and spaces are allowed and must NOT be empty.", "warning")
            return redirect(url_for('student.create'))
        if not newID or len(newID) != 9:
            flash("ID is required and must be a 9-character ID.", "warning")
            return redirect(url_for('student.create'))
        if not id_regex.match(newID):
            flash("ID must match with pattern ####-####, e.g. 1234-5678", "warning")
            return redirect(url_for('student.create'))

        isStudentExist = databaseModel.DatabaseManager.createStudent(newFirstName, newLastName, newID, newYear, newGender, newCourse, cloudinary_url)

        if isStudentExist == False:
            flash(f"Student {newID} already exists!", "warning")
            return redirect(url_for('student.create'))
        else:
            flash(f"Student {newID} has been added successfully!", "success")
            return redirect(url_for('student.index'))
    
    if request.method == "GET":
        flash("You are not allowed to do that!", "danger")
        return redirect(url_for('student.index'))

# UPDATE CONTROLLERS
# UPDATE CONTROLLERS
# UPDATE CONTROLLERS

@student_bp.route('/students/edit/id=<student_id>', methods=['POST','GET'])
def edit(student_id):
    student_id = student_id or request.args.get('id')
    student, _ = databaseModel.DatabaseManager.queryStudentWithID(student_id)

    print(f"student: {student}")

    if student:
        studentForm = StudentForm()

        studentForm.studentFirstName.data = student[0][0]
        studentForm.studentLastName.data = student[0][1]
        studentForm.studentID.data = student[0][2]
        studentForm.studentYear.data = student[0][3] 
        studentForm.studentGender.data = student[0][4]
        courses = databaseModel.DatabaseManager.allCourses()
        studentForm.studentCourse.choices = [("None", 'Not Enrolled')] + [(course[1], course[0]) for course in courses]

        studentForm.studentCourse.data = student[0][5]
        profile_url = student[0][6]

        return render_template('./crud_blueprint/student.html', form=studentForm, student_id=student_id, profile_url=profile_url)
    
    else:
        flash(f"Student {student_id} does not exist!", "warning")
        return redirect(url_for('student.index'))

@student_bp.route('/students/edit/id=<student_id>/submit', methods=['POST','GET'])
def editSubmit(student_id):
    student_id = student_id or request.args.get('id')
    retrievedURL = databaseModel.DatabaseManager.queryStudentCloudinaryURL(student_id)
    old_cloudinary_url = retrievedURL[0][0]

    form = StudentForm()

    if request.method == "POST":
        name_regex = regex.compile(r'^[A-Za-z\s]+$')
        id_regex = regex.compile(r'^\d{4}-\d{4}$')

        oldID = request.form.get('student_id-edit')
        newFirstName = request.form.get('studentFirstName')
        newLastName = request.form.get('studentLastName')
        newID = request.form.get('studentID')
        newYear = request.form.get('studentYear')
        newGender = request.form.get('studentGender')
        newCourse = request.form.get('studentCourse')
        delete_profile_picture = request.form.get('deleteProfilePicture') == "true"

        # Save the profile picture file and initialize cloudinary_url
        cloudinary_url: str = ""
        profile_picture = form.studentUpload.data
        print(f"profile_picture: {profile_picture}")

        # Delete profile picture if the checkbox is selected
        if delete_profile_picture and old_cloudinary_url:
            # Extract the public_id from the URL and delete the image
            old_public_id = old_cloudinary_url.split('/')[-1]  # Get the filename
            old_public_id = '.'.join(old_public_id.split('.')[:-1])  # Remove the last extension
            try:
                cloudinary.api.delete_resources(old_public_id, resource_type="image", type="upload")
                print(f"Old image {old_public_id} deleted successfully.")
                cloudinary_url = "None"  # Clear URL to indicate no profile picture
                flash("Profile picture removed successfully.", "info")
            except Exception as delete_error:
                print(f"Error deleting old image: {str(delete_error)}")
                flash("An error occurred while trying to delete the profile picture.", "danger")

        if profile_picture:
            # Secure the filename
            allowed_extensions = {'png', 'jpg', 'webp'}  # Define allowed file extensions
            filename = secure_filename(profile_picture.filename)
            print(f"filename: {filename}") # TODO: Remove this later
            extension = filename.rsplit('.', 1)[-1].lower()  # Get the file extension

            # Check if the file extension is allowed
            if extension not in allowed_extensions:
                flash("Invalid file type! Please upload a PNG, JPG, or WEBP image.", "warning")
                return redirect(url_for('student.edit', student_id=student_id))
            
            # Check the size of the file (optional, you can specify your size limit)
            max_size = 25 * 1024 * 1024  # Example: 25MB
            if len(profile_picture.read()) > max_size:
                flash("File size exceeds the limit of 25MB.", "warning")
                return redirect(url_for('student.edit', student_id=student_id))
            
            profile_picture.seek(0)  # Reset file pointer after reading

            # Upload to Cloudinary
            try:
                filename = os.path.splitext(filename)[0]
                upload_result = cloudinary.uploader.upload(profile_picture, public_id=filename)
                cloudinary_url = upload_result.get('secure_url')  # Get the URL of the uploaded image

                # Modify the URL by inserting the transformation string
                transformation = "c_auto,g_auto,h_500,w_500"
                cloudinary_url = cloudinary_url.replace("/upload/", f"/upload/{transformation}/")
                
                # If the old and new Cloudinary URLs are different, delete the old image
                if old_cloudinary_url and old_cloudinary_url != cloudinary_url:
                    # Extract public_id from the old URL to delete it
                    old_public_id = old_cloudinary_url.split('/')[-1]  # Get the filename
                    old_public_id = '.'.join(old_public_id.split('.')[:-1])  # Remove the last extension

                    try:
                        cloudinary.api.delete_resources(old_public_id, resource_type="image", type="upload")
                        print(f"Old image {old_public_id} deleted successfully.")
                    except Exception as delete_error:
                        print(f"Error deleting old image: {str(delete_error)}")

                print(f"cloudinary_url: {cloudinary_url}")
                flash(f"Profile picture updated successfully!", "success")
            except Exception as e:
                flash(f"An error occurred during file upload: {str(e)}", "danger")
                return redirect(url_for('student.edit', student_id=student_id))

        # Input validation
        if not newFirstName or len(newFirstName) < 2 or len(newFirstName) > 199 or not name_regex.match(newFirstName):
            flash("Invalid First Name: Only letters and spaces are allowed and must NOT be empty.", "warning")
            return redirect(url_for('student.edit', student_id=student_id))
        if not newLastName or len(newLastName) < 2 or len(newLastName) > 199 or not name_regex.match(newLastName):
            flash("Invalid Last Name: Only letters and spaces are allowed and must NOT be empty.", "warning")
            return redirect(url_for('student.edit', student_id=student_id))
        if not newID or len(newID) != 9:
            flash("ID is required and must be a 9-character ID.", "warning")
            return redirect(url_for('student.edit', student_id=student_id))
        if not id_regex.match(newID):
            flash("ID must match with pattern ####-####, e.g. 1234-5678", "warning")
            return redirect(url_for('student.edit', student_id=student_id))

        isCommitSuccessful = databaseModel.DatabaseManager.editStudent(oldID, newFirstName, newLastName, newID, newYear, newGender, newCourse, cloudinary_url)

        if isCommitSuccessful:
            flash(f"Student {newID} has been updated successfully!", "success")
            return redirect(url_for('student.index'))
        else:
            flash(f"Student {newID} has NOT updated successfully!", "warning")
            return redirect(url_for('student.index'))
    
    if request.method == "GET":
        flash("You can't illegally edit a record!", "danger")
        return redirect(url_for('student.index'))
    
# DELETE CONTROLLERS
# DELETE CONTROLLERS
# DELETE CONTROLLERS

@student_bp.route('/students/delete/', methods=['POST','GET'])
def delete():
    if request.method == "POST":
        delete_item = request.form.get('delete-chosen_id')
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
    
        for student_id in checked_items:
            try:
                databaseModel.DatabaseManager.deleteStudent(student_id)
            except Exception as e:
                flash(f"Failed to delete student with ID: {student_id}", "danger")
                return redirect(url_for('student.index'))

        return redirect(url_for('student.index'))
    
    if request.method == "GET":
        flash("You are not allowed to do that!", "danger")
        return redirect(url_for('student.index'))