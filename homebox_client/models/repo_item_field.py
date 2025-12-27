from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="RepoItemField")



@_attrs_define
class RepoItemField:
    """ 
        Attributes:
            boolean_value (Union[Unset, bool]):
            id (Union[Unset, str]):
            name (Union[Unset, str]):
            number_value (Union[Unset, int]):
            text_value (Union[Unset, str]):
            type_ (Union[Unset, str]):
     """

    boolean_value: Union[Unset, bool] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    number_value: Union[Unset, int] = UNSET
    text_value: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        boolean_value = self.boolean_value

        id = self.id

        name = self.name

        number_value = self.number_value

        text_value = self.text_value

        type_ = self.type_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if boolean_value is not UNSET:
            field_dict["booleanValue"] = boolean_value
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if number_value is not UNSET:
            field_dict["numberValue"] = number_value
        if text_value is not UNSET:
            field_dict["textValue"] = text_value
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        boolean_value = d.pop("booleanValue", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        number_value = d.pop("numberValue", UNSET)

        text_value = d.pop("textValue", UNSET)

        type_ = d.pop("type", UNSET)

        repo_item_field = cls(
            boolean_value=boolean_value,
            id=id,
            name=name,
            number_value=number_value,
            text_value=text_value,
            type_=type_,
        )


        repo_item_field.additional_properties = d
        return repo_item_field

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
