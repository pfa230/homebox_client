"""Basic import checks for the generated client."""

from homebox_client import AuthenticatedClient, Client
from homebox_client.api.base import get_v1_status


def test_imports() -> None:
    assert Client is not None
    assert AuthenticatedClient is not None
    assert get_v1_status is not None
