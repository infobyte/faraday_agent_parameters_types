from ..faraday_agent_parameters_types import TypeSchema
from marshmallow import fields, ValidationError, validates
from dataclasses import dataclass, field


@dataclass
class FaradayString:
    data: str = str()
    class_name: str = field(default="string", init=False)
    base: str = field(default="string", init=False)


class FaradayStringSchema(TypeSchema):
    data = fields.String()
    type = FaradayString

    @validates("data")
    def validate_length_characters(self, text):
        if len(text) > 256:
            raise ValidationError(f"Max length 256. Your text {len(text)}")
