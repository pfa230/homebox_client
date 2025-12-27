from __future__ import annotations

from typing import Any, Mapping, Optional

import urllib3

SUPPORTED_SOCKS_PROXIES: set[str]
RESTResponseType = urllib3.HTTPResponse


def is_socks_proxy_url(url: Optional[str]) -> bool: ...


class RESTResponse:
    response: Any
    status: int
    reason: str
    data: Optional[bytes]

    def __init__(self, resp: Any) -> None: ...
    def read(self) -> bytes: ...
    def getheaders(self) -> Mapping[str, str]: ...
    def getheader(self, name: str, default: Optional[str] = ...) -> Optional[str]: ...


class RESTClientObject:
    pool_manager: Any

    def __init__(self, configuration: Any) -> None: ...

    def request(
        self,
        method: str,
        url: str,
        headers: Optional[Mapping[str, str]] = ...,
        body: Any = ...,
        post_params: Any = ...,
        _request_timeout: Any = ...,
    ) -> RESTResponse: ...
