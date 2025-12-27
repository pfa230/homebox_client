from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.ent_group import EntGroup
  from ..models.ent_item import EntItem





T = TypeVar("T", bound="EntLabelEdges")



@_attrs_define
class EntLabelEdges:
    """ 
        Attributes:
            group (Union[Unset, EntGroup]):
            items (Union[Unset, list['EntItem']]): Items holds the value of the items edge.
     """

    group: Union[Unset, 'EntGroup'] = UNSET
    items: Union[Unset, list['EntItem']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ent_group import EntGroup
        from ..models.ent_item import EntItem
        group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if group is not UNSET:
            field_dict["group"] = group
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ent_group import EntGroup
        from ..models.ent_item import EntItem
        d = dict(src_dict)
        _group = d.pop("group", UNSET)
        group: Union[Unset, EntGroup]
        if isinstance(_group,  Unset):
            group = UNSET
        else:
            group = EntGroup.from_dict(_group)




        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in (_items or []):
            items_item = EntItem.from_dict(items_item_data)



            items.append(items_item)


        ent_label_edges = cls(
            group=group,
            items=items,
        )


        ent_label_edges.additional_properties = d
        return ent_label_edges

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
