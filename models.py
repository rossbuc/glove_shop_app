from app import db

class Glove(db.Model):
    __tablename__ = "gloves"
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.String(64))
    colour = db.Column(db.String(64))
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))


class Customer(db.Model):
    __tablename__ = "customers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    gloves = db.relationship("Glove", backref="customer")