"""Request payload behavior for login endpoint."""

from homebox_client.api.authentication import post_v1_users_login
from homebox_client.models.v1_login_form import V1LoginForm


def test_login_uses_json_only() -> None:
    body = V1LoginForm(username="user", password="pass", stay_logged_in=True)
    kwargs = post_v1_users_login._get_kwargs(body=body)

    assert "json" in kwargs
    assert "data" not in kwargs
    assert kwargs["headers"]["Content-Type"] == "application/json"
