#app

#imports
from flask import Flask, render_template
from product import db

#init database
app = Flask(__name__)
app.config['SQLALCHEMY_DB'] = 'sqlite:///database.db'

db.init_app(app)

with app.app_context():
    db.create_all()