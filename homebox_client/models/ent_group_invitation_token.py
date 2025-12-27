from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.ent_group_invitation_token_edges import EntGroupInvitationTokenEdges





T = TypeVar("T", bound="EntGroupInvitationToken")



@_attrs_define
class EntGroupInvitationToken:
    """ 
        Attributes:
            created_at (Union[Unset, str]): CreatedAt holds the value of the "created_at" field.
            edges (Union[Unset, EntGroupInvitationTokenEdges]):
            expires_at (Union[Unset, str]): ExpiresAt holds the value of the "expires_at" field.
            id (Union[Unset, str]): ID of the ent.
            token (Union[Unset, list[int]]): Token holds the value of the "token" field.
            updated_at (Union[Unset, str]): UpdatedAt holds the value of the "updated_at" field.
            uses (Union[Unset, int]): Uses holds the value of the "uses" field.
     """

    created_at: Union[Unset, str] = UNSET
    edges: Union[Unset, 'EntGroupInvitationTokenEdges'] = UNSET
    expires_at: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    token: Union[Unset, list[int]] = UNSET
    updated_at: Union[Unset, str] = UNSET
    uses: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ent_group_invitation_token_edges import EntGroupInvitationTokenEdges
        created_at = self.created_at

        edges: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.edges, Unset):
            edges = self.edges.to_dict()

        expires_at = self.expires_at

        id = self.id

        token: Union[Unset, list[int]] = UNSET
        if not isinstance(self.token, Unset):
            token = self.token



        updated_at = self.updated_at

        uses = self.uses


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if edges is not UNSET:
            field_dict["edges"] = edges
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at
        if id is not UNSET:
            field_dict["id"] = id
        if token is not UNSET:
            field_dict["token"] = token
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if uses is not UNSET:
            field_dict["uses"] = uses

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ent_group_invitation_token_edges import EntGroupInvitationTokenEdges
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        _edges = d.pop("edges", UNSET)
        edges: Union[Unset, EntGroupInvitationTokenEdges]
        if isinstance(_edges,  Unset):
            edges = UNSET
        else:
            edges = EntGroupInvitationTokenEdges.from_dict(_edges)




        expires_at = d.pop("expires_at", UNSET)

        id = d.pop("id", UNSET)

        token = cast(list[int], d.pop("token", UNSET))


        updated_at = d.pop("updated_at", UNSET)

        uses = d.pop("uses", UNSET)

        ent_group_invitation_token = cls(
            created_at=created_at,
            edges=edges,
            expires_at=expires_at,
            id=id,
            token=token,
            updated_at=updated_at,
            uses=uses,
        )


        ent_group_invitation_token.additional_properties = d
        return ent_group_invitation_token

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
