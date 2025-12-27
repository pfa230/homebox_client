from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="V1LoginForm")



@_attrs_define
class V1LoginForm:
    """ 
        Attributes:
            password (Union[Unset, str]):  Example: admin.
            stay_logged_in (Union[Unset, bool]):
            username (Union[Unset, str]):  Example: admin@admin.com.
     """

    password: Union[Unset, str] = UNSET
    stay_logged_in: Union[Unset, bool] = UNSET
    username: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        password = self.password

        stay_logged_in = self.stay_logged_in

        username = self.username


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if password is not UNSET:
            field_dict["password"] = password
        if stay_logged_in is not UNSET:
            field_dict["stayLoggedIn"] = stay_logged_in
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        password = d.pop("password", UNSET)

        stay_logged_in = d.pop("stayLoggedIn", UNSET)

        username = d.pop("username", UNSET)

        v1_login_form = cls(
            password=password,
            stay_logged_in=stay_logged_in,
            username=username,
        )


        v1_login_form.additional_properties = d
        return v1_login_form

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
