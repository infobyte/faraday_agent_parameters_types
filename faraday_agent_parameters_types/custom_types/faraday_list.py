from ..faraday_agent_parameters_types import Type, TypeSchema
from marshmallow import fields

NAME_TYPE_CLASS = "list"


class FaradayList(Type):
    def __init__(self, items=[]):
        """
        Type: Lista
        """
        Type.__init__(self, class_name=NAME_TYPE_CLASS)
        self.items = items

    def __str__(self):
        return NAME_TYPE_CLASS


class FaradayIntegerSchema(TypeSchema):
    items = fields.List()
    _type = FaradayList
