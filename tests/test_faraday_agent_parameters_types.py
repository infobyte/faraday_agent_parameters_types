#!/usr/bin/env python

"""Tests for `faraday_agent_parameters_types` package."""

import pytest
from faraday_agent_parameters_types.data_types import DATA_TYPE, BASE_TYPE, valid_base_types
from faraday_agent_parameters_types.utils import deserialize_param, serialize_param

from faraday_agent_parameters_types.custom_types import (
    faraday_integer,
    faraday_string,
    faraday_boolean,
    faraday_list,
    faraday_int_range,
    faraday_ip,
    faraday_float,
)

from ipaddress import IPv4Address, IPv6Address

indentify_dict = [
    {"obj": {"type": "integer"}, "class": faraday_integer.FaradayIntegerSchema()},
    {"obj": {"type": "range"}, "class": faraday_int_range.FaradayRangeSchema()},
    {"obj": {"type": "string"}, "class": faraday_string.FaradayStringSchema()},
    {"obj": {"type": "boolean"}, "class": faraday_boolean.FaradayBooleanSchema()},
    {
        "obj": {"type": "list", "composed": ["integer", "string"]},
        "class": faraday_list.FaradayListSchema(),
    },
    {"obj": {"type": "ip"}, "class": faraday_ip.FaradayIPSchema()},
    {"obj": {"type": "float"}, "class": faraday_float.FaradayFloatSchema()},
]

field_dict = [
    # INT
    {
        "obj": {"type": "integer"},
        "class": faraday_integer.FaradayIntegerSchema(),
        "valid": {
            "deser": {
                "fields": [
                    {"data": 1, "value": 1},
                    {"data": 1.5, "value": 1},
                    {"data": "1", "value": 1},
                ],
            },
            "ser": {
                "fields": [
                    {"data": 1, "value": 1},
                    {"data": 1.5, "value": 1},
                    {"data": "1", "value": 1},
                ],
            },
        },
        "invalid": ["test", {"data": "text"}, ["test", "test2"]],
    },
    # STRING
    {
        "obj": {"type": "string"},
        "class": faraday_string.FaradayStringSchema(),
        "valid": {
            "deser": {
                "fields": [{"data": "text_string", "value": "text_string"}],
            },
            "ser": {
                "fields": [{"data": "text_string", "value": "text_string"}],
            },
        },
        "invalid": ["test", {"Test": 2}, ["test"]],
    },
    # BOOL
    {
        "obj": {"type": "boolean"},
        "class": faraday_boolean.FaradayBooleanSchema(),
        "valid": {
            "deser": {
                "fields": [
                    {"data": True, "value": True},
                    {"data": "true", "value": True},
                    {"data": 1, "value": True},
                ],
            },
            "ser": {
                "fields": [
                    {"data": True, "value": True},
                    {"data": "true", "value": True},
                    {"data": 1, "value": True},
                ],
            },
        },
        "invalid": [
            "test",
            {"data": "test"},
            {"data": 3},
            3,
            ["3"],
        ],
    },
    # LIST
    {
        "obj": {"type": "list", "composed": (int, str)},
        "class": faraday_list.FaradayListSchema(),
        "valid": {
            "deser": {
                "fields": [
                    {
                        "data": [1, "test_data"],
                        "value": [1, "test_data"],
                    }
                ],
            },
            "ser": {
                "fields": [
                    {
                        "data": [1, "test_data"],
                        "value": [1, "test_data"],
                    }
                ],
            },
        },
        "invalid": [
            "test",
            {"data": 1},
            {"data": "test"},
            {"data": {"test": "test"}},
            1,
            {"test": "test"},
        ],
    },
    # RANGE
    {
        "obj": {"type": "range"},
        "class": faraday_int_range.FaradayRangeSchema(),
        "valid": {
            "deser": {
                "fields": [
                    {"data": "1-4", "value": [1, 2, 3, 4]},
                    {"data": [4, 5, 6, 7], "value": [4, 5, 6, 7]},
                ],
            },
            "ser": {
                "fields": [{"data": [1, 2, 3, 4], "value": "1-4"}],
            },
        },
        "invalid": [
            "test",
            {"data": "6-4"},
            {"data": "test"},
            {"data": 1},
            {"data": 1 - 4},
            {"data": [1, 2, "Test", 4]},
            "6-4",
            1,
            1 - 4,
            [1, 2, "Test", 4],
        ],
    },
    # IP
    {
        "obj": {"type": "ip"},
        "class": faraday_ip.FaradayIPSchema(),
        "valid": {
            "deser": {
                "fields": [
                    {
                        "data": "192.168.0.1",
                        "value": IPv4Address("192.168.0.1"),
                    },
                    {
                        "data": "2001:db8:0:0:0:0:2:1",
                        "value": IPv6Address("2001:db8:0:0:0:0:2:1"),
                    },
                    {
                        "data": "2001:db8::2:1",
                        "value": IPv6Address("2001:db8:0:0:0:0:2:1"),
                    },
                ],
            },
            "ser": {
                "fields": [
                    {
                        "data": IPv4Address("192.168.0.1"),
                        "value": "192.168.0.1",
                    },
                    {
                        "data": IPv6Address("2001:db8:0:0:0:0:2:1"),
                        "value": "2001:db8::2:1",
                    },
                ],
            },
        },
        "invalid": [
            "test",
            {"data": "192.168..1"},
            {"data": "test"},
            {"data": [192, 168, 0, 1]},
            "192.168..1",
            [192, 168, 0, 1],
        ],
    },
    # Float
    {
        "obj": {"type": "float"},
        "class": faraday_float.FaradayFloatSchema(),
        "valid": {
            "deser": {
                "fields": [
                    {"data": 1.5, "value": 1.5},
                    {"data": "1.5", "value": 1.5},
                    {"data": "1", "value": 1.0},
                ],
            },
            "ser": {
                "fields": [
                    {"data": 1.5, "value": 1.5},
                    {"data": "1.5", "value": 1.5},
                    {"data": "1", "value": 1.0},
                ],
            },
        },
        "invalid": ["test", {"data": "text"}],
    },
]


