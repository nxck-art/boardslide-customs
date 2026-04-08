from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from models import db

class OrderItem(db.Model):
    __tablename__ = 'order_item'

    id = db.Column(db.Integer, primary_key = True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    prod_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.column(db.Integer)