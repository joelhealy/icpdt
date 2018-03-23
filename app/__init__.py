from flask import Flask

UPLOAD_FOLDER = 'c:/users/jhealy02/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = b'\xaf\xec\\\xb6\xab\xbf\x9d\xc8an\x03\x04\x19q\x9d\nn\xf2\x91\x12,@\xa3\xed'

from app import routes

