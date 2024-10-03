from flask import Blueprint

college_bp = Blueprint('colleges',__name__)

from . import controller