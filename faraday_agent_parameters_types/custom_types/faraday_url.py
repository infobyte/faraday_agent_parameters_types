from ..faraday_agent_parameters_types import TypeSchema
from marshmallow import fields
from dataclasses import dataclass, field


@dataclass
class FaradayUrl:
    data: str = str()
    class_name: str = field(default="url", init=False)
    base: str = field(default="string", init=False)


class FaradayUrlSchema(TypeSchema):
    data = fields.Url()
    type = FaradayUrl
