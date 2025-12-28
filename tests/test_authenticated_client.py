"""Authorization header handling for AuthenticatedClient."""

from homebox_client import AuthenticatedClient


def test_authenticated_client_adds_prefix_once() -> None:
    client = AuthenticatedClient(base_url="https://example.com", token="Bearer abc123")
    httpx_client = client.get_httpx_client()
    assert httpx_client.headers["Authorization"] == "Bearer abc123"


def test_authenticated_client_adds_prefix_when_missing() -> None:
    client = AuthenticatedClient(base_url="https://example.com", token="abc123")
    httpx_client = client.get_httpx_client()
    assert httpx_client.headers["Authorization"] == "Bearer abc123"
