#!/usr/bin/env python3
# pyright: ignore
# mypy: ignore-errors
"""Pre-generation fixups for Homebox OpenAPI JSON.

- Deduplicate enum values (and align x-enum-varnames when present)
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


def main() -> int:
    parser = argparse.ArgumentParser(description="Preprocess Homebox OpenAPI JSON for generation.")
    parser.add_argument("input", type=Path, help="Input OpenAPI JSON")
    parser.add_argument("output", type=Path, help="Output OpenAPI JSON")
    args = parser.parse_args()

    data = json.loads(args.input.read_text())
    _walk_enums(data)

    args.output.write_text(json.dumps(data, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
