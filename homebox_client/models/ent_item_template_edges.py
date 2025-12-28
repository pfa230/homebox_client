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
  from ..models.ent_template_field import EntTemplateField
  from ..models.ent_location import EntLocation





T = TypeVar("T", bound="EntItemTemplateEdges")



@_attrs_define
class EntItemTemplateEdges:
    """ 
        Attributes:
            fields (Union[Unset, list['EntTemplateField']]): Fields holds the value of the fields edge.
            group (Union[Unset, EntGroup]):
            location (Union[Unset, EntLocation]):
     """

    fields: Union[Unset, list['EntTemplateField']] = UNSET
    group: Union[Unset, 'EntGroup'] = UNSET
    location: Union[Unset, 'EntLocation'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ent_group import EntGroup
        from ..models.ent_template_field import EntTemplateField
        from ..models.ent_location import EntLocation
        fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)



        group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        location: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if fields is not UNSET:
            field_dict["fields"] = fields
        if group is not UNSET:
            field_dict["group"] = group
        if location is not UNSET:
            field_dict["location"] = location

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ent_group import EntGroup
        from ..models.ent_template_field import EntTemplateField
        from ..models.ent_location import EntLocation
        d = dict(src_dict)
        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in (_fields or []):
            fields_item = EntTemplateField.from_dict(fields_item_data)



            fields.append(fields_item)


        _group = d.pop("group", UNSET)
        group: Union[Unset, EntGroup]
        if isinstance(_group,  Unset):
            group = UNSET
        else:
            group = EntGroup.from_dict(_group)




        _location = d.pop("location", UNSET)
        location: Union[Unset, EntLocation]
        if isinstance(_location,  Unset):
            location = UNSET
        else:
            location = EntLocation.from_dict(_location)




        ent_item_template_edges = cls(
            fields=fields,
            group=group,
            location=location,
        )


        ent_item_template_edges.additional_properties = d
        return ent_item_template_edges

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