def test_data_type_and_base_type():
    for d_type in DATA_TYPE:
        if d_type not in BASE_TYPE:
            print(f'\n\nBASE_TYPE NOT ASSIGNED FOR "{d_type}"\nGo to data_types.py and assign a base type to it')
            assert False


def test_base_type_valid():
    for b_value in BASE_TYPE.values():
        if b_value not in valid_base_types:
            print(f'\n\n"{b_value}" is not a valid base type')
            assert False


@pytest.mark.parametrize("case", indentify_dict)
def test_indentify_type(case):
    # In base of obj, it should recognize the class
    assert isinstance(case["class"], type(DATA_TYPE[case["obj"]["type"]]))


@pytest.mark.parametrize("case", indentify_dict)
def test_to_object(case):
    assert case["class"].to_obj() == case["obj"]["type"]


# Here goes an import, or an example list
@pytest.mark.parametrize("field", field_dict)
def test_deserialize(field):
    fields = field["valid"]["deser"]["fields"]
    if field["obj"]["type"] == "list":
        field["class"]._composed_list = field["obj"]["composed"]
    for entry in fields:
        value = entry["value"]
        data = entry["data"]
        assert deserialize_param(field["class"], data) == value


@pytest.mark.parametrize("field", field_dict)
def test_serialize(field):
    fields = field["valid"]["ser"]["fields"]
    if field["obj"]["type"] == "list":
        field["class"]._composed_list = field["obj"]["composed"]
    for entry in fields:
        value = entry["value"]
        data = entry["data"]
        assert serialize_param(field["class"], data) == value


@pytest.mark.parametrize("field", field_dict)
def test_invalid_data(field):
    fields = field["invalid"]
    if field["obj"]["type"] == "list":
        field["class"]._composed_list = field["obj"]["composed"]
    for entry in fields:
        assert field["class"].validate(entry)
