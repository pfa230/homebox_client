from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="RepoItemCreate")



@_attrs_define
class RepoItemCreate:
    """ 
        Attributes:
            name (str):
            description (Union[Unset, str]):
            label_ids (Union[Unset, list[str]]):
            location_id (Union[Unset, str]): Edges
            parent_id (Union[None, Unset, str]):
            quantity (Union[Unset, int]):
     """

    name: str
    description: Union[Unset, str] = UNSET
    label_ids: Union[Unset, list[str]] = UNSET
    location_id: Union[Unset, str] = UNSET
    parent_id: Union[None, Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        label_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.label_ids, Unset):
            label_ids = self.label_ids



        location_id = self.location_id

        parent_id: Union[None, Unset, str]
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        quantity = self.quantity


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if label_ids is not UNSET:
            field_dict["labelIds"] = label_ids
        if location_id is not UNSET:
            field_dict["locationId"] = location_id
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description", UNSET)

        label_ids = cast(list[str], d.pop("labelIds", UNSET))


        location_id = d.pop("locationId", UNSET)

        def _parse_parent_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))


        quantity = d.pop("quantity", UNSET)

        repo_item_create = cls(
            name=name,
            description=description,
            label_ids=label_ids,
            location_id=location_id,
            parent_id=parent_id,
            quantity=quantity,
        )


        repo_item_create.additional_properties = d
        return repo_item_create

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
