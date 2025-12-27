#!/usr/bin/env python3
"""Simple smoke test against the Homebox API using the generated client."""

from __future__ import annotations

import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable

from dotenv import load_dotenv

# Ensure the repository root is on sys.path so the local package is importable
REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from homebox_client import AuthenticatedClient, Client  # noqa: E402
from homebox_client.api.authentication import post_v1_users_login  # noqa: E402
from homebox_client.api.base import get_v1_status  # noqa: E402
from homebox_client.models.v1_login_form import V1LoginForm  # noqa: E402
from homebox_client.types import Unset  # noqa: E402

REQUIRED_ENV_VARS: Iterable[str] = (
    "HOMEBOX_API_URL",
    "HOMEBOX_USERNAME",
    "HOMEBOX_PASSWORD",
)


class MissingEnvironmentVariable(RuntimeError):
    """Raised when a required environment variable is missing."""


def _load_required_env() -> Dict[str, str]:
    """Fetch required environment variables and error if any are unset."""
    values: Dict[str, str] = {}
    missing: list[str] = []

    for name in REQUIRED_ENV_VARS:
        value = os.getenv(name)
        if value:
            values[name] = value
        else:
            missing.append(name)

    if missing:
        raise MissingEnvironmentVariable(
            f"Missing required environment variable(s): {', '.join(missing)}"
        )

    return values


@dataclass
class ApiCredentials:
    api_url: str
    username: str
    password: str

    @classmethod
    def from_env(cls) -> "ApiCredentials":
        env = _load_required_env()
        return cls(
            api_url=env["HOMEBOX_API_URL"],
            username=env["HOMEBOX_USERNAME"],
            password=env["HOMEBOX_PASSWORD"],
        )


def _authenticate(base_url: str, credentials: ApiCredentials) -> str:
    """Authenticate against the Homebox API and return a bearer token."""
    client = Client(base_url=base_url)
    login_form = V1LoginForm(
        username=credentials.username,
        password=credentials.password,
        stay_logged_in=True,
    )
    token_response = post_v1_users_login.sync(client=client, body=login_form)
    if token_response is None:
        raise RuntimeError("Login failed: empty response from API.")

    token = token_response.token
    if isinstance(token, Unset) or not token:
        raise RuntimeError("Login succeeded but the API returned an empty token.")
    return token


def _fetch_status(client: AuthenticatedClient) -> None:
    """Fetch and print a minimal status payload from the API."""
    status = get_v1_status.sync(client=client)
    if status is None:
        raise RuntimeError("Status check failed: empty response from API.")

    build = status.build

    print("✅ API reachable")
    if not isinstance(status.title, Unset) and status.title:
        print(f"  title: {status.title}")
    if not isinstance(status.health, Unset):
        print(f"  health: {status.health}")
    if not isinstance(build, Unset):
        if not isinstance(build.version, Unset):
            print(f"  version: {build.version}")
        if not isinstance(build.commit, Unset):
            print(f"  commit: {build.commit}")
        if not isinstance(build.build_time, Unset):
            print(f"  built: {build.build_time}")


def main() -> int:
    load_dotenv()

    try:
        credentials = ApiCredentials.from_env()
    except MissingEnvironmentVariable as exc:
        print(f"❌ {exc}", file=sys.stderr)
        return 1

    try:
        token = _authenticate(credentials.api_url, credentials)
    except RuntimeError as exc:
        print(f"❌ {exc}", file=sys.stderr)
        return 3

    client = AuthenticatedClient(base_url=credentials.api_url, token=token)

    try:
        _fetch_status(client)
    except RuntimeError as exc:
        print(f"❌ API call failed: {exc}", file=sys.stderr)
        return 4

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
