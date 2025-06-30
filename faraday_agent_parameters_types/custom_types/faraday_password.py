from ..faraday_agent_parameters_types import TypeSchema
from marshmallow import fields, ValidationError, validates
from dataclasses import dataclass, field


@dataclass
class FaradayPassword:
    data: str = str()
    class_name: str = field(default="password", init=False)
    base: str = field(default="string", init=False)


class FaradayPasswordSchema(TypeSchema):
    data = fields.String()
    type = FaradayPassword

    @validates("data")
    def validate_data(self, text):
        if len(text) > 256:
            raise ValidationError("Max length 256")
