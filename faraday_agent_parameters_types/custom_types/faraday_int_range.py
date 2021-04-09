from ..faraday_agent_parameters_types import Type, TypeSchema
from marshmallow import fields, ValidationError, validates
import re

NAME_TYPE_CLASS = "range"
regex = re.compile(r"^(\d+)-(\d+)$")


def get_range(string):
    reg = re.match(regex, string)
    return list(range(int(reg.group(1)), int(reg.group(2)) + 1)) if reg else None


class FaradayRange(Type):
    def __init__(self, str_range="", int_range: list = None):
        """
        Type: Range
        """
        Type.__init__(self, class_name=NAME_TYPE_CLASS)
        self.str_range = str_range
        self.int_range = int_range or get_range(self.str_range)

    def __str__(self):
        return NAME_TYPE_CLASS


class FaradayRangeSchema(TypeSchema):
    int_range = fields.List(fields.Integer())
    str_range = fields.String()
    _type = FaradayRange

    @validates('str_range')
    def validate_range_string(self, str_range):
        reg = re.match(regex, str_range)
        if not reg:
            raise ValidationError("Incorrect format, use: (integer)-(integer)")
        if int(reg.group(1)) > int(reg.group(2)):
            raise ValidationError("Range has to be in ascending order")


class FaradayRangeField(fields.Field):

    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return ""
        return f"{value[0]}-{value[len(value)]}"

    def _deserialize(self, value, attr, data, **kwargs):
        return get_range(value)
