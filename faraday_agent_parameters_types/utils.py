import json
from functools import lru_cache

from faraday_agent_parameters_types.data_types import DATA_TYPE
from typing import Union, List, Any
from marshmallow import ValidationError
from faraday_agent_parameters_types.faraday_agent_parameters_types import TypeSchema
from pathlib import Path
from packaging.version import parse, Version

manifests_folder = Path(__file__).parent / "static" / "manifests"


def get_schema(type_schema: Union[str, TypeSchema]) -> TypeSchema:
    if isinstance(type_schema, TypeSchema):
        return type_schema
    if isinstance(type_schema, str):
        if type_schema in DATA_TYPE:
            return DATA_TYPE[type_schema]
    raise ValidationError("Invalid Data Type")


def type_validate(type_schema: Union[str, TypeSchema, List[Union[str, TypeSchema]]], data) -> dict:
    if isinstance(type_schema, list):
        errors = {}
        for t in type_schema:
            error = get_schema(t).validate({"data": data})
            if not error:
                return {}
            else:
                errors[t] = error
    else:
        errors = get_schema(type_schema).validate({"data": data})
    return errors


def deserialize_param(type_schema: Union[str, TypeSchema, List[Union[str, TypeSchema]]], data, get_obj=False) -> Any:
    if isinstance(type_schema, list):
        for t in type_schema:
            error = get_schema(t).validate({"data": data})
            if not error:
                type_schema = t
                break
        else:
            raise ValidationError("Could not validate with any of the possible types")
    obj = get_schema(type_schema).load({"data": data})
    return obj if get_obj else obj.data


def serialize_param(type_schema: Union[str, TypeSchema, List[Union[str, TypeSchema]]], data, get_dict=False) -> Any:
    if isinstance(type_schema, list):
        for t in type_schema:
            error = get_schema(t).validate({"data": data})
            if not error:
                type_schema = t
                break
        else:
            raise ValidationError("Could not validate with any of the possible types")
    r_dict = get_schema(type_schema).dump({"data": data})
    return r_dict if get_dict else r_dict.get("data")


@lru_cache()
def get_manifests(version_requested: str = None) -> dict:
    all_manifests_dict = {}

    if version_requested is not None:
        version_requested = parse(version_requested)
        if not isinstance(version_requested, Version):
            raise ValueError("Version requested not valid")

    for path in manifests_folder.iterdir():
        if path.is_file():
            with path.open() as file:
                loaded_json = json.load(file)
                parsed_ver = parse(loaded_json["manifest_version"])
                if version_requested is not None and parsed_ver > version_requested:
                    continue
                manifest_name = loaded_json["name"]
                if manifest_name not in all_manifests_dict:
                    all_manifests_dict[manifest_name] = {}
                all_manifests_dict[manifest_name][parsed_ver] = loaded_json

    manifests_dict = {}
    for tool_name, tool in all_manifests_dict.items():
        manifests_dict[tool_name] = tool[max(tool.keys())]

    return manifests_dict
