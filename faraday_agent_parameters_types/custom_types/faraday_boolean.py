from ..faraday_agent_parameters_types import Type, TypeSchema
from marshmallow import fields


NAME_TYPE_CLASS = "boolean"


class FaradayBoolean(Type):
    def __init__(self, data: bool = True):
        """
        Type: Faraday Boolean.
        """
        Type.__init__(self, class_name=NAME_TYPE_CLASS)
        self.data = data
        self.value_dict = {"data": data}


class FaradayBooleanSchema(TypeSchema):
    data = fields.Boolean()
    _type = FaradayBoolean
