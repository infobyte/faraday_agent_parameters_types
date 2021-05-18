from ..faraday_agent_parameters_types import TypeSchema
from marshmallow import fields
from dataclasses import dataclass


@dataclass
class FaradayIP:
    data: str = str
    class_name: str = "ip"


class FaradayIPSchema(TypeSchema):
    data = fields.IP()
    _type = FaradayIP
