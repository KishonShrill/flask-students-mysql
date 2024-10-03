from flask import render_template, redirect, request, flash, url_for
from . import homepage_bp
import app.databaseModel as databaseModel
from app.forms import *


@homepage_bp.route('/')
def index():
    students = databaseModel.DatabaseManager.countStudents()
    programs = databaseModel.DatabaseManager.countPrograms()
    colleges = databaseModel.DatabaseManager.countColleges()
    return render_template('index.html', students=students, programs=programs, colleges=colleges)