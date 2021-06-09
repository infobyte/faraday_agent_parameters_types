import json
from faraday_agent_parameters_types.data_types import DATA_TYPE
from typing import Union, List, Any
from marshmallow import ValidationError
from faraday_agent_parameters_types.faraday_agent_parameters_types import TypeSchema
from pathlib import Path
from packaging.version import parse
import re

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


def get_manifests(version_requested: str = None) -> dict:
    all_manifests_dict = {}
    for path in manifests_folder.iterdir():
        if path.is_file():
            manifest_name = re.search(r"^(.+)-.+$", path.stem).group(1)
            if manifest_name not in all_manifests_dict:
                all_manifests_dict[manifest_name] = {}
            with path.open() as file:
                loaded_json = json.load(file)
                all_manifests_dict[manifest_name][loaded_json["manifest_version"]] = loaded_json

    # GET LASTEST VERSION
    manifests_dict = {}
    for tool_name, tool in all_manifests_dict.items():
        parsed_versions = {}
        for version, data in tool.items():
            parsed_version = parse(version)
            if version_requested and parsed_version > parse(version_requested):
                continue
            parsed_versions[parsed_version] = data

        if not parsed_versions:
            continue
        version_to_use = max(parsed_versions)
        manifests_dict[tool_name] = parsed_versions[version_to_use]

    return manifests_dict
