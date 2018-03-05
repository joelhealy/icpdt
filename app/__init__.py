from flask import Flask

UPLOAD_FOLDER = 'c:/users/jhealy02/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from app import routes

