from flask import Blueprint

courses_bp = Blueprint('programs',__name__)

from . import controller