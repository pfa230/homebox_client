from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="RepoMaintenanceEntryCreate")



@_attrs_define
class RepoMaintenanceEntryCreate:
    """ 
        Attributes:
            name (str):
            completed_date (Union[Unset, str]):
            cost (Union[Unset, str]):  Example: 0.
            description (Union[Unset, str]):
            scheduled_date (Union[Unset, str]):
     """

    name: str
    completed_date: Union[Unset, str] = UNSET
    cost: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    scheduled_date: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        completed_date = self.completed_date

        cost = self.cost

        description = self.description

        scheduled_date = self.scheduled_date


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
        })
        if completed_date is not UNSET:
            field_dict["completedDate"] = completed_date
        if cost is not UNSET:
            field_dict["cost"] = cost
        if description is not UNSET:
            field_dict["description"] = description
        if scheduled_date is not UNSET:
            field_dict["scheduledDate"] = scheduled_date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        completed_date = d.pop("completedDate", UNSET)

        cost = d.pop("cost", UNSET)

        description = d.pop("description", UNSET)

        scheduled_date = d.pop("scheduledDate", UNSET)

        repo_maintenance_entry_create = cls(
            name=name,
            completed_date=completed_date,
            cost=cost,
            description=description,
            scheduled_date=scheduled_date,
        )


        repo_maintenance_entry_create.additional_properties = d
        return repo_maintenance_entry_create

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
