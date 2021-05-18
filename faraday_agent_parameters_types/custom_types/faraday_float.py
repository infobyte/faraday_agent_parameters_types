from ..faraday_agent_parameters_types import TypeSchema
from marshmallow import fields
from dataclasses import dataclass, field


@dataclass
class FaradayFloat:
    data: float = float()
    class_name: str = field(default="float", init=False)


class FaradayFloatSchema(TypeSchema):
    data = fields.Float()
    _type = FaradayFloat
