from ..faraday_agent_parameters_types import Type, TypeSchema
from marshmallow import fields

NAME_TYPE_CLASS = "integer"


class FaradayInteger(Type):
    def __init__(self, data=0):
        """
        Type: Numero enero
        """
        Type.__init__(self, class_name=NAME_TYPE_CLASS)
        self.data = data
        self.value_dict = {"data": data}

    def __str__(self):
        return NAME_TYPE_CLASS


class FaradayIntegerSchema(TypeSchema):
    data = fields.Integer()
    _type = FaradayInteger
