from flask import render_template, redirect, request, jsonify
from . import student_bp
import app.databaseModel as databaseModel
from app.forms import SearchForm


@student_bp.route('/')
@student_bp.route('/students')
def index():
    return render_template('index.html', title='Homepage')

@student_bp.route('/students/search', methods=['POST','GET'])
def search():
    form = SearchForm()
    if request.method == "POST":
        query = request.form['search']
        results = databaseModel.DatabaseManager.queryStudents(query)
        return render_template('index.html', results=results, query=query)