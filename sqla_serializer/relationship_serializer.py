from marshmallow_sqlalchemy import ModelSchema
from sqla_model.self_relationship import self_reflation
from example.main import session


class RelationshipSchema(ModelSchema):

    class Meta:
        model = self_reflation
        sqla_session = session

