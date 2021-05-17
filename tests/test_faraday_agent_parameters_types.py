#!/usr/bin/env python

"""Tests for `faraday_agent_parameters_types` package."""

import pytest
from tests.config.agent_manifests import indentify
from faraday_agent_parameters_types.data_types import DATA_TYPE, BASE_TYPE, valid_base_types

from faraday_agent_parameters_types.custom_types import (
    faraday_integer,
    faraday_string,
    faraday_boolean,
    faraday_list,
    faraday_int_range,
    faraday_ip,
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
    # {"obj": {"type": "list", "of": {"type": "boolean"}}, "class": List(Boolean())},
    # {"obj": {"type": "or", "of": ({"type": "boolean"}, {"type": "string"})}, "class": Or(Boolean(), String())},
    # {"obj": {"type": "list", "of": {"type": "or", "of": ({"type": "boolean"}, {"type": "string"})}},
    # "class": List(Or(Boolean(), String()))},
]

field_dict = [
    # INT
    {
        "obj": {"type": "integer"},
        "class": faraday_integer.FaradayIntegerSchema(),
        "valid": {
            "deser": {
                "fields": [
                    {"data": {"data": 1}, "value": {"data": 1}},
                    {"data": {"data": "1"}, "value": {"data": 1}},
                ],
            },
            "ser": {
                "fields": [
                    {"data": {"data": 1}, "value": {"data": 1}},
                    {"data": {"data": "1"}, "value": {"data": 1}},
                ],
            },
        },
        "invalid": ["test", {"data": "text"}],
    },
    # STRING
    {
        "obj": {"type": "string"},
        "class": faraday_string.FaradayStringSchema(),
        "valid": {
            "deser": {
                "fields": [{"data": {"data": "text_string"}, "value": {"data": "text_string"}}],
            },
            "ser": {
                "fields": [{"data": {"data": "text_string"}, "value": {"data": "text_string"}}],
            },
        },
        "invalid": [
            "test",
        ],
    },
    # BOOL
    {
        "obj": {"type": "boolean"},
        "class": faraday_boolean.FaradayBooleanSchema(),
        "valid": {
            "deser": {
                "fields": [
                    {"data": {"data": True}, "value": {"data": True}},
                    {"data": {"data": "true"}, "value": {"data": True}},
                    {"data": {"data": 1}, "value": {"data": True}},
                ],
            },
            "ser": {
                "fields": [
                    {"data": {"data": True}, "value": {"data": True}},
                    {"data": {"data": "true"}, "value": {"data": True}},
                    {"data": {"data": 1}, "value": {"data": True}},
                ],
            },
        },
        "invalid": ["test", {"data": "test"}, {"data": 3}],
    },
    # LIST
    {
        "obj": {"type": "list", "composed": (int, str)},
        "class": faraday_list.FaradayListSchema(),
        "valid": {
            "deser": {
                "fields": [
                    {
                        "data": {"data": [1, "test_data"]},
                        "value": {"data": [1, "test_data"]},
                    }
                ],
            },
            "ser": {
                "fields": [
                    {
                        "data": {"data": [1, "test_data"]},
                        "value": {"data": [1, "test_data"]},
                    }
                ],
            },
        },
        "invalid": ["test", {"data": 1}, {"data": "test"}, {"data": {"test": "test"}}],
    },
    # RANGE
    {
        "obj": {"type": "range"},
        "class": faraday_int_range.FaradayRangeSchema(),
        "valid": {
            "deser": {
                "fields": [
                    {"data": {"data": "1-4"}, "value": {"data": [1, 2, 3, 4]}},
                    {"data": {"data": [4, 5, 6, 7]}, "value": {"data": [4, 5, 6, 7]}},
                ],
            },
            "ser": {
                "fields": [{"data": {"data": [1, 2, 3, 4]}, "value": {"data": "1-4"}}],
            },
        },
        "invalid": [
            "test",
            {"data": "6-4"},
            {"data": "test"},
            {"data": 1},
            {"data": 1 - 4},
            {"data": [1, 2, "Test", 4]},
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
                        "data": {"data": "192.168.0.1"},
                        "value": {"data": IPv4Address("192.168.0.1")},
                    },
                    {
                        "data": {"data": "2001:db8:0:0:0:0:2:1"},
                        "value": {"data": IPv6Address("2001:db8:0:0:0:0:2:1")},
                    },
                    {
                        "data": {"data": "2001:db8::2:1"},
                        "value": {"data": IPv6Address("2001:db8:0:0:0:0:2:1")},
                    },
                ],
            },
            "ser": {
                "fields": [
                    {
                        "data": {"data": IPv4Address("192.168.0.1")},
                        "value": {"data": "192.168.0.1"},
                    },
                    {
                        "data": {"data": IPv6Address("2001:db8:0:0:0:0:2:1")},
                        "value": {"data": "2001:db8::2:1"},
                    },
                ],
            },
        },
        "invalid": [
            "test",
            {"data": "192.168..1"},
            {"data": "test"},
            {"data": [192, 168, 0, 1]},
        ],
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
    assert isinstance(case["class"], indentify(case["obj"]))


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
        assert field["class"].load(data).value_dict == value


@pytest.mark.parametrize("field", field_dict)
def test_serialize(field):
    fields = field["valid"]["ser"]["fields"]
    if field["obj"]["type"] == "list":
        field["class"]._composed_list = field["obj"]["composed"]
    for entry in fields:
        value = entry["value"]
        data = entry["data"]
        assert field["class"].dump(data) == value


@pytest.mark.parametrize("field", field_dict)
def test_invalid_data(field):
    fields = field["invalid"]
    if field["obj"]["type"] == "list":
        field["class"]._composed_list = field["obj"]["composed"]
    for entry in fields:
        assert field["class"].validate(entry)
