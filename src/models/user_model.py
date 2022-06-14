from . import db, ma
from .address_model import Address, AddressSchema


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    user_name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    address = db.relationship('Address', backref='user', lazy=True)

    def __init__(self, user_name, age, address):
        self.user_name = user_name
        self.age = age
        self.address = address

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
    
    address = ma.Nested(AddressSchema, many=True)

