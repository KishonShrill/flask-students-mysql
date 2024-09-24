from flask import render_template, redirect, request, jsonify
from . import college_bp
import app.databaseModel as databaseModel
from app.forms import SearchForm

@college_bp.route('/colleges')
def index():
    searchForm = SearchForm()
    colleges = databaseModel.DatabaseManager.allCourses()
    return render_template('colleges.html', results=colleges, searchForm=searchForm)