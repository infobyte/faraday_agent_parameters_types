#!/usr/bin/env python

"""Tests for `faraday_agent_parameters_types` package."""

import pytest
from tests.config.agent_manifests import (
    indentify
)

from faraday_agent_parameters_types.custom_types \
    import faraday_integer, faraday_string, faraday_boolean, faraday_list, faraday_int_range

indentify_dict = [
    {"obj": {"type": "integer"}, "class": faraday_integer.FaradayIntegerSchema()},
    {"obj": {"type": "range"}, "class": faraday_int_range.FaradayRangeSchema()},
    {"obj": {"type": "string"}, "class": faraday_string.FaradayStringSchema()},
    {"obj": {"type": "boolean"}, "class": faraday_boolean.FaradayBooleanSchema()},
    {"obj": {"type": "list", "composed": ["integer", "string"]}, "class": faraday_list.FaradayListSchema()},
    # {"obj": {"type": "list", "of": {"type": "boolean"}}, "class": List(Boolean())},
    # {"obj": {"type": "or", "of": ({"type": "boolean"}, {"type": "string"})}, "class": Or(Boolean(), String())},
    # {"obj": {"type": "list", "of": {"type": "or", "of": ({"type": "boolean"}, {"type": "string"})}},
    # "class": List(Or(Boolean(), String()))},
]

field_dict = [
    {"obj": {"type": "integer"}, "class": faraday_integer.FaradayIntegerSchema(),
     "fields": {"data": {'number': 1}, "value": {'number': 1}}, },
    {"obj": {"type": "integer"}, "class": faraday_integer.FaradayIntegerSchema(),
     "fields": {"data": {'number': "1"}, "value": {'number': 1}}, },
    {"obj": {"type": "string"}, "class": faraday_string.FaradayStringSchema(),
     "fields": {"data": {'text': "text_string"}, "value": {'text': "text_string"}}, },
    {"obj": {"type": "boolean"}, "class": faraday_boolean.FaradayBooleanSchema(),
     "fields": {"data": {'option': True}, "value": {'option': True}}, },
    {"obj": {"type": "boolean"}, "class": faraday_boolean.FaradayBooleanSchema(),
     "fields": {"data": {'option': "true"}, "value": {'option': True}}, },
    {"obj": {"type": "list", "composed": (int, str)}, "class": faraday_list.FaradayListSchema(),
     "fields": {"data": {'items': [1, "test_data"]}, "value": {'items': [1, "test_data"]}}, },
    {"obj": {"type": "range"}, "class": faraday_int_range.FaradayRangeSchema(),
         "fields": {"data": {'str_range': "1-3"}, "value": {'int_range': [1, 2, 3], 'str_range': "1-3"}}, },
]


@pytest.mark.parametrize("case", indentify_dict)
def test_indentify_type(case):
    # In base of obj, it should recognize the class
    assert indentify(case["obj"]) == type(case["class"])


@pytest.mark.parametrize("case", indentify_dict)
def test_to_object(case):
    assert case['class'].to_obj() == case["obj"]["type"]


# Here goes an import, or an example list
@pytest.mark.parametrize("field", field_dict)
def test_serializar_deserialize(field):
    value = field['fields']['value']
    data = field['fields']['data']
    if field['obj']['type'] == 'list':
        field['class']._composed_list = field['obj']['composed']
    load_data = field['class'].load(data)
    assert field['class'].dump(load_data) == value
