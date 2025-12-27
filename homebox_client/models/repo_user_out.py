from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="RepoUserOut")



@_attrs_define
class RepoUserOut:
    """ 
        Attributes:
            email (Union[Unset, str]):
            group_id (Union[Unset, str]):
            group_name (Union[Unset, str]):
            id (Union[Unset, str]):
            is_owner (Union[Unset, bool]):
            is_superuser (Union[Unset, bool]):
            name (Union[Unset, str]):
            oidc_issuer (Union[Unset, str]):
            oidc_subject (Union[Unset, str]):
     """

    email: Union[Unset, str] = UNSET
    group_id: Union[Unset, str] = UNSET
    group_name: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    is_owner: Union[Unset, bool] = UNSET
    is_superuser: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    oidc_issuer: Union[Unset, str] = UNSET
    oidc_subject: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        email = self.email

        group_id = self.group_id

        group_name = self.group_name

        id = self.id

        is_owner = self.is_owner

        is_superuser = self.is_superuser

        name = self.name

        oidc_issuer = self.oidc_issuer

        oidc_subject = self.oidc_subject


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if email is not UNSET:
            field_dict["email"] = email
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if group_name is not UNSET:
            field_dict["groupName"] = group_name
        if id is not UNSET:
            field_dict["id"] = id
        if is_owner is not UNSET:
            field_dict["isOwner"] = is_owner
        if is_superuser is not UNSET:
            field_dict["isSuperuser"] = is_superuser
        if name is not UNSET:
            field_dict["name"] = name
        if oidc_issuer is not UNSET:
            field_dict["oidcIssuer"] = oidc_issuer
        if oidc_subject is not UNSET:
            field_dict["oidcSubject"] = oidc_subject

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        group_id = d.pop("groupId", UNSET)

        group_name = d.pop("groupName", UNSET)

        id = d.pop("id", UNSET)

        is_owner = d.pop("isOwner", UNSET)

        is_superuser = d.pop("isSuperuser", UNSET)

        name = d.pop("name", UNSET)

        oidc_issuer = d.pop("oidcIssuer", UNSET)

        oidc_subject = d.pop("oidcSubject", UNSET)

        repo_user_out = cls(
            email=email,
            group_id=group_id,
            group_name=group_name,
            id=id,
            is_owner=is_owner,
            is_superuser=is_superuser,
            name=name,
            oidc_issuer=oidc_issuer,
            oidc_subject=oidc_subject,
        )


        repo_user_out.additional_properties = d
        return repo_user_out

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
