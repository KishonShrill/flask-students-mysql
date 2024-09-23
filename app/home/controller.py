from flask import render_template, redirect, request, flash, url_for
from . import homepage_bp
import app.databaseModel as databaseModel
from app.forms import *


@homepage_bp.route('/')
def index():
    return render_template('index.html')