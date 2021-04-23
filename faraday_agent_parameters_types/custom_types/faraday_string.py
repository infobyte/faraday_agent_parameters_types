from ..faraday_agent_parameters_types import Type, TypeSchema
from marshmallow import fields, ValidationError, validates

NAME_TYPE_CLASS = "string"


class FaradayString(Type):
    def __init__(self, data: str = ""):
        """
        Type: Faraday String.
        """
        Type.__init__(self, class_name=NAME_TYPE_CLASS)
        self.data = data
        self.value_dict = {"data": data}


class FaradayStringSchema(TypeSchema):
    data = fields.String()
    _type = FaradayString

    @validates("data")
    def validate_length_characters(self, text):
        if len(text) > 256:
            raise ValidationError(f"Max length 256. Your text {len(text)}")
