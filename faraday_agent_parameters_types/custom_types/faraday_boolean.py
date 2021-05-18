from ..faraday_agent_parameters_types import TypeSchema
from marshmallow import fields
from dataclasses import dataclass


@dataclass
class FaradayBoolean:
    data: bool = bool
    class_name: str = "boolean"


class FaradayBooleanSchema(TypeSchema):
    data = fields.Boolean()
    _type = FaradayBoolean
