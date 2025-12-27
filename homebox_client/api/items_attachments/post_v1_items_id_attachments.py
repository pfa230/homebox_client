from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.post_v1_items_id_attachments_body import PostV1ItemsIdAttachmentsBody
from ...models.repo_item_out import RepoItemOut
from ...models.validate_error_response import ValidateErrorResponse
from typing import cast



def _get_kwargs(
    id: str,
    *,
    body: PostV1ItemsIdAttachmentsBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/items/{id}/attachments".format(id=id,),
    }

    _kwargs["files"] = body.to_multipart()



    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[RepoItemOut, ValidateErrorResponse]]:
    if response.status_code == 200:
        response_200 = RepoItemOut.from_dict(response.json())



        return response_200

    if response.status_code == 422:
        response_422 = ValidateErrorResponse.from_dict(response.json())



        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[RepoItemOut, ValidateErrorResponse]]:
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
    body: PostV1ItemsIdAttachmentsBody,

) -> Response[Union[RepoItemOut, ValidateErrorResponse]]:
    """ Create Item Attachment

    Args:
        id (str):
        body (PostV1ItemsIdAttachmentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RepoItemOut, ValidateErrorResponse]]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PostV1ItemsIdAttachmentsBody,

) -> Optional[Union[RepoItemOut, ValidateErrorResponse]]:
    """ Create Item Attachment

    Args:
        id (str):
        body (PostV1ItemsIdAttachmentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[RepoItemOut, ValidateErrorResponse]
     """


    return sync_detailed(
        id=id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PostV1ItemsIdAttachmentsBody,

) -> Response[Union[RepoItemOut, ValidateErrorResponse]]:
    """ Create Item Attachment

    Args:
        id (str):
        body (PostV1ItemsIdAttachmentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RepoItemOut, ValidateErrorResponse]]
     """


    kwargs = _get_kwargs(
        id=id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PostV1ItemsIdAttachmentsBody,

) -> Optional[Union[RepoItemOut, ValidateErrorResponse]]:
    """ Create Item Attachment

    Args:
        id (str):
        body (PostV1ItemsIdAttachmentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[RepoItemOut, ValidateErrorResponse]
     """


    return (await asyncio_detailed(
        id=id,
client=client,
body=body,

    )).parsed
