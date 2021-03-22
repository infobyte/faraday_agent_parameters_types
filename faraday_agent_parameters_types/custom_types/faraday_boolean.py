from ..faraday_agent_parameters_types import Type, TypeSchema
from marshmallow import fields


NAME_TYPE_CLASS = "boolean"


class FaradayBoolean(Type):
    def __init__(self, option: 'Boolean Field' = True):
        """
        Type: Faraday Boolean.
        """
        Type.__init__(self, class_name=NAME_TYPE_CLASS)
        self.option = option


class FaradayBooleanSchema(TypeSchema):
    option = fields.Boolean()
    _type = FaradayBoolean
