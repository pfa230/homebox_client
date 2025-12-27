from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="RepoTemplateField")



@_attrs_define
class RepoTemplateField:
    """ 
        Attributes:
            id (Union[Unset, str]):
            name (Union[Unset, str]):
            text_value (Union[Unset, str]):
            type_ (Union[Unset, str]):
     """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    text_value: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        text_value = self.text_value

        type_ = self.type_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if text_value is not UNSET:
            field_dict["textValue"] = text_value
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        text_value = d.pop("textValue", UNSET)

        type_ = d.pop("type", UNSET)

        repo_template_field = cls(
            id=id,
            name=name,
            text_value=text_value,
            type_=type_,
        )


        repo_template_field.additional_properties = d
        return repo_template_field

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
