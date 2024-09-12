from flask import render_template, redirect, request, jsonify
from . import courses_bp
import app.databaseModel as databaseModel
# from app.user.forms import UserForm

@courses_bp.route('/programs')
def index():
    courses = databaseModel.DatabaseManager.allCourses()
    return render_template('programs.html', data=courses, title='Available courses from all colleges')