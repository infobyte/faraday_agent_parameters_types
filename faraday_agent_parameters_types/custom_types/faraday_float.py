from ..faraday_agent_parameters_types import TypeSchema
from marshmallow import fields
from dataclasses import dataclass


@dataclass
class FaradayFloat:
    data: float = float
    class_name: str = "float"


class FaradayFloatSchema(TypeSchema):
    data = fields.Float()
    _type = FaradayFloat
