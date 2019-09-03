from flask import Flask
from flask_app.main import main
app = Flask(__name__)

app.register_blueprint(main, url_prefix='/')
