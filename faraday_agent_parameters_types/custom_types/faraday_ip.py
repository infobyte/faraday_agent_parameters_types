from ..faraday_agent_parameters_types import Type, TypeSchema
from marshmallow import fields

NAME_TYPE_CLASS = "ip"


class FaradayIP(Type):
    def __init__(self, ip=""):
        """
        Type: ip
        """
        Type.__init__(self, class_name=NAME_TYPE_CLASS)
        self.ip = ip
        self.value_dict = {"ip": ip}

    def __str__(self):
        return NAME_TYPE_CLASS


class FaradayIPSchema(TypeSchema):
    ip = fields.IP()
    _type = FaradayIP
