from marshmallow import validate,fields
from app.model import User
from extensions.extersions import ma

class UserSchema(ma.SQLAlchemyAutoSchema):
    name = fields.String(required=True,validate=[validate.Length(min=2,max=20)])
    surname = fields.String(required=True,validate=[validate.Length(min=2,max=20)])
    password = fields.String(required=True,validate=[validate.Length(min=8,max=20)])
    
    class Meta:
        model = User
        load_instance = True

