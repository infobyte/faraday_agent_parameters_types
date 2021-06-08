from ..faraday_agent_parameters_types import TypeSchema
from marshmallow import fields, ValidationError
import re
from dataclasses import dataclass, field

regex = re.compile(r"^(\d+)-(\d+)$")


def validate_str(string):
    reg = re.match(regex, string)
    if not reg:
        raise ValidationError("Incorrect format, use: (integer)-(integer)")
    if int(reg.group(1)) > int(reg.group(2)):
        raise ValidationError("Range has to be in ascending order")
    return reg


def validate_list(_list):
    if all(isinstance(e, int) for e in _list):
        return True
    raise ValidationError("Only Integers allowed in the list")


class FaradayRangeField(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return ""
        if isinstance(value, str):
            return validate_str(value).group(0)
        if isinstance(value, list):
            validate_list(value)
            return f"{value[0]}-{value[-1]}"
        raise ValidationError("Invalid Data Type")

    def _deserialize(self, value, attr, data, **kwargs):
        if value is None:
            return []
        if isinstance(value, list):
            validate_list(value)
            return value
        if isinstance(value, str):
            reg = validate_str(value)
            return list(range(int(reg.group(1)), int(reg.group(2)) + 1))
        raise ValidationError("Invalid Data Type")


@dataclass
class FaradayRange:
    data: list = field(default_factory=list)
    class_name: str = field(default="range", init=False)
    base: str = field(default="string", init=False)


class FaradayRangeSchema(TypeSchema):
    data = FaradayRangeField()
    type = FaradayRange
