#!/usr/bin/env python3
"""Post-generation fixups for the Homebox client code."""

from __future__ import annotations

import re
import sys
from pathlib import Path


_AUTH_HEADER_ASSIGN_RE = re.compile(
    r"self\._headers\[self\.auth_header_name\]\s*=\s*"
    r"f\"\{self\.prefix\} \{self\.token\}\"\s*if\s*self\.prefix\s*else\s*self\.token"
)

_AUTH_HEADER_METHOD = """
    def _get_auth_header_value(self) -> str:
        token = self.token
        prefix = self.prefix.strip()
        if not prefix:
            return token
        prefix_with_space = f"{prefix} "
        if token.lower().startswith(prefix_with_space.lower()):
            return token
        return f"{prefix_with_space}{token}"
"""


def _ensure_auth_header_helper(contents: str) -> str:
    if "def _get_auth_header_value" in contents:
        return contents

    marker_re = re.compile(r'(\n\s*auth_header_name: str = "Authorization"\n)')
    match = marker_re.search(contents)
    if not match:
        raise RuntimeError("Could not find auth_header_name to insert helper method")

    insert_at = match.end(1)
    return contents[:insert_at] + _AUTH_HEADER_METHOD + contents[insert_at:]


def _patch_auth_header_assignments(contents: str) -> str:
    return _AUTH_HEADER_ASSIGN_RE.sub(
        "self._headers[self.auth_header_name] = self._get_auth_header_value()",
        contents,
    )


def main() -> int:
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("homebox_client/client.py")
    if not target.exists():
        raise FileNotFoundError(f"Expected generated client file at {target}")

    text = target.read_text()
    text = _ensure_auth_header_helper(text)
    text = _patch_auth_header_assignments(text)

    if _AUTH_HEADER_ASSIGN_RE.search(text):
        raise RuntimeError("Auth header assignment still uses raw prefix/token concatenation")

    target.write_text(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
