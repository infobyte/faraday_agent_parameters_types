from ..faraday_agent_parameters_types import TypeSchema
from marshmallow import fields
from dataclasses import dataclass


@dataclass
class FaradayInteger:
    data: int = int
    class_name: str = "integer"


class FaradayIntegerSchema(TypeSchema):
    data = fields.Integer()
    _type = FaradayInteger
