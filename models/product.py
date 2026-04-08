from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(30))
    category = db.Column(db.String(30))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)