from pathlib import Path
from unittest import mock

import pytest

from faraday_agent_parameters_types.utils import get_manifests

needed_manifest_fields = (
    "arguments",
    "environment_variables",
    "check_cmds",
    "cmd",
    "category",
    "name",
    "title",
    "website",
    "description",
    "image",
    "manifest_version",
    "repo_executor",
)

nullable_fields = ("website", "image")


def test_manifests_valid():
    manifests = get_manifests()
    assert manifests
    for manifest in manifests.values():
        # Check if field exists
        assert all(field in manifest for field in needed_manifest_fields)
        # Check if none
        for key, value in manifest.items():
            assert key in nullable_fields or value is not None


@mock.patch("faraday_agent_parameters_types.utils.manifests_folder", Path(__file__).parent / "test_manifests")
class Test_manifests_versions:
    def test_ask_for_low_nonexistant_version(self):
        manifests = get_manifests("0.1.0")
        assert not manifests

    def test_ask_for_low_unique_version(self):
        manifests = get_manifests("1.5.0")
        assert len(manifests) == 1
        for tool in manifests.values():
            assert tool["manifest_version"] == "1.5.0"

    def test_dont_ask_for_version(self):
        manifests = get_manifests()
        for name, tool in manifests.items():
            if name == "test":
                assert tool["manifest_version"] == "1.8.0"
            if name == "test2":
                assert tool["manifest_version"] == "1.6.0"

    def test_ask_for_low_version(self):
        manifests = get_manifests("1.7.0")
        for name, tool in manifests.items():
            if name == "test":
                assert tool["manifest_version"] == "1.7.0"
            if name == "test2":
                assert tool["manifest_version"] == "1.6.0"

    def test_incorrect_version_requested(self):
        with pytest.raises(ValueError) as error:
            get_manifests("hola")
        assert "Version requested not valid" in str(error.value)
