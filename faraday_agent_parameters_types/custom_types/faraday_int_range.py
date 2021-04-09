from ..faraday_agent_parameters_types import Type, TypeSchema
from marshmallow import fields, ValidationError, validates
import re

NAME_TYPE_CLASS = "range"
regex = re.compile(r"^(\d+)-(\d+)$")


class FaradayRangeField(fields.Field):

    def _deserialize(self, value, attr, data, **kwargs):
        if value is None:
            return ""
        return f"{value[0]}-{value[-1]}"

    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return []
        reg = re.match(regex, value)
        if not reg:
            raise ValidationError("Incorrect format, use: (integer)-(integer)")
        if int(reg.group(1)) > int(reg.group(2)):
            raise ValidationError("Range has to be in ascending order")

        return list(range(int(reg.group(1)), int(reg.group(2)) + 1))


class FaradayRange(Type):
    def __init__(self, int_range=list):
        """
        Type: Range
        """
        Type.__init__(self, class_name=NAME_TYPE_CLASS)
        self.int_range = int_range

    def __str__(self):
        return NAME_TYPE_CLASS


class FaradayRangeSchema(TypeSchema):
    int_range = FaradayRangeField()
    _type = FaradayRange

