from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.ent_location import EntLocation
  from ..models.ent_group import EntGroup
  from ..models.ent_item_field import EntItemField
  from ..models.ent_label import EntLabel
  from ..models.ent_maintenance_entry import EntMaintenanceEntry
  from ..models.ent_attachment import EntAttachment
  from ..models.ent_item import EntItem





T = TypeVar("T", bound="EntItemEdges")



@_attrs_define
class EntItemEdges:
    """ 
        Attributes:
            attachments (Union[Unset, list['EntAttachment']]): Attachments holds the value of the attachments edge.
            children (Union[Unset, list['EntItem']]): Children holds the value of the children edge.
            fields (Union[Unset, list['EntItemField']]): Fields holds the value of the fields edge.
            group (Union[Unset, EntGroup]):
            label (Union[Unset, list['EntLabel']]): Label holds the value of the label edge.
            location (Union[Unset, EntLocation]):
            maintenance_entries (Union[Unset, list['EntMaintenanceEntry']]): MaintenanceEntries holds the value of the
                maintenance_entries edge.
            parent (Union[Unset, EntItem]):
     """

    attachments: Union[Unset, list['EntAttachment']] = UNSET
    children: Union[Unset, list['EntItem']] = UNSET
    fields: Union[Unset, list['EntItemField']] = UNSET
    group: Union[Unset, 'EntGroup'] = UNSET
    label: Union[Unset, list['EntLabel']] = UNSET
    location: Union[Unset, 'EntLocation'] = UNSET
    maintenance_entries: Union[Unset, list['EntMaintenanceEntry']] = UNSET
    parent: Union[Unset, 'EntItem'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ent_location import EntLocation
        from ..models.ent_group import EntGroup
        from ..models.ent_item_field import EntItemField
        from ..models.ent_label import EntLabel
        from ..models.ent_maintenance_entry import EntMaintenanceEntry
        from ..models.ent_attachment import EntAttachment
        from ..models.ent_item import EntItem
        attachments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)



        children: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.children, Unset):
            children = []
            for children_item_data in self.children:
                children_item = children_item_data.to_dict()
                children.append(children_item)



        fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)



        group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        label: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.label, Unset):
            label = []
            for label_item_data in self.label:
                label_item = label_item_data.to_dict()
                label.append(label_item)



        location: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        maintenance_entries: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.maintenance_entries, Unset):
            maintenance_entries = []
            for maintenance_entries_item_data in self.maintenance_entries:
                maintenance_entries_item = maintenance_entries_item_data.to_dict()
                maintenance_entries.append(maintenance_entries_item)



        parent: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent, Unset):
            parent = self.parent.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if children is not UNSET:
            field_dict["children"] = children
        if fields is not UNSET:
            field_dict["fields"] = fields
        if group is not UNSET:
            field_dict["group"] = group
        if label is not UNSET:
            field_dict["label"] = label
        if location is not UNSET:
            field_dict["location"] = location
        if maintenance_entries is not UNSET:
            field_dict["maintenance_entries"] = maintenance_entries
        if parent is not UNSET:
            field_dict["parent"] = parent

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ent_location import EntLocation
        from ..models.ent_group import EntGroup
        from ..models.ent_item_field import EntItemField
        from ..models.ent_label import EntLabel
        from ..models.ent_maintenance_entry import EntMaintenanceEntry
        from ..models.ent_attachment import EntAttachment
        from ..models.ent_item import EntItem
        d = dict(src_dict)
        attachments = []
        _attachments = d.pop("attachments", UNSET)
        for attachments_item_data in (_attachments or []):
            attachments_item = EntAttachment.from_dict(attachments_item_data)



            attachments.append(attachments_item)


        children = []
        _children = d.pop("children", UNSET)
        for children_item_data in (_children or []):
            children_item = EntItem.from_dict(children_item_data)



            children.append(children_item)


        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in (_fields or []):
            fields_item = EntItemField.from_dict(fields_item_data)



            fields.append(fields_item)


        _group = d.pop("group", UNSET)
        group: Union[Unset, EntGroup]
        if isinstance(_group,  Unset):
            group = UNSET
        else:
            group = EntGroup.from_dict(_group)




        label = []
        _label = d.pop("label", UNSET)
        for label_item_data in (_label or []):
            label_item = EntLabel.from_dict(label_item_data)



            label.append(label_item)


        _location = d.pop("location", UNSET)
        location: Union[Unset, EntLocation]
        if isinstance(_location,  Unset):
            location = UNSET
        else:
            location = EntLocation.from_dict(_location)




        maintenance_entries = []
        _maintenance_entries = d.pop("maintenance_entries", UNSET)
        for maintenance_entries_item_data in (_maintenance_entries or []):
            maintenance_entries_item = EntMaintenanceEntry.from_dict(maintenance_entries_item_data)



            maintenance_entries.append(maintenance_entries_item)


        _parent = d.pop("parent", UNSET)
        parent: Union[Unset, EntItem]
        if isinstance(_parent,  Unset):
            parent = UNSET
        else:
            parent = EntItem.from_dict(_parent)




        ent_item_edges = cls(
            attachments=attachments,
            children=children,
            fields=fields,
            group=group,
            label=label,
            location=location,
            maintenance_entries=maintenance_entries,
            parent=parent,
        )


        ent_item_edges.additional_properties = d
        return ent_item_edges

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
