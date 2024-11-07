import cloudinary
from flask import Flask
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY, BOOTSTRAP_SERVE_LOCAL
from config import CLOUD_NAME, API_KEY, API_SECRET

mysql = MySQL()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
        MYSQL_USER=DB_USERNAME,
        MYSQL_PASSWORD=DB_PASSWORD,
        MYSQL_DB=DB_NAME,
        MYSQL_HOST=DB_HOST,
        #BOOTSTRAP_SERVE_LOCAL=BOOTSTRAP_SERVE_LOCAL
    )

    # Set the max upload size to 25MB (in bytes)
    app.config['MAX_CONTENT_LENGTH'] = 25 * 1024 * 1024  # 25MB

    cloudinary.config(
        cloud_name=CLOUD_NAME,
        api_key=API_KEY,
        api_secret=API_SECRET,
        secure=True
    )

    mysql.init_app(app)
    CSRFProtect(app)

    from .home import homepage_bp as homepage_blueprint
    from .student import student_bp as student_blueprint
    from .programs import courses_bp as program_blueprint
    from .college import college_bp as colleges_blueprint
    app.register_blueprint(homepage_blueprint)
    app.register_blueprint(student_blueprint)
    app.register_blueprint(program_blueprint)
    app.register_blueprint(colleges_blueprint)

    return app