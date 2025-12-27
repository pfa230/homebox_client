from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union






T = TypeVar("T", bound="RepoItemPatch")



@_attrs_define
class RepoItemPatch:
    """ 
        Attributes:
            id (Union[Unset, str]):
            label_ids (Union[None, Unset, list[str]]):
            location_id (Union[None, Unset, str]):
            quantity (Union[None, Unset, int]):
     """

    id: Union[Unset, str] = UNSET
    label_ids: Union[None, Unset, list[str]] = UNSET
    location_id: Union[None, Unset, str] = UNSET
    quantity: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        label_ids: Union[None, Unset, list[str]]
        if isinstance(self.label_ids, Unset):
            label_ids = UNSET
        elif isinstance(self.label_ids, list):
            label_ids = self.label_ids


        else:
            label_ids = self.label_ids

        location_id: Union[None, Unset, str]
        if isinstance(self.location_id, Unset):
            location_id = UNSET
        else:
            location_id = self.location_id

        quantity: Union[None, Unset, int]
        if isinstance(self.quantity, Unset):
            quantity = UNSET
        else:
            quantity = self.quantity


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if label_ids is not UNSET:
            field_dict["labelIds"] = label_ids
        if location_id is not UNSET:
            field_dict["locationId"] = location_id
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        def _parse_label_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                label_ids_type_0 = cast(list[str], data)

                return label_ids_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        label_ids = _parse_label_ids(d.pop("labelIds", UNSET))


        def _parse_location_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        location_id = _parse_location_id(d.pop("locationId", UNSET))


        def _parse_quantity(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        quantity = _parse_quantity(d.pop("quantity", UNSET))


        repo_item_patch = cls(
            id=id,
            label_ids=label_ids,
            location_id=location_id,
            quantity=quantity,
        )


        repo_item_patch.additional_properties = d
        return repo_item_patch

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
