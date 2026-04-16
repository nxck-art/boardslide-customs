from flask_sqlalchemy import SQLAlchemy
from models import db

class Customer(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(30))
    lname = db.Column(db.String(30))
    email = db.Column(db.String(30))
    phone = db.Column(db.String(30))