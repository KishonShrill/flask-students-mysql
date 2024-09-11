from flask import render_template, redirect, request, jsonify
from . import student_bp
import app.databaseModel as databaseModel
# from app.user.forms import UserForm


@student_bp.route('/students')
@student_bp.route('/')
def index():
    students = databaseModel.DatabaseManager.allStudents()
    return render_template('index.html', data=students, title='Homepage')