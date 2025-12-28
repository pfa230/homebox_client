from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.v1_login_form import V1LoginForm
from ...models.v1_token_response import V1TokenResponse
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    body: V1LoginForm,
    provider: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["provider"] = provider


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/users/login",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[V1TokenResponse]:
    if response.status_code == 200:
        response_200 = V1TokenResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[V1TokenResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: V1LoginForm,
    provider: Union[Unset, str] = UNSET,

) -> Response[V1TokenResponse]:
    """ User Login

    Args:
        provider (Union[Unset, str]):
        body (V1LoginForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V1TokenResponse]
     """


    kwargs = _get_kwargs(
        body=body,
provider=provider,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: V1LoginForm,
    provider: Union[Unset, str] = UNSET,

) -> Optional[V1TokenResponse]:
    """ User Login

    Args:
        provider (Union[Unset, str]):
        body (V1LoginForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V1TokenResponse
     """


    return sync_detailed(
        client=client,
body=body,
provider=provider,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: V1LoginForm,
    provider: Union[Unset, str] = UNSET,

) -> Response[V1TokenResponse]:
    """ User Login

    Args:
        provider (Union[Unset, str]):
        body (V1LoginForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[V1TokenResponse]
     """


    kwargs = _get_kwargs(
        body=body,
provider=provider,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: V1LoginForm,
    provider: Union[Unset, str] = UNSET,

) -> Optional[V1TokenResponse]:
    """ User Login

    Args:
        provider (Union[Unset, str]):
        body (V1LoginForm):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        V1TokenResponse
     """


    return (await asyncio_detailed(
        client=client,
body=body,
provider=provider,

    )).parsed
