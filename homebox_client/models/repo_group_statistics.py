from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="RepoGroupStatistics")



@_attrs_define
class RepoGroupStatistics:
    """ 
        Attributes:
            total_item_price (Union[Unset, float]):
            total_items (Union[Unset, int]):
            total_labels (Union[Unset, int]):
            total_locations (Union[Unset, int]):
            total_users (Union[Unset, int]):
            total_with_warranty (Union[Unset, int]):
     """

    total_item_price: Union[Unset, float] = UNSET
    total_items: Union[Unset, int] = UNSET
    total_labels: Union[Unset, int] = UNSET
    total_locations: Union[Unset, int] = UNSET
    total_users: Union[Unset, int] = UNSET
    total_with_warranty: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        total_item_price = self.total_item_price

        total_items = self.total_items

        total_labels = self.total_labels

        total_locations = self.total_locations

        total_users = self.total_users

        total_with_warranty = self.total_with_warranty


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if total_item_price is not UNSET:
            field_dict["totalItemPrice"] = total_item_price
        if total_items is not UNSET:
            field_dict["totalItems"] = total_items
        if total_labels is not UNSET:
            field_dict["totalLabels"] = total_labels
        if total_locations is not UNSET:
            field_dict["totalLocations"] = total_locations
        if total_users is not UNSET:
            field_dict["totalUsers"] = total_users
        if total_with_warranty is not UNSET:
            field_dict["totalWithWarranty"] = total_with_warranty

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_item_price = d.pop("totalItemPrice", UNSET)

        total_items = d.pop("totalItems", UNSET)

        total_labels = d.pop("totalLabels", UNSET)

        total_locations = d.pop("totalLocations", UNSET)

        total_users = d.pop("totalUsers", UNSET)

        total_with_warranty = d.pop("totalWithWarranty", UNSET)

        repo_group_statistics = cls(
            total_item_price=total_item_price,
            total_items=total_items,
            total_labels=total_labels,
            total_locations=total_locations,
            total_users=total_users,
            total_with_warranty=total_with_warranty,
        )


        repo_group_statistics.additional_properties = d
        return repo_group_statistics

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
