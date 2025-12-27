from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.ent_item_template import EntItemTemplate





T = TypeVar("T", bound="EntTemplateFieldEdges")



@_attrs_define
class EntTemplateFieldEdges:
    """ 
        Attributes:
            item_template (Union[Unset, EntItemTemplate]):
     """

    item_template: Union[Unset, 'EntItemTemplate'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ent_item_template import EntItemTemplate
        item_template: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.item_template, Unset):
            item_template = self.item_template.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if item_template is not UNSET:
            field_dict["item_template"] = item_template

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ent_item_template import EntItemTemplate
        d = dict(src_dict)
        _item_template = d.pop("item_template", UNSET)
        item_template: Union[Unset, EntItemTemplate]
        if isinstance(_item_template,  Unset):
            item_template = UNSET
        else:
            item_template = EntItemTemplate.from_dict(_item_template)




        ent_template_field_edges = cls(
            item_template=item_template,
        )


        ent_template_field_edges.additional_properties = d
        return ent_template_field_edges

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
