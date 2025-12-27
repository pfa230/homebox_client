from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="RepoDuplicateOptions")



@_attrs_define
class RepoDuplicateOptions:
    """ 
        Attributes:
            copy_attachments (Union[Unset, bool]):
            copy_custom_fields (Union[Unset, bool]):
            copy_maintenance (Union[Unset, bool]):
            copy_prefix (Union[Unset, str]):
     """

    copy_attachments: Union[Unset, bool] = UNSET
    copy_custom_fields: Union[Unset, bool] = UNSET
    copy_maintenance: Union[Unset, bool] = UNSET
    copy_prefix: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        copy_attachments = self.copy_attachments

        copy_custom_fields = self.copy_custom_fields

        copy_maintenance = self.copy_maintenance

        copy_prefix = self.copy_prefix


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if copy_attachments is not UNSET:
            field_dict["copyAttachments"] = copy_attachments
        if copy_custom_fields is not UNSET:
            field_dict["copyCustomFields"] = copy_custom_fields
        if copy_maintenance is not UNSET:
            field_dict["copyMaintenance"] = copy_maintenance
        if copy_prefix is not UNSET:
            field_dict["copyPrefix"] = copy_prefix

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        copy_attachments = d.pop("copyAttachments", UNSET)

        copy_custom_fields = d.pop("copyCustomFields", UNSET)

        copy_maintenance = d.pop("copyMaintenance", UNSET)

        copy_prefix = d.pop("copyPrefix", UNSET)

        repo_duplicate_options = cls(
            copy_attachments=copy_attachments,
            copy_custom_fields=copy_custom_fields,
            copy_maintenance=copy_maintenance,
            copy_prefix=copy_prefix,
        )


        repo_duplicate_options.additional_properties = d
        return repo_duplicate_options

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
