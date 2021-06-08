from typing import Union
from ..faraday_agent_parameters_types import TypeSchema
from marshmallow import fields
from dataclasses import dataclass, field
from ipaddress import IPv4Address, IPv6Address


@dataclass
class FaradayIP:
    data: Union[IPv4Address, IPv6Address] = IPv4Address("127.0.0.1")
    class_name: str = field(default="ip", init=False)
    base: str = field(default="string", init=False)


class FaradayIPSchema(TypeSchema):
    data = fields.IP()
    type = FaradayIP
