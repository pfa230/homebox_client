from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.repo_pagination_result_repo_item_summary import RepoPaginationResultRepoItemSummary
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    q: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    labels: Union[Unset, list[str]] = UNSET,
    locations: Union[Unset, list[str]] = UNSET,
    parent_ids: Union[Unset, list[str]] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["q"] = q

    params["page"] = page

    params["pageSize"] = page_size

    json_labels: Union[Unset, list[str]] = UNSET
    if not isinstance(labels, Unset):
        json_labels = labels


    params["labels"] = json_labels

    json_locations: Union[Unset, list[str]] = UNSET
    if not isinstance(locations, Unset):
        json_locations = locations


    params["locations"] = json_locations

    json_parent_ids: Union[Unset, list[str]] = UNSET
    if not isinstance(parent_ids, Unset):
        json_parent_ids = parent_ids


    params["parentIds"] = json_parent_ids


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/items",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[RepoPaginationResultRepoItemSummary]:
    if response.status_code == 200:
        response_200 = RepoPaginationResultRepoItemSummary.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[RepoPaginationResultRepoItemSummary]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    q: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    labels: Union[Unset, list[str]] = UNSET,
    locations: Union[Unset, list[str]] = UNSET,
    parent_ids: Union[Unset, list[str]] = UNSET,

) -> Response[RepoPaginationResultRepoItemSummary]:
    """ Query All Items

    Args:
        q (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        labels (Union[Unset, list[str]]):
        locations (Union[Unset, list[str]]):
        parent_ids (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RepoPaginationResultRepoItemSummary]
     """


    kwargs = _get_kwargs(
        q=q,
page=page,
page_size=page_size,
labels=labels,
locations=locations,
parent_ids=parent_ids,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    q: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    labels: Union[Unset, list[str]] = UNSET,
    locations: Union[Unset, list[str]] = UNSET,
    parent_ids: Union[Unset, list[str]] = UNSET,

) -> Optional[RepoPaginationResultRepoItemSummary]:
    """ Query All Items

    Args:
        q (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        labels (Union[Unset, list[str]]):
        locations (Union[Unset, list[str]]):
        parent_ids (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RepoPaginationResultRepoItemSummary
     """


    return sync_detailed(
        client=client,
q=q,
page=page,
page_size=page_size,
labels=labels,
locations=locations,
parent_ids=parent_ids,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    q: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    labels: Union[Unset, list[str]] = UNSET,
    locations: Union[Unset, list[str]] = UNSET,
    parent_ids: Union[Unset, list[str]] = UNSET,

) -> Response[RepoPaginationResultRepoItemSummary]:
    """ Query All Items

    Args:
        q (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        labels (Union[Unset, list[str]]):
        locations (Union[Unset, list[str]]):
        parent_ids (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RepoPaginationResultRepoItemSummary]
     """


    kwargs = _get_kwargs(
        q=q,
page=page,
page_size=page_size,
labels=labels,
locations=locations,
parent_ids=parent_ids,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    q: Union[Unset, str] = UNSET,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    labels: Union[Unset, list[str]] = UNSET,
    locations: Union[Unset, list[str]] = UNSET,
    parent_ids: Union[Unset, list[str]] = UNSET,

) -> Optional[RepoPaginationResultRepoItemSummary]:
    """ Query All Items

    Args:
        q (Union[Unset, str]):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        labels (Union[Unset, list[str]]):
        locations (Union[Unset, list[str]]):
        parent_ids (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RepoPaginationResultRepoItemSummary
     """


    return (await asyncio_detailed(
        client=client,
q=q,
page=page,
page_size=page_size,
labels=labels,
locations=locations,
parent_ids=parent_ids,

    )).parsed
