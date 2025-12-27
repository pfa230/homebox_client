from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="RepoNotifierOut")



@_attrs_define
class RepoNotifierOut:
    """ 
        Attributes:
            created_at (Union[Unset, str]):
            group_id (Union[Unset, str]):
            id (Union[Unset, str]):
            is_active (Union[Unset, bool]):
            name (Union[Unset, str]):
            updated_at (Union[Unset, str]):
            url (Union[Unset, str]):
            user_id (Union[Unset, str]):
     """

    created_at: Union[Unset, str] = UNSET
    group_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at

        group_id = self.group_id

        id = self.id

        is_active = self.is_active

        name = self.name

        updated_at = self.updated_at

        url = self.url

        user_id = self.user_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if group_id is not UNSET:
            field_dict["groupId"] = group_id
        if id is not UNSET:
            field_dict["id"] = id
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if name is not UNSET:
            field_dict["name"] = name
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if url is not UNSET:
            field_dict["url"] = url
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = d.pop("createdAt", UNSET)

        group_id = d.pop("groupId", UNSET)

        id = d.pop("id", UNSET)

        is_active = d.pop("isActive", UNSET)

        name = d.pop("name", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        url = d.pop("url", UNSET)

        user_id = d.pop("userId", UNSET)

        repo_notifier_out = cls(
            created_at=created_at,
            group_id=group_id,
            id=id,
            is_active=is_active,
            name=name,
            updated_at=updated_at,
            url=url,
            user_id=user_id,
        )


        repo_notifier_out.additional_properties = d
        return repo_notifier_out

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
