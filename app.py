import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


from model import *

@app.route('/')
@app.route('/index')
@app.route('/main')
def index():
    return render_template('index.html')


if __name__ == "__main__":
        app.run()