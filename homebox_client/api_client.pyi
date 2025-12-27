from __future__ import annotations

from typing import Any, Optional, Sequence

from homebox_client.api_response import ApiResponse
from homebox_client.configuration import Configuration

RequestSerialized = tuple[str, str, dict[str, str], Optional[str], list[str]]


class ApiClient:
    configuration: Configuration
    rest_client: Any
    default_headers: dict[str, str]
    client_side_validation: bool
    cookie: Optional[str]
    user_agent: str

    def __init__(
        self,
        configuration: Optional[Configuration] = ...,
        header_name: Optional[str] = ...,
        header_value: Optional[str] = ...,
        cookie: Optional[str] = ...,
    ) -> None: ...

    def __enter__(self) -> "ApiClient": ...
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None: ...

    @classmethod
    def get_default(cls) -> "ApiClient": ...

    @classmethod
    def set_default(cls, default: "ApiClient") -> None: ...

    def set_default_header(self, header_name: str, header_value: str) -> None: ...

    def param_serialize(
        self,
        method: str,
        resource_path: str,
        path_params: Any = ...,
        query_params: Any = ...,
        header_params: Any = ...,
        body: Any = ...,
        post_params: Any = ...,
        files: Any = ...,
        auth_settings: Any = ...,
        collection_formats: Any = ...,
        _host: Optional[str] = ...,
        _request_auth: Any = ...,
    ) -> RequestSerialized: ...

    def call_api(self, *args: Any, **kwargs: Any) -> Any: ...

    def response_deserialize(
        self,
        *,
        response_data: Any,
        response_types_map: dict[str, Optional[str]],
        **kwargs: Any,
    ) -> ApiResponse[Any]: ...

    def sanitize_for_serialization(self, obj: Any) -> Any: ...

    def select_header_accept(self, accepts: Sequence[str]) -> Optional[str]: ...

    def select_header_content_type(self, content_types: Sequence[str]) -> str: ...

    def update_params_for_auth(
        self,
        headers: dict[str, str],
        queries: list[tuple[str, str]],
        auth_settings: list[str],
        resource_path: str,
        method: str,
        body: Any,
        request_auth: Any = ...,
    ) -> None: ...
