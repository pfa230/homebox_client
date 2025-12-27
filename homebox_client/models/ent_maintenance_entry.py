from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.ent_maintenance_entry_edges import EntMaintenanceEntryEdges





T = TypeVar("T", bound="EntMaintenanceEntry")



@_attrs_define
class EntMaintenanceEntry:
    """ 
        Attributes:
            cost (Union[Unset, float]): Cost holds the value of the "cost" field.
            created_at (Union[Unset, str]): CreatedAt holds the value of the "created_at" field.
            date (Union[Unset, str]): Date holds the value of the "date" field.
            description (Union[Unset, str]): Description holds the value of the "description" field.
            edges (Union[Unset, EntMaintenanceEntryEdges]):
            id (Union[Unset, str]): ID of the ent.
            item_id (Union[Unset, str]): ItemID holds the value of the "item_id" field.
            name (Union[Unset, str]): Name holds the value of the "name" field.
            scheduled_date (Union[Unset, str]): ScheduledDate holds the value of the "scheduled_date" field.
            updated_at (Union[Unset, str]): UpdatedAt holds the value of the "updated_at" field.
     """

    cost: Union[Unset, float] = UNSET
    created_at: Union[Unset, str] = UNSET
    date: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    edges: Union[Unset, 'EntMaintenanceEntryEdges'] = UNSET
    id: Union[Unset, str] = UNSET
    item_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    scheduled_date: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ent_maintenance_entry_edges import EntMaintenanceEntryEdges
        cost = self.cost

        created_at = self.created_at

        date = self.date

        description = self.description

        edges: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.edges, Unset):
            edges = self.edges.to_dict()

        id = self.id

        item_id = self.item_id

        name = self.name

        scheduled_date = self.scheduled_date

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if cost is not UNSET:
            field_dict["cost"] = cost
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if date is not UNSET:
            field_dict["date"] = date
        if description is not UNSET:
            field_dict["description"] = description
        if edges is not UNSET:
            field_dict["edges"] = edges
        if id is not UNSET:
            field_dict["id"] = id
        if item_id is not UNSET:
            field_dict["item_id"] = item_id
        if name is not UNSET:
            field_dict["name"] = name
        if scheduled_date is not UNSET:
            field_dict["scheduled_date"] = scheduled_date
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ent_maintenance_entry_edges import EntMaintenanceEntryEdges
        d = dict(src_dict)
        cost = d.pop("cost", UNSET)

        created_at = d.pop("created_at", UNSET)

        date = d.pop("date", UNSET)

        description = d.pop("description", UNSET)

        _edges = d.pop("edges", UNSET)
        edges: Union[Unset, EntMaintenanceEntryEdges]
        if isinstance(_edges,  Unset):
            edges = UNSET
        else:
            edges = EntMaintenanceEntryEdges.from_dict(_edges)




        id = d.pop("id", UNSET)

        item_id = d.pop("item_id", UNSET)

        name = d.pop("name", UNSET)

        scheduled_date = d.pop("scheduled_date", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        ent_maintenance_entry = cls(
            cost=cost,
            created_at=created_at,
            date=date,
            description=description,
            edges=edges,
            id=id,
            item_id=item_id,
            name=name,
            scheduled_date=scheduled_date,
            updated_at=updated_at,
        )


        ent_maintenance_entry.additional_properties = d
        return ent_maintenance_entry

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
