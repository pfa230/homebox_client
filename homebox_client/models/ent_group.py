from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.ent_group_edges import EntGroupEdges





T = TypeVar("T", bound="EntGroup")



@_attrs_define
class EntGroup:
    """ 
        Attributes:
            created_at (Union[Unset, str]): CreatedAt holds the value of the "created_at" field.
            currency (Union[Unset, str]): Currency holds the value of the "currency" field.
            edges (Union[Unset, EntGroupEdges]):
            id (Union[Unset, str]): ID of the ent.
            name (Union[Unset, str]): Name holds the value of the "name" field.
            updated_at (Union[Unset, str]): UpdatedAt holds the value of the "updated_at" field.
     """

    created_at: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    edges: Union[Unset, 'EntGroupEdges'] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ent_group_edges import EntGroupEdges
        created_at = self.created_at

        currency = self.currency

        edges: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.edges, Unset):
            edges = self.edges.to_dict()

        id = self.id

        name = self.name

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if currency is not UNSET:
            field_dict["currency"] = currency
        if edges is not UNSET:
            field_dict["edges"] = edges
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ent_group_edges import EntGroupEdges
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        currency = d.pop("currency", UNSET)

        _edges = d.pop("edges", UNSET)
        edges: Union[Unset, EntGroupEdges]
        if isinstance(_edges,  Unset):
            edges = UNSET
        else:
            edges = EntGroupEdges.from_dict(_edges)




        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        ent_group = cls(
            created_at=created_at,
            currency=currency,
            edges=edges,
            id=id,
            name=name,
            updated_at=updated_at,
        )


        ent_group.additional_properties = d
        return ent_group

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
