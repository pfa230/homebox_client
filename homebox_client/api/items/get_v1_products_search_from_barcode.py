from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.repo_barcode_product import RepoBarcodeProduct
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    data: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["data"] = data


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/products/search-from-barcode",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[list['RepoBarcodeProduct']]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = RepoBarcodeProduct.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[list['RepoBarcodeProduct']]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    data: Union[Unset, str] = UNSET,

) -> Response[list['RepoBarcodeProduct']]:
    """ Search EAN from Barcode

    Args:
        data (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['RepoBarcodeProduct']]
     """


    kwargs = _get_kwargs(
        data=data,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    data: Union[Unset, str] = UNSET,

) -> Optional[list['RepoBarcodeProduct']]:
    """ Search EAN from Barcode

    Args:
        data (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['RepoBarcodeProduct']
     """


    return sync_detailed(
        client=client,
data=data,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    data: Union[Unset, str] = UNSET,

) -> Response[list['RepoBarcodeProduct']]:
    """ Search EAN from Barcode

    Args:
        data (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list['RepoBarcodeProduct']]
     """


    kwargs = _get_kwargs(
        data=data,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    data: Union[Unset, str] = UNSET,

) -> Optional[list['RepoBarcodeProduct']]:
    """ Search EAN from Barcode

    Args:
        data (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list['RepoBarcodeProduct']
     """


    return (await asyncio_detailed(
        client=client,
data=data,

    )).parsed
