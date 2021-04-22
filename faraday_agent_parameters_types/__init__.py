"""Top-level package for faraday_agent_parameters_types."""

__author__ = """Blas Moyano"""
__email__ = 'bmoyano@infobytesec.com'
__version__ = '0.1.0'

from pathlib import Path
from typing import Union
from faraday_agent_parameters_types.custom_types import faraday_integer, faraday_string, faraday_boolean, faraday_list, faraday_int_range, faraday_ip

DATA_TYPE = {
    "integer": custom_types.faraday_integer.FaradayIntegerSchema(),
    "string": custom_types.faraday_string.FaradayStringSchema(),
    "boolean": custom_types.faraday_boolean.FaradayBooleanSchema(),
    "list": custom_types.faraday_list.FaradayListSchema(),
    "range": custom_types.faraday_int_range.FaradayRangeSchema(),
    "ip": custom_types.faraday_ip.FaradayIPSchema()
}


def manifests_folder() -> Union[Path, str]:

    return Path(__file__).parent / "static" / "executors" / "official"


def type_validate(p_type: str, data):
    schema = DATA_TYPE[p_type]
    errors = schema.validate({"data": data})
    return errors
