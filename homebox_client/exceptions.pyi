from __future__ import annotations

from typing import Any, Optional
from typing_extensions import Self


class OpenApiException(Exception):
    pass


class ApiTypeError(OpenApiException, TypeError):
    path_to_item: Optional[list[Any]]
    valid_classes: Optional[tuple[type[Any], ...]]
    key_type: Optional[bool]

    def __init__(
        self,
        msg: str,
        path_to_item: Optional[list[Any]] = ...,
        valid_classes: Optional[tuple[type[Any], ...]] = ...,
        key_type: Optional[bool] = ...,
    ) -> None: ...


class ApiValueError(OpenApiException, ValueError):
    path_to_item: Optional[list[Any]]

    def __init__(self, msg: str, path_to_item: Optional[list[Any]] = ...) -> None: ...


class ApiAttributeError(OpenApiException, AttributeError):
    path_to_item: Optional[list[Any]]

    def __init__(self, msg: str, path_to_item: Optional[list[Any]] = ...) -> None: ...


class ApiKeyError(OpenApiException, KeyError):
    path_to_item: Optional[list[Any]]

    def __init__(self, msg: str, path_to_item: Optional[list[Any]] = ...) -> None: ...


class ApiException(OpenApiException):
    status: Optional[int]
    reason: Optional[str]
    body: Optional[str]
    data: Optional[Any]
    headers: Optional[Any]

    def __init__(
        self,
        status: Optional[int] = ...,
        reason: Optional[str] = ...,
        http_resp: Any = ...,
        *,
        body: Optional[str] = ...,
        data: Optional[Any] = ...,
    ) -> None: ...

    @classmethod
    def from_response(
        cls,
        *,
        http_resp: Any,
        body: Optional[str],
        data: Optional[Any],
    ) -> Self: ...

    def __str__(self) -> str: ...


class BadRequestException(ApiException):
    pass


class NotFoundException(ApiException):
    pass


class UnauthorizedException(ApiException):
    pass


class ForbiddenException(ApiException):
    pass


class ServiceException(ApiException):
    pass


class ConflictException(ApiException):
    pass


class UnprocessableEntityException(ApiException):
    pass


def render_path(path_to_item: list[Any]) -> str: ...
