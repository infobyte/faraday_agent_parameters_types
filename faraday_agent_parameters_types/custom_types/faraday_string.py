from ..faraday_agent_parameters_types import TypeSchema
from marshmallow import fields, ValidationError, validates
from dataclasses import dataclass


@dataclass
class FaradayString:
    data: str = str
    class_name: str = "string"


class FaradayStringSchema(TypeSchema):
    data = fields.String()
    _type = FaradayString

    @validates("data")
    def validate_length_characters(self, text):
        if len(text) > 256:
            raise ValidationError(f"Max length 256. Your text {len(text)}")
