from sqlalchemy import SQLAlchemy

db = SQLAlchemy() #to import db

#order class
class Order(db.Model):
    __tablename__ = "Order" #dunder method that sets table name in db

    #define columns
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    cust_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    date = db.Column(db.String(40))
    total = db.Column(db.Float)