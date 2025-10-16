#!/usr/bin/env python3
"""Simple smoke test against the Homebox API using the generated client."""

from __future__ import annotations

import os
import sys
from dataclasses import dataclass
from typing import Dict, Iterable

from dotenv import load_dotenv

from homebox_client import ApiClient, AuthenticationApi, BaseApi, Configuration
from homebox_client.exceptions import ApiException

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
    missing = []

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


def _authenticate(config: Configuration, credentials: ApiCredentials) -> str:
    """Authenticate against the Homebox API and return a bearer token."""
    with ApiClient(config) as unauthenticated_client:
        auth_api = AuthenticationApi(unauthenticated_client)
        response = auth_api.v1_users_login_post(
            username=credentials.username,
            password=credentials.password,
            stay_logged_in=True,
        )

    token = response.token
    if not token:
        raise RuntimeError("Login succeeded but the API returned an empty token.")
    return token


def _fetch_status(config: Configuration) -> None:
    """Fetch and print a minimal status payload from the API."""
    with ApiClient(config) as api_client:
        base_api = BaseApi(api_client)
        status = base_api.v1_status_get()

    build = status.build

    print("✅ API reachable")
    if status.title:
        print(f"  title: {status.title}")
    print(f"  health: {status.health}")
    if build:
        print(f"  version: {build.version}")
        print(f"  commit: {build.commit}")
        print(f"  built: {build.build_time}")


def main() -> int:
    load_dotenv()

    try:
        credentials = ApiCredentials.from_env()
    except MissingEnvironmentVariable as exc:
        print(f"❌ {exc}", file=sys.stderr)
        return 1

    config = Configuration(host=credentials.api_url)

    try:
        token = _authenticate(config, credentials)
    except ApiException as exc:
        print(f"❌ Authentication failed: {exc}", file=sys.stderr)
        return 2
    except RuntimeError as exc:
        print(f"❌ {exc}", file=sys.stderr)
        return 3

    config.api_key["Bearer"] = token
    config.api_key_prefix["Bearer"] = "Bearer"

    try:
        _fetch_status(config)
    except ApiException as exc:
        print(f"❌ API call failed: {exc}", file=sys.stderr)
        return 4

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
