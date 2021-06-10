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


def test_ask_for_low_nonexistant_version():
    manifests = get_manifests("0.1.0", test_manifests=True)
    assert not manifests


def test_ask_for_low_unique_version():
    manifests = get_manifests("1.5.0", test_manifests=True)
    assert len(manifests) == 1
    for tool in manifests.values():
        assert tool["manifest_version"] == "1.5.0"


def test_dont_ask_for_version():
    manifests = get_manifests(test_manifests=True)
    for name, tool in manifests.items():
        if name == "test":
            assert tool["manifest_version"] == "1.8.0"
        if name == "test2":
            assert tool["manifest_version"] == "1.6.0"


def test_ask_for_low_version():
    manifests = get_manifests("1.7.0", test_manifests=True)
    for name, tool in manifests.items():
        if name == "test":
            assert tool["manifest_version"] == "1.7.0"
        if name == "test2":
            assert tool["manifest_version"] == "1.6.0"
