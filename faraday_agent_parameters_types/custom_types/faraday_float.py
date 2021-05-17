from ..faraday_agent_parameters_types import Type, TypeSchema
from marshmallow import fields

NAME_TYPE_CLASS = "float"


class FaradayFloat(Type):
    def __init__(self, data=float):
        """
        Type: Float
        """
        Type.__init__(self, class_name=NAME_TYPE_CLASS)
        self.data = data
        self.value_dict = {"data": data}

    def __str__(self):
        return NAME_TYPE_CLASS


class FaradayFloatSchema(TypeSchema):
    data = fields.Float()
    _type = FaradayFloat
