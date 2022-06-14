from . import db, ma


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class AddressSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Address
        load_instance = True
        include_fk = True