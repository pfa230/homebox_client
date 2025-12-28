# homebox-client

`homebox-client` is the typed Python SDK for the Homebox API. The package is generated from the official OpenAPI 3.0 specification (`homebox.json`) with `openapi-python-client` and ships with `attrs`-based models plus HTTPX-powered sync/async clients.

## Highlights

- Full coverage of the Homebox API 1.0, including authentication, items, locations, labels, reporting, maintenance, and notifier endpoints.
- `attrs` models with `typing`-friendly method signatures for confident auto-completion and static analysis.
- Configurable `Client`/`AuthenticatedClient` built on top of HTTPX, making it straightforward to tune timeouts, TLS behaviour, and async usage.
- Generated API modules grouped under `homebox_client/api` with endpoint-specific helpers.

## Requirements

- Python 3.9 or newer.
- `pip` 21.3+ (or another PEP 517 compatible installer) is recommended.

## Installation

### From PyPI

```sh
python -m pip install homebox-client
```

### From source

Install directly from a clone or a source archive:

```sh
git clone https://github.com/pfa230/homebox_client.git
cd homebox_client
python -m pip install .
```

If you are already inside a local checkout, skip the `git clone` command.

### Editable install for development

```sh
python -m pip install -e .
python -m pip install -r test-requirements.txt
```

The editable install keeps the package in sync with the working tree, while `test-requirements.txt` pulls in tooling such as `pytest`, `mypy`, and `flake8`.
It also installs `python-dotenv`, which enables utility scripts to read credentials from a local `.env` file.

## Configuring the client

The generated client defaults to whatever `base_url` you pass. Use `Client` for unauthenticated calls and `AuthenticatedClient` once you have a bearer token:

```python
import os
from homebox_client import Client, AuthenticatedClient

base_url = os.getenv("HOMEBOX_API_URL", "https://demo.homebox.software/api")
client = Client(base_url=base_url)
auth_client = AuthenticatedClient(base_url=base_url, token=os.environ["HOMEBOX_TOKEN"])
```

> Tip: store long-lived access tokens in a secret manager or environment variable (`HOMEBOX_TOKEN` in the example above) instead of hard-coding them.

## Quickstart

```python
import os
from homebox_client import AuthenticatedClient, Client
from homebox_client.api.authentication import post_v1_users_login
from homebox_client.api.items import get_v1_items
from homebox_client.models.v1_login_form import V1LoginForm
from homebox_client.types import Unset

base_url = os.getenv("HOMEBOX_API_URL", "https://demo.homebox.software/api")

# Acquire a short-lived bearer token (skip this block if you already have one)
login_form = V1LoginForm(
    username=os.environ["HOMEBOX_USERNAME"],
    password=os.environ["HOMEBOX_PASSWORD"],
    stay_logged_in=True,
)
token_response = post_v1_users_login.sync(client=Client(base_url=base_url), body=login_form)
if token_response is None or isinstance(token_response.token, Unset):
    raise RuntimeError("Login failed")

# Use the authenticated client for secured endpoints
auth_client = AuthenticatedClient(base_url=base_url, token=token_response.token)
page = get_v1_items.sync(client=auth_client, page_size=5)

if page and not isinstance(page.items, Unset):
    for item in page.items:
        print(f"{item.name} (asset: {item.asset_id})")
```

## Reference documentation

- The original OpenAPI document: `homebox.json`.
- Models live under `homebox_client/models`.
- Endpoint modules live under `homebox_client/api`.
- [Upstream Homebox docs](https://github.com/sysadminsmedia/homebox/tree/main/docs)

## Regenerating the client

If the upstream API specification changes, regenerate the SDK with `openapi-python-client`:

```sh
curl -L -o homebox.json https://raw.githubusercontent.com/sysadminsmedia/homebox/main/docs/en/api/openapi-3.0.json
python scripts/pregen_fixup.py homebox.json homebox_fixed.json
openapi-python-client generate \
  --path homebox_fixed.json \
  --config openapi-python-client.yml \
  --meta none \
  --output-path homebox_client \
  --overwrite
touch homebox_client/py.typed
```

## Development workflow

- Linting: `flake8`
- Type checks: `mypy`
- Tests: `pytest`
- Multi-environment runs: `tox`

All commands operate from the project root. Combine them in CI to guard against regressions.

## Utility scripts

- `scripts/test_homebox_api.py`: smoke-tests authentication and the `/v1/status` endpoint using the environment variables `HOMEBOX_API_URL`, `HOMEBOX_USERNAME`, and `HOMEBOX_PASSWORD`. The script loads these values from `.env` automatically via `python-dotenv`, so run `pip install -r test-requirements.txt` (or install `python-dotenv` manually) before executing it.

## License

MIT. See `LICENSE`.

## Support

Questions about the Homebox API or feature requests for the client can be discussed with the Homebox team on [Discord](https://discord.homebox.software). Bug reports and contribution proposals are welcome via GitHub issues and pull requests.
