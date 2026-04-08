from models import db

class Skateboard(db.Model):
    __tablename__ = "skateboard"

    #columns
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))

    #customizables (still columns)
    deck_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    wheels_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    bearing_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    trucks_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    griptape_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    design_id = db.Column(db.Integer, db.ForeignKey('product.id'))

    #more columns
    total = db.Column(db.Float)

    #foreign keys
    deck = db.relationship('Product', foreign_keys=[deck_id])
    wheels = db.relationship('Product', foreign_keys=[wheels_id])
    bearing = db.relationship('Product', foreign_keys=[bearing_id])
    trucks = db.relationship('Product', foreign_keys=[trucks_id])
    griptape = db.relationship('Product', foreign_keys=[griptape_id])
    design = db.relationship('Product', foreign_keys=[design_id])