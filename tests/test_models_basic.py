"""Basic model serialization checks for the generated client."""

from homebox_client.models.v1_login_form import V1LoginForm
from homebox_client.models.ent_auth_roles import EntAuthRoles
from homebox_client.models.ent_auth_roles_edges import EntAuthRolesEdges
from homebox_client.types import UNSET, Unset


def test_login_form_roundtrip() -> None:
    model = V1LoginForm(username="user", password="pass", stay_logged_in=True)
    payload = model.to_dict()

    assert payload == {
        "username": "user",
        "password": "pass",
        "stayLoggedIn": True,
    }

    restored = V1LoginForm.from_dict(payload)
    assert restored.username == "user"
    assert restored.password == "pass"
    assert restored.stay_logged_in is True


def test_edges_serialization() -> None:
    edges = EntAuthRolesEdges()
    model = EntAuthRoles(edges=edges)
    payload = model.to_dict()

    assert "edges" in payload
    assert payload["edges"] == {}

    restored = EntAuthRoles.from_dict(payload)
    assert not isinstance(restored.edges, Unset)


def test_additional_properties_roundtrip() -> None:
    model = V1LoginForm.from_dict({"username": "user", "extra": "value"})
    assert model["extra"] == "value"
    model["extra"] = "updated"
    payload = model.to_dict()
    assert payload["extra"] == "updated"
    assert model.additional_keys == ["extra"]


def test_unset_is_falsey() -> None:
    assert not UNSET
