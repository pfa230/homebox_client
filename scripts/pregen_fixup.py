#!/usr/bin/env python3
# pyright: ignore
# mypy: ignore-errors
"""Pre-generation fixups for Homebox OpenAPI JSON.

- Deduplicate enum values (and align x-enum-varnames when present)
- Normalize known wildcard response content types
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def _dedupe_enum(
    enum: list[Any], varnames: list[Any] | None
) -> tuple[list[Any], list[Any] | None]:
    seen: set[Any] = set()
    new_enum: list[Any] = []
    new_var: list[Any] | None = [] if varnames is not None else None
    for idx, value in enumerate(enum):
        if value in seen:
            continue
        seen.add(value)
        new_enum.append(value)
        if new_var is not None and varnames is not None:
            new_var.append(varnames[idx])
    return new_enum, new_var


def _walk_enums(obj: Any) -> None:
    if isinstance(obj, dict):
        enum = obj.get("enum")
        if isinstance(enum, list):
            varnames = obj.get("x-enum-varnames")
            if isinstance(varnames, list) and len(varnames) == len(enum):
                new_enum, new_var = _dedupe_enum(enum, varnames)
                obj["enum"] = new_enum
                obj["x-enum-varnames"] = new_var
            else:
                obj["enum"], _ = _dedupe_enum(enum, None)
        for value in obj.values():
            _walk_enums(value)
    elif isinstance(obj, list):
        for value in obj:
            _walk_enums(value)


_RESPONSE_CONTENT_TYPE_OVERRIDES: dict[tuple[str, str, str], str] = {
    ("get", "/v1/items/export", "200"): "text/csv",
    ("put", "/v1/items/{id}/attachments/{attachment_id}", "200"): "application/json",
    ("put", "/v1/notifiers/{id}", "200"): "application/json",
}


def _override_response_content_types(doc: dict[str, Any]) -> None:
    paths = doc.get("paths")
    if not isinstance(paths, dict):
        return

    for path, operations in paths.items():
        if not isinstance(operations, dict):
            continue
        for method, operation in operations.items():
            if not isinstance(operation, dict):
                continue
            key = (method.lower(), path, "200")
            override = _RESPONSE_CONTENT_TYPE_OVERRIDES.get(key)
            if not override:
                continue
            responses = operation.get("responses")
            if not isinstance(responses, dict):
                continue
            response = responses.get("200")
            if not isinstance(response, dict):
                continue
            content = response.get("content")
            if not isinstance(content, dict) or "*/*" not in content:
                continue
            content[override] = content.pop("*/*")


def main() -> int:
    parser = argparse.ArgumentParser(description="Preprocess Homebox OpenAPI JSON for generation.")
    parser.add_argument("input", type=Path, help="Input OpenAPI JSON")
    parser.add_argument("output", type=Path, help="Output OpenAPI JSON")
    args = parser.parse_args()

    data = json.loads(args.input.read_text())
    _walk_enums(data)
    _override_response_content_types(data)

    args.output.write_text(json.dumps(data, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
