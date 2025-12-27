from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="V1ChangePassword")



@_attrs_define
class V1ChangePassword:
    """ 
        Attributes:
            current (Union[Unset, str]):
            new (Union[Unset, str]):
     """

    current: Union[Unset, str] = UNSET
    new: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        current = self.current

        new = self.new


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if current is not UNSET:
            field_dict["current"] = current
        if new is not UNSET:
            field_dict["new"] = new

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current = d.pop("current", UNSET)

        new = d.pop("new", UNSET)

        v1_change_password = cls(
            current=current,
            new=new,
        )


        v1_change_password.additional_properties = d
        return v1_change_password

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
