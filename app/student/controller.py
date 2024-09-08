from flask import render_template, redirect, request, jsonify
from . import student_bp
import app.models as models
# from app.user.forms import UserForm


@student_bp.route('/students')
@student_bp.route('/')
def index():
    students = models.Students.all()
    return render_template('index.html', data=students, title='Homepage')