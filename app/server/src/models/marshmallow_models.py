from server.src.models.marshmallow import ma

from server.src.models.models import User, Gender


class GenderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Gender
        fields = ["gender"]
        load_instance = True
        

class UserSchema(ma.SQLAlchemyAutoSchema):
    
    gender = ma.Nested(GenderSchema)
    
    class Meta:
        model = User
        load_instance = True
