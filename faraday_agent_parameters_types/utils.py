from faraday_agent_parameters_types.data_types import DATA_TYPE
from typing import Union
from marshmallow import Schema, ValidationError


def get_schema(p_type: Union[str, Schema]):
    if isinstance(p_type, Schema):
        return p_type
    if p_type not in DATA_TYPE:
        return [f"Invalid type: {p_type}"]
    return DATA_TYPE[p_type]


def type_validate(p_type: Union[str, list, Schema], data):
    if isinstance(p_type, list):
        errors = {}
        for t in p_type:
            error = get_schema(t).validate({"data": data})
            if not error:
                return False
            else:
                errors[t] = error
    else:
        errors = get_schema(p_type).validate({"data": data})
    return errors


def deserialize_param(p_type: Union[str, list, Schema], data, get_obj=False):
    v_type = p_type
    if isinstance(v_type, list):
        for t in v_type:
            error = get_schema(t).validate({"data": data})
            if not error:
                v_type = t
                break
        else:
            raise ValidationError("Could not validate with any of the possible types")
    obj = get_schema(v_type).load({"data": data})
    return obj if get_obj else obj.data


def serialize_param(p_type: Union[str, list, Schema], data, get_dict=False):
    v_type = p_type
    if isinstance(v_type, list):
        for t in v_type:
            error = get_schema(t).validate({"data": data})
            if not error:
                v_type = t
                break
        else:
            raise ValidationError("Could not validate with any of the possible types")
    r_dict = get_schema(v_type).dump({"data": data})
    return r_dict if get_dict else r_dict.get("data")
