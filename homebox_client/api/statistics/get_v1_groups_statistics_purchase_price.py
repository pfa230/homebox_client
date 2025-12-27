from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.repo_value_over_time import RepoValueOverTime
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    start: Union[Unset, str] = UNSET,
    end: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["start"] = start

    params["end"] = end


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/groups/statistics/purchase-price",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[RepoValueOverTime]:
    if response.status_code == 200:
        response_200 = RepoValueOverTime.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[RepoValueOverTime]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start: Union[Unset, str] = UNSET,
    end: Union[Unset, str] = UNSET,

) -> Response[RepoValueOverTime]:
    """ Get Purchase Price Statistics

    Args:
        start (Union[Unset, str]):
        end (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RepoValueOverTime]
     """


    kwargs = _get_kwargs(
        start=start,
end=end,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    start: Union[Unset, str] = UNSET,
    end: Union[Unset, str] = UNSET,

) -> Optional[RepoValueOverTime]:
    """ Get Purchase Price Statistics

    Args:
        start (Union[Unset, str]):
        end (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RepoValueOverTime
     """


    return sync_detailed(
        client=client,
start=start,
end=end,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start: Union[Unset, str] = UNSET,
    end: Union[Unset, str] = UNSET,

) -> Response[RepoValueOverTime]:
    """ Get Purchase Price Statistics

    Args:
        start (Union[Unset, str]):
        end (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RepoValueOverTime]
     """


    kwargs = _get_kwargs(
        start=start,
end=end,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    start: Union[Unset, str] = UNSET,
    end: Union[Unset, str] = UNSET,

) -> Optional[RepoValueOverTime]:
    """ Get Purchase Price Statistics

    Args:
        start (Union[Unset, str]):
        end (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RepoValueOverTime
     """


    return (await asyncio_detailed(
        client=client,
start=start,
end=end,

    )).parsed
