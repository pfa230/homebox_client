from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="V1Build")



@_attrs_define
class V1Build:
    """ 
        Attributes:
            build_time (Union[Unset, str]):
            commit (Union[Unset, str]):
            version (Union[Unset, str]):
     """

    build_time: Union[Unset, str] = UNSET
    commit: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        build_time = self.build_time

        commit = self.commit

        version = self.version


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if build_time is not UNSET:
            field_dict["buildTime"] = build_time
        if commit is not UNSET:
            field_dict["commit"] = commit
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        build_time = d.pop("buildTime", UNSET)

        commit = d.pop("commit", UNSET)

        version = d.pop("version", UNSET)

        v1_build = cls(
            build_time=build_time,
            commit=commit,
            version=version,
        )


        v1_build.additional_properties = d
        return v1_build

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
