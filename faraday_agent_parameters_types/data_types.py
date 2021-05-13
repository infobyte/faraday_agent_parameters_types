from faraday_agent_parameters_types.custom_types import (
    faraday_integer,
    faraday_string,
    faraday_boolean,
    faraday_list,
    faraday_int_range,
    faraday_ip,
)

DATA_TYPE = {
    "integer": faraday_integer.FaradayIntegerSchema(),
    "string": faraday_string.FaradayStringSchema(),
    "boolean": faraday_boolean.FaradayBooleanSchema(),
    "list": faraday_list.FaradayListSchema(),
    "range": faraday_int_range.FaradayRangeSchema(),
    "ip": faraday_ip.FaradayIPSchema(),
}

BASE_TYPE = {
    "integer": "integer",
    "string": "string",
    "boolean": "boolean",
    "list": "list",
    "range": "string",
    "ip": "string",
}
