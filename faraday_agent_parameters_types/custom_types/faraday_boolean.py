from ..faraday_agent_parameters_types import TypeSchema
from marshmallow import fields
from dataclasses import dataclass, field


@dataclass
class FaradayBoolean:
    data: bool = bool()
    class_name: str = field(default="boolean", init=False)
    base: str = field(default="boolean", init=False)


class FaradayBooleanSchema(TypeSchema):
    data = fields.Boolean()
    type = FaradayBoolean
