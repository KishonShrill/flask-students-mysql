from flask import render_template, redirect, request, jsonify
from . import college_bp
import app.databaseModel as databaseModel
# from app.user.forms import UserForm

@college_bp.route('/colleges')
def index():
    colleges = databaseModel.DatabaseManager.allCourses()
    return render_template('colleges.html', data=colleges, title='Current established colleges inside MSU-IIT')