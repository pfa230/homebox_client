from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.repo_location_summary import RepoLocationSummary





T = TypeVar("T", bound="RepoLocationOut")



@_attrs_define
class RepoLocationOut:
    """ 
        Attributes:
            children (Union[Unset, list['RepoLocationSummary']]):
            created_at (Union[Unset, str]):
            description (Union[Unset, str]):
            id (Union[Unset, str]):
            name (Union[Unset, str]):
            parent (Union[Unset, RepoLocationSummary]):
            total_price (Union[Unset, float]):
            updated_at (Union[Unset, str]):
     """

    children: Union[Unset, list['RepoLocationSummary']] = UNSET
    created_at: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    parent: Union[Unset, 'RepoLocationSummary'] = UNSET
    total_price: Union[Unset, float] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.repo_location_summary import RepoLocationSummary
        children: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)



        created_at = self.created_at

        description = self.description

        id = self.id

        name = self.name

        parent: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()

        total_price = self.total_price

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if children is not UNSET:
            field_dict["children"] = children
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if parent is not UNSET:
            field_dict["parent"] = parent
        if total_price is not UNSET:
            field_dict["totalPrice"] = total_price
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.repo_location_summary import RepoLocationSummary
        d = dict(src_dict)
        children = []
        _children = d.pop("children", UNSET)
        for children_item_data in (_children or []):
            children_item = RepoLocationSummary.from_dict(children_item_data)



            children.append(children_item)


        created_at = d.pop("createdAt", UNSET)

        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _parent = d.pop("parent", UNSET)
        parent: Union[Unset, RepoLocationSummary]
        if isinstance(_parent,  Unset):
            parent = UNSET
        else:
            parent = RepoLocationSummary.from_dict(_parent)




        total_price = d.pop("totalPrice", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        repo_location_out = cls(
            children=children,
            created_at=created_at,
            description=description,
            id=id,
            name=name,
            parent=parent,
            total_price=total_price,
            updated_at=updated_at,
        )


        repo_location_out.additional_properties = d
        return repo_location_out

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
