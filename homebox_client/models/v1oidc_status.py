from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="V1OIDCStatus")



@_attrs_define
class V1OIDCStatus:
    """ 
        Attributes:
            allow_local (Union[Unset, bool]):
            auto_redirect (Union[Unset, bool]):
            button_text (Union[Unset, str]):
            enabled (Union[Unset, bool]):
     """

    allow_local: Union[Unset, bool] = UNSET
    auto_redirect: Union[Unset, bool] = UNSET
    button_text: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        allow_local = self.allow_local

        auto_redirect = self.auto_redirect

        button_text = self.button_text

        enabled = self.enabled


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if allow_local is not UNSET:
            field_dict["allowLocal"] = allow_local
        if auto_redirect is not UNSET:
            field_dict["autoRedirect"] = auto_redirect
        if button_text is not UNSET:
            field_dict["buttonText"] = button_text
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allow_local = d.pop("allowLocal", UNSET)

        auto_redirect = d.pop("autoRedirect", UNSET)

        button_text = d.pop("buttonText", UNSET)

        enabled = d.pop("enabled", UNSET)

        v1oidc_status = cls(
            allow_local=allow_local,
            auto_redirect=auto_redirect,
            button_text=button_text,
            enabled=enabled,
        )


        v1oidc_status.additional_properties = d
        return v1oidc_status

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
