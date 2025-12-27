from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union






T = TypeVar("T", bound="V1ItemTemplateCreateItemRequest")



@_attrs_define
class V1ItemTemplateCreateItemRequest:
    """ 
        Attributes:
            location_id (str):
            name (str):
            description (Union[Unset, str]):
            label_ids (Union[Unset, list[str]]):
            quantity (Union[Unset, int]):
     """

    location_id: str
    name: str
    description: Union[Unset, str] = UNSET
    label_ids: Union[Unset, list[str]] = UNSET
    quantity: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        location_id = self.location_id

        name = self.name

        description = self.description

        label_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.label_ids, Unset):
            label_ids = self.label_ids



        quantity = self.quantity


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "locationId": location_id,
            "name": name,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if label_ids is not UNSET:
            field_dict["labelIds"] = label_ids
        if quantity is not UNSET:
            field_dict["quantity"] = quantity

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        location_id = d.pop("locationId")

        name = d.pop("name")

        description = d.pop("description", UNSET)

        label_ids = cast(list[str], d.pop("labelIds", UNSET))


        quantity = d.pop("quantity", UNSET)

        v1_item_template_create_item_request = cls(
            location_id=location_id,
            name=name,
            description=description,
            label_ids=label_ids,
            quantity=quantity,
        )


        v1_item_template_create_item_request.additional_properties = d
        return v1_item_template_create_item_request

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
