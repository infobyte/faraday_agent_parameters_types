import json
from pathlib import Path
from unittest import mock

import pytest

from faraday_agent_parameters_types.utils import get_manifests, manifests_folder

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


def _all_manifest_files():
    return sorted(manifests_folder.glob("*.json"))


def _check_environment_variables_metadata(manifest):
    names = manifest["environment_variables"]
    metadata = manifest.get("environment_variables_metadata")
    if metadata is None:
        # The field is optional: without it every variable is treated as sensitive
        return
    assert isinstance(metadata, list)
    for entry in metadata:
        assert isinstance(entry, dict)
        assert set(entry) == {"name", "sensitive"}
        assert isinstance(entry["name"], str)
        assert isinstance(entry["sensitive"], bool)
    metadata_names = [entry["name"] for entry in metadata]
    assert len(metadata_names) == len(set(metadata_names))
    assert sorted(metadata_names) == sorted(names)


@pytest.mark.parametrize("path", _all_manifest_files(), ids=lambda path: path.name)
def test_environment_variables_metadata_valid(path):
    manifest = json.loads(path.read_text())
    _check_environment_variables_metadata(manifest)
    if manifest["environment_variables"]:
        # Bundled manifests must declare the sensitivity of each variable explicitly
        assert "environment_variables_metadata" in manifest


@pytest.mark.parametrize(
    "metadata",
    [
        "BURP_HOST",
        ["BURP_HOST"],
        [{"name": "BURP_HOST"}],
        [{"name": "BURP_HOST", "sensitive": "false"}],
        [{"name": "BURP_HOST", "sensitive": False, "extra": 1}],
        [{"name": "BURP_HOST", "sensitive": False}],
        [{"name": "BURP_HOST", "sensitive": False}, {"name": "OTHER", "sensitive": True}],
        [{"name": "BURP_HOST", "sensitive": False}, {"name": "BURP_HOST", "sensitive": True}],
    ],
)
def test_environment_variables_metadata_invalid(metadata):
    manifest = {"environment_variables": ["BURP_HOST", "BURP_API_KEY"], "environment_variables_metadata": metadata}
    with pytest.raises(AssertionError):
        _check_environment_variables_metadata(manifest)


def test_environment_variables_metadata_is_optional():
    _check_environment_variables_metadata({"environment_variables": ["BURP_HOST"]})


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
        assert "Invalid version: 'hola'" in str(error.value)
