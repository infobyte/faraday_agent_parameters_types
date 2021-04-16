#!/usr/bin/env python

"""Tests for `faraday_agent_parameters_types` package."""

import pytest
from tests.config.agent_manifests import (
    indentify
)

from faraday_agent_parameters_types.custom_types \
    import faraday_integer, faraday_string, faraday_boolean, faraday_list, faraday_int_range, faraday_ip

from ipaddress import IPv4Address, IPv6Address

indentify_dict = [
    {"obj": {"type": "integer"}, "class": faraday_integer.FaradayIntegerSchema()},
    {"obj": {"type": "range"}, "class": faraday_int_range.FaradayRangeSchema()},
    {"obj": {"type": "string"}, "class": faraday_string.FaradayStringSchema()},
    {"obj": {"type": "boolean"}, "class": faraday_boolean.FaradayBooleanSchema()},
    {"obj": {"type": "list", "composed": ["integer", "string"]}, "class": faraday_list.FaradayListSchema()},
    {"obj": {"type": "ip"}, "class": faraday_ip.FaradayIPSchema()},
    # {"obj": {"type": "list", "of": {"type": "boolean"}}, "class": List(Boolean())},
    # {"obj": {"type": "or", "of": ({"type": "boolean"}, {"type": "string"})}, "class": Or(Boolean(), String())},
    # {"obj": {"type": "list", "of": {"type": "or", "of": ({"type": "boolean"}, {"type": "string"})}},
    # "class": List(Or(Boolean(), String()))},
]

field_dict = [

    # INT

    {"obj": {"type": "integer"},
     "class": faraday_integer.FaradayIntegerSchema(),
     "valid": {
         "deser": {"fields": [{"data": {'number': 1},
                               "value": {'number': 1}},
                              {"data": {'number': "1"},
                               "value": {'number': 1}},
                              ], },
         "ser": {"fields": [{"data": {'number': 1},
                             "value": {'number': 1}},
                            {"data": {'number': "1"},
                             "value": {'number': 1}},
                            ], }},
     "invalid": [
         "test",
         {'number': "text"}
     ]
     },

    # STRING

    {"obj": {"type": "string"},
     "class": faraday_string.FaradayStringSchema(),
     "valid": {"deser": {"fields": [{"data": {'text': "text_string"},
                                     "value": {'text': "text_string"}}], },
               "ser": {"fields": [{"data": {'text': "text_string"},
                                   "value": {'text': "text_string"}}], }},
     "invalid": [
         "test",
     ]
     },

    # BOOL

    {"obj": {"type": "boolean"},
     "class": faraday_boolean.FaradayBooleanSchema(),
     "valid": {"deser": {"fields": [{"data": {'option': True},
                                     "value": {'option': True}},
                                    {"data": {'option': "true"},
                                     "value": {'option': True}},
                                    {"data": {'option': 1},
                                     "value": {'option': True}},
                                    ], },
               "ser": {"fields": [{"data": {'option': True},
                                   "value": {'option': True}},
                                  {"data": {'option': "true"},
                                   "value": {'option': True}},
                                  {"data": {'option': 1},
                                   "value": {'option': True}},
                                  ], }},
     "invalid": [
         "test",
         {'option': "test"},
         {'option': 3}
     ]
     },

    # LIST

    {"obj": {"type": "list", "composed": (int, str)},
     "class": faraday_list.FaradayListSchema(),
     "valid": {"deser": {"fields": [{"data": {'items': [1, "test_data"]},
                                     "value": {'items': [1, "test_data"]}}], },
               "ser": {"fields": [{"data": {'items': [1, "test_data"]},
                                   "value": {'items': [1, "test_data"]}}], }},
     "invalid": [
         "test",
         {'items': 1},
         {'items': "test"},
         {'items': {"test": "test"}}
     ]
     },

    # RANGE

    {"obj": {"type": "range"},
     "class": faraday_int_range.FaradayRangeSchema(),
     "valid": {"deser": {"fields": [{"data": {'int_range': "1-4"},
                                     "value": {'int_range': [1, 2, 3, 4]}},
                                    {"data": {'int_range': [4, 5, 6, 7]},
                                     "value": {'int_range': [4, 5, 6, 7]}}
                                    ], },
               "ser": {"fields": [{"data": {'int_range': [1, 2, 3, 4]},
                                   "value": {'int_range': "1-4"}}
                                  ], }},
     "invalid": [
         "test",
         {'int_range': "6-4"},
         {'int_range': "test"},
         {'int_range': 1},
         {'int_range': 1 - 4},
         {'int_range': [1, 2, "Test", 4]}
     ]
     },

    # IP

    {"obj": {"type": "ip"},
     "class": faraday_ip.FaradayIPSchema(),
     "valid": {"deser": {"fields": [{"data": {'ip': "192.168.0.1"},
                                     "value": {'ip': IPv4Address('192.168.0.1')}},
                                    {"data": {'ip': "2001:db8:0:0:0:0:2:1"},
                                     "value": {'ip': IPv6Address('2001:db8:0:0:0:0:2:1')}},
                                    {"data": {'ip': "2001:db8::2:1"},
                                     "value": {'ip': IPv6Address('2001:db8:0:0:0:0:2:1')}},
                                    ], },
               "ser": {"fields": [{"data": {'ip': IPv4Address('192.168.0.1')},
                                   "value": {'ip': "192.168.0.1"}},
                                  {"data": {'ip': IPv6Address('2001:db8:0:0:0:0:2:1')},
                                   "value": {'ip': "2001:db8::2:1"}},
                                  ], }},
     "invalid": [
         "test",
         {'ip': "192.168..1"},
         {'ip': "test"},
         {'ip': [192, 168, 0, 1]}
     ]
     },
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
def test_deserialize(field):
    fields = field["valid"]['deser']['fields']
    if field['obj']['type'] == 'list':
        field['class']._composed_list = field['obj']['composed']
    for entry in fields:
        value = entry['value']
        data = entry['data']
        assert field['class'].load(data).value_dict == value


@pytest.mark.parametrize("field", field_dict)
def test_serialize(field):
    fields = field["valid"]['ser']['fields']
    if field['obj']['type'] == 'list':
        field['class']._composed_list = field['obj']['composed']
    for entry in fields:
        value = entry['value']
        data = entry['data']
        assert field['class'].dump(data) == value


@pytest.mark.parametrize("field", field_dict)
def test_invalid_data(field):
    fields = field["invalid"]
    if field['obj']['type'] == 'list':
        field['class']._composed_list = field['obj']['composed']
    for entry in fields:
        assert field['class'].validate(entry)
