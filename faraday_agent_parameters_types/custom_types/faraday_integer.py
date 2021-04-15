from ..faraday_agent_parameters_types import Type, TypeSchema
from marshmallow import fields

NAME_TYPE_CLASS = "integer"


class FaradayInteger(Type):
    def __init__(self, number=0):
        """
        Type: Numero enero
        """
        Type.__init__(self, class_name=NAME_TYPE_CLASS)
        self.number = number
        self.value_dict = {"number": number}

    def __str__(self):
        return NAME_TYPE_CLASS


class FaradayIntegerSchema(TypeSchema):
    number = fields.Integer()
    _type = FaradayInteger
