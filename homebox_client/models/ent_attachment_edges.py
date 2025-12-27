from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.ent_attachment import EntAttachment
  from ..models.ent_item import EntItem





T = TypeVar("T", bound="EntAttachmentEdges")



@_attrs_define
class EntAttachmentEdges:
    """ 
        Attributes:
            item (Union[Unset, EntItem]):
            thumbnail (Union[Unset, EntAttachment]):
     """

    item: Union[Unset, 'EntItem'] = UNSET
    thumbnail: Union[Unset, 'EntAttachment'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ent_attachment import EntAttachment
        from ..models.ent_item import EntItem
        item: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.item, Unset):
            item = self.item.to_dict()

        thumbnail: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.thumbnail, Unset):
            thumbnail = self.thumbnail.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if item is not UNSET:
            field_dict["item"] = item
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ent_attachment import EntAttachment
        from ..models.ent_item import EntItem
        d = dict(src_dict)
        _item = d.pop("item", UNSET)
        item: Union[Unset, EntItem]
        if isinstance(_item,  Unset):
            item = UNSET
        else:
            item = EntItem.from_dict(_item)




        _thumbnail = d.pop("thumbnail", UNSET)
        thumbnail: Union[Unset, EntAttachment]
        if isinstance(_thumbnail,  Unset):
            thumbnail = UNSET
        else:
            thumbnail = EntAttachment.from_dict(_thumbnail)




        ent_attachment_edges = cls(
            item=item,
            thumbnail=thumbnail,
        )


        ent_attachment_edges.additional_properties = d
        return ent_attachment_edges

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
