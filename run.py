# from flask import Flask
from app import create_app
from dotenv import load_dotenv

load_dotenv('.env')

app = create_app()

# @app.route('/')
# def index():
#     return "LETS DO THIS SHITT"

# if __name__ == "__main__":
#     app.run(debug=True)