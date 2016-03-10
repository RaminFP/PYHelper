from marshmallow_sqlalchemy import ModelSchema

from sqla_model.Users import User
from example.main import session


class UserSchema(ModelSchema):

    class Meta:
        model = User
        sqla_session = session

