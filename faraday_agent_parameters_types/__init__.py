"""Top-level package for faraday_agent_parameters_types."""

__author__ = """Faraday Development Team"""
__email__ = "devel@infobytesec.com"
__version__ = "0.1.2"

from pathlib import Path
from typing import Union


def manifests_folder() -> Union[Path, str]:

    return Path(__file__).parent / "static" / "executors" / "official"
