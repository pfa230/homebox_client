from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.ent_notifier_edges import EntNotifierEdges





T = TypeVar("T", bound="EntNotifier")



@_attrs_define
class EntNotifier:
    """ 
        Attributes:
            created_at (Union[Unset, str]): CreatedAt holds the value of the "created_at" field.
            edges (Union[Unset, EntNotifierEdges]):
            group_id (Union[Unset, str]): GroupID holds the value of the "group_id" field.
            id (Union[Unset, str]): ID of the ent.
            is_active (Union[Unset, bool]): IsActive holds the value of the "is_active" field.
            name (Union[Unset, str]): Name holds the value of the "name" field.
            updated_at (Union[Unset, str]): UpdatedAt holds the value of the "updated_at" field.
            user_id (Union[Unset, str]): UserID holds the value of the "user_id" field.
     """

    created_at: Union[Unset, str] = UNSET
    edges: Union[Unset, 'EntNotifierEdges'] = UNSET
    group_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    user_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ent_notifier_edges import EntNotifierEdges
        created_at = self.created_at

        edges: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.edges, Unset):
            edges = self.edges.to_dict()

        group_id = self.group_id

        id = self.id

        is_active = self.is_active

        name = self.name

        updated_at = self.updated_at

        user_id = self.user_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if edges is not UNSET:
            field_dict["edges"] = edges
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if id is not UNSET:
            field_dict["id"] = id
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if name is not UNSET:
            field_dict["name"] = name
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if user_id is not UNSET:
            field_dict["user_id"] = user_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ent_notifier_edges import EntNotifierEdges
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        _edges = d.pop("edges", UNSET)
        edges: Union[Unset, EntNotifierEdges]
        if isinstance(_edges,  Unset):
            edges = UNSET
        else:
            edges = EntNotifierEdges.from_dict(_edges)




        group_id = d.pop("group_id", UNSET)

        id = d.pop("id", UNSET)

        is_active = d.pop("is_active", UNSET)

        name = d.pop("name", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        user_id = d.pop("user_id", UNSET)

        ent_notifier = cls(
            created_at=created_at,
            edges=edges,
            group_id=group_id,
            id=id,
            is_active=is_active,
            name=name,
            updated_at=updated_at,
            user_id=user_id,
        )


        ent_notifier.additional_properties = d
        return ent_notifier

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
