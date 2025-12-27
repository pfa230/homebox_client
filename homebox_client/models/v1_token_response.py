from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="V1TokenResponse")



@_attrs_define
class V1TokenResponse:
    """ 
        Attributes:
            attachment_token (Union[Unset, str]):
            expires_at (Union[Unset, str]):
            token (Union[Unset, str]):
     """

    attachment_token: Union[Unset, str] = UNSET
    expires_at: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        attachment_token = self.attachment_token

        expires_at = self.expires_at

        token = self.token


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if attachment_token is not UNSET:
            field_dict["attachmentToken"] = attachment_token
        if expires_at is not UNSET:
            field_dict["expiresAt"] = expires_at
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        attachment_token = d.pop("attachmentToken", UNSET)

        expires_at = d.pop("expiresAt", UNSET)

        token = d.pop("token", UNSET)

        v1_token_response = cls(
            attachment_token=attachment_token,
            expires_at=expires_at,
            token=token,
        )


        v1_token_response.additional_properties = d
        return v1_token_response

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
