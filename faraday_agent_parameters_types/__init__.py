"""Top-level package for faraday_agent_parameters_types."""

__author__ = """Blas Moyano"""
__email__ = 'bmoyano@infobytesec.com'
__version__ = '0.1.0'

from pathlib import Path
from typing import Union


def manifests_folder() -> Union[Path, str]:

    return Path(__file__).parent / "static" / "executors" / "official"
