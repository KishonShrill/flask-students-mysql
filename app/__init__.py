from flask import Flask
from flask_mysqldb import MySQL
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY, BOOTSTRAP_SERVE_LOCAL
from flask_wtf.csrf import CSRFProtect

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

    mysql.init_app(app)
    CSRFProtect(app)


    # @app.route('/')
    # def index():
    #     return "LETS DO THIS SHITTassdfasdf"

    from .student import student_bp as student_blueprint
    from .programs import courses_bp as program_blueprint
    from .college import college_bp as colleges_blueprint
    app.register_blueprint(student_blueprint)
    app.register_blueprint(program_blueprint)
    app.register_blueprint(colleges_blueprint)

    return app