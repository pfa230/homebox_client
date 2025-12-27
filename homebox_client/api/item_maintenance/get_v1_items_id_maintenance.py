from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_v1_items_id_maintenance_status import GetV1ItemsIdMaintenanceStatus
from ...models.repo_maintenance_entry_with_details import RepoMaintenanceEntryWithDetails
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    id: str,
    *,
    status: Union[Unset, GetV1ItemsIdMaintenanceStatus] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/items/{id}/maintenance".format(id=id,),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[list['RepoMaintenanceEntryWithDetails']]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = RepoMaintenanceEntryWithDetails.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[list['RepoMaintenanceEntryWithDetails']]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    status: Union[Unset, GetV1ItemsIdMaintenanceStatus] = UNSET,

) -> Response[list['RepoMaintenanceEntryWithDetails']]:
    """ Get Maintenance Log

    Args:
        id (str):
        status (Union[Unset, GetV1ItemsIdMaintenanceStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['RepoMaintenanceEntryWithDetails']]
     """


    kwargs = _get_kwargs(
        id=id,
status=status,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    status: Union[Unset, GetV1ItemsIdMaintenanceStatus] = UNSET,

) -> Optional[list['RepoMaintenanceEntryWithDetails']]:
    """ Get Maintenance Log

    Args:
        id (str):
        status (Union[Unset, GetV1ItemsIdMaintenanceStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['RepoMaintenanceEntryWithDetails']
     """


    return sync_detailed(
        id=id,
client=client,
status=status,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    status: Union[Unset, GetV1ItemsIdMaintenanceStatus] = UNSET,

) -> Response[list['RepoMaintenanceEntryWithDetails']]:
    """ Get Maintenance Log

    Args:
        id (str):
        status (Union[Unset, GetV1ItemsIdMaintenanceStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['RepoMaintenanceEntryWithDetails']]
     """


    kwargs = _get_kwargs(
        id=id,
status=status,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    status: Union[Unset, GetV1ItemsIdMaintenanceStatus] = UNSET,

) -> Optional[list['RepoMaintenanceEntryWithDetails']]:
    """ Get Maintenance Log

    Args:
        id (str):
        status (Union[Unset, GetV1ItemsIdMaintenanceStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['RepoMaintenanceEntryWithDetails']
     """


    return (await asyncio_detailed(
        id=id,
client=client,
status=status,

    )).parsed
