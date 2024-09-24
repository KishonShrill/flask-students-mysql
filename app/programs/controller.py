from flask import render_template, redirect, request, jsonify
from . import courses_bp
import app.databaseModel as databaseModel
from app.forms import SearchForm


@courses_bp.route('/programs')
def index():
    searchForm = SearchForm()
    courses = databaseModel.DatabaseManager.allCourses()
    colleges = databaseModel.DatabaseManager.allColleges()
    searchForm.searchCollege.choices = [('', 'Select a College')] + [(college[1], college[0]) for college in colleges]
    return render_template('programs.html', results=courses, searchForm=searchForm, title='Available courses from all colleges')