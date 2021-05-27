import json
from faraday_agent_parameters_types.data_types import DATA_TYPE
from typing import Union, List, Any
from marshmallow import ValidationError
from faraday_agent_parameters_types.faraday_agent_parameters_types import TypeSchema
from pathlib import Path

manifests_folder = Path(__file__).parent / "static" / "manifests"


def get_schema(p_type: Union[str, TypeSchema]) -> TypeSchema:
    if isinstance(p_type, TypeSchema):
        return p_type
    if isinstance(p_type, str):
        if p_type in DATA_TYPE:
            return DATA_TYPE[p_type]
    raise ValidationError("Invalid Data Type")


def type_validate(p_type: Union[str, TypeSchema, List[Union[str, TypeSchema]]], data) -> dict:
    if isinstance(p_type, list):
        errors = {}
        for t in p_type:
            error = get_schema(t).validate({"data": data})
            if not error:
                return {}
            else:
                errors[t] = error
    else:
        errors = get_schema(p_type).validate({"data": data})
    return errors


def deserialize_param(p_type: Union[str, TypeSchema, List[Union[str, TypeSchema]]], data, get_obj=False) -> Any:
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


def serialize_param(p_type: Union[str, TypeSchema, List[Union[str, TypeSchema]]], data, get_dict=False) -> Any:
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


def get_manifests() -> dict:
    manifests_dict = {}
    for path in manifests_folder.iterdir():
        if path.is_file():
            with path.open() as file:
                manifests_dict[path.stem] = json.load(file)
    return manifests_dict
