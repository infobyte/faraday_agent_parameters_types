from faraday_agent_parameters_types.data_types import DATA_TYPE
from typing import Union
from marshmallow import Schema


def get_schema(p_type: Union[str, Schema]):
    if isinstance(p_type, Schema):
        return p_type
    if p_type not in DATA_TYPE:
        return [f"Invalid type: {p_type}"]
    return DATA_TYPE[p_type]


def type_validate(p_type: str, data):
    errors = get_schema(p_type).validate({"data": data})
    return errors


def deserialize_param(p_type: str, data):
    return get_schema(p_type).load({"data": data}).data


def serialize_param(p_type: str, data):
    return get_schema(p_type).dump({"data": data}).get("data")
