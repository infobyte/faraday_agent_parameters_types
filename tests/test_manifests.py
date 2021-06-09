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
