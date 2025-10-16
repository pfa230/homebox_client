# homebox-client

`homebox-client` is the typed Python SDK for the Homebox API, the service that helps you track, manage, and organize your belongings. The package is generated from the official OpenAPI specification (`homebox.json`) with OpenAPI Generator 7.16.0 and ships with type-safe Pydantic models and a synchronous HTTP client.

## Highlights

- Full coverage of the Homebox API 1.0, including authentication, items, locations, labels, reporting, maintenance, and notifier endpoints.
- Pydantic v2 models with `typing`-friendly method signatures for confident auto-completion and static analysis.
- Configurable `ApiClient` built on top of `urllib3`, making it straightforward to tune retries, timeouts, and TLS behaviour.
- Generated documentation for every endpoint and model under `docs/`.

## Requirements

- Python 3.9 or newer.
- `pip` 21.3+ (or another PEP 517 compatible installer) is recommended.

## Installation

### From source

The project is not currently published on PyPI. Install it directly from a clone or a source archive:

```sh
git clone https://github.com/<your-org>/homebox-client.git
cd homebox_client
python -m pip install .
```

Replace `<your-org>` with the GitHub organisation or username that hosts your fork. If you are already inside a local checkout, skip the `git clone` command.

### Editable install for development

```sh
python -m pip install -e .
python -m pip install -r test-requirements.txt
```

The editable install keeps the package in sync with the working tree, while `test-requirements.txt` pulls in tooling such as `pytest`, `mypy`, and `flake8`.

## Configuring the client

The generated client defaults to the public demo environment at `https://demo.homebox.software/api`. Override the host or provide authentication tokens through the `Configuration` object:

```python
import os
from homebox_client import Configuration

config = Configuration(host=os.getenv("HOMEBOX_API_URL", "https://demo.homebox.software/api"))
config.api_key["Bearer"] = os.environ["HOMEBOX_TOKEN"]
config.api_key_prefix["Bearer"] = "Bearer"
```

> Tip: store long-lived access tokens in a secret manager or environment variable (`HOMEBOX_TOKEN` in the example above) instead of hard-coding them.

## Quickstart

```python
import os
from homebox_client import ApiClient, AuthenticationApi, Configuration, ItemsApi

config = Configuration(host=os.getenv("HOMEBOX_API_URL", "https://demo.homebox.software/api"))

# Acquire a short-lived bearer token (skip this block if you already have one)
with ApiClient(config) as unauthenticated_client:
    auth_api = AuthenticationApi(unauthenticated_client)
    token_response = auth_api.v1_users_login_post(
        username=os.environ["HOMEBOX_USERNAME"],
        password=os.environ["HOMEBOX_PASSWORD"],
        stay_logged_in=True,
    )

# Persist and apply the token for subsequent requests
config.api_key["Bearer"] = token_response.token
config.api_key_prefix["Bearer"] = "Bearer"

with ApiClient(config) as api_client:
    items_api = ItemsApi(api_client)
    page = items_api.v1_items_get(page_size=5)

    for item in page.items or []:
        print(f"{item.name} (asset: {item.asset_id})")
```

### Handling file uploads and downloads

Endpoints such as `ItemsAttachmentsApi` operate on binary payloads. Use the `with ApiClient(...)` context manager to make sure file handles are released, and pass file objects opened in binary mode (`open("photo.jpg", "rb")`) to upload methods. Responses that stream content expose the raw `urllib3` response on `ApiClient.last_response`.

## Reference documentation

- Endpoint usage guides: `docs/<ApiName>.md` (for example `docs/ItemsApi.md`).
- Data model reference: `docs/<ModelName>.md`.
- The original OpenAPI document: `homebox.json`.

## Regenerating the client

If the upstream API specification changes, regenerate the SDK with OpenAPI Generator:

```sh
docker run --rm \
  -v "${PWD}:/local" \
  openapitools/openapi-generator-cli:v7.16.0 generate \
  -i /local/homebox.json \
  -g python \
  -o /local/generated \
  --additional-properties=packageName=homebox_client,projectName=homebox-client,packageVersion=1.0.0,pythonAttrNoneIfUnset=true
```

Review the contents of `/local/generated`, then copy the updated modules into this repository (or adjust the output path to overwrite the current package once you have reviewed the changes).

## Development workflow

- Linting: `flake8`
- Type checks: `mypy`
- Tests: `pytest`
- Multi-environment runs: `tox`

All commands operate from the project root. Combine them in CI to guard against regressions.

## Support

Questions about the Homebox API or feature requests for the client can be discussed with the Homebox team on [Discord](https://discord.homebox.software). Bug reports and contribution proposals are welcome via GitHub issues and pull requests.
