from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json
from .. import types

from ..types import UNSET, Unset

from ..types import File, FileTypes
from ..types import UNSET, Unset
from io import BytesIO
from typing import Union






T = TypeVar("T", bound="PostV1ItemsIdAttachmentsBody")



@_attrs_define
class PostV1ItemsIdAttachmentsBody:
    """ 
        Attributes:
            file (File): File attachment
            name (str): name of the file including extension
            type_ (Union[Unset, str]): Type of file
            primary (Union[Unset, bool]): Is this the primary attachment
     """

    file: File
    name: str
    type_: Union[Unset, str] = UNSET
    primary: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        file = self.file.to_tuple()


        name = self.name

        type_ = self.type_

        primary = self.primary


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "file": file,
            "name": name,
        })
        if type_ is not UNSET:
            field_dict["type"] = type_
        if primary is not UNSET:
            field_dict["primary"] = primary

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("file", self.file.to_tuple()))



        files.append(("name", (None, str(self.name).encode(), "text/plain")))



        if not isinstance(self.type_, Unset):
            files.append(("type", (None, str(self.type_).encode(), "text/plain")))



        if not isinstance(self.primary, Unset):
            files.append(("primary", (None, str(self.primary).encode(), "text/plain")))




        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        file = File(
             payload = BytesIO(d.pop("file"))
        )




        name = d.pop("name")

        type_ = d.pop("type", UNSET)

        primary = d.pop("primary", UNSET)

        post_v1_items_id_attachments_body = cls(
            file=file,
            name=name,
            type_=type_,
            primary=primary,
        )


        post_v1_items_id_attachments_body.additional_properties = d
        return post_v1_items_id_attachments_body

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
