from ..faraday_agent_parameters_types import Type, TypeSchema
from marshmallow import fields, ValidationError, validates

NAME_TYPE_CLASS = "list"


class FaradayList(Type):
    def __init__(self, data=[]):
        """
        Type: Lista
        """
        Type.__init__(self, class_name=NAME_TYPE_CLASS)
        self.data = data
        self.value_dict = {"data": data}

    def __str__(self):
        return NAME_TYPE_CLASS


class FaradayListSchema(TypeSchema):
    data = fields.List(fields.Raw())
    _type = FaradayList
    _composed_list = []

    @validates("data")
    def validate_length_characters(self, items):
        for item in items:
            if not isinstance(item, self._composed_list):
                raise ValidationError("Item not valid in list")
