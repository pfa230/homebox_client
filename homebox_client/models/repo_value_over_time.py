from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.repo_value_over_time_entry import RepoValueOverTimeEntry





T = TypeVar("T", bound="RepoValueOverTime")



@_attrs_define
class RepoValueOverTime:
    """ 
        Attributes:
            end (Union[Unset, str]):
            entries (Union[Unset, list['RepoValueOverTimeEntry']]):
            start (Union[Unset, str]):
            value_at_end (Union[Unset, float]):
            value_at_start (Union[Unset, float]):
     """

    end: Union[Unset, str] = UNSET
    entries: Union[Unset, list['RepoValueOverTimeEntry']] = UNSET
    start: Union[Unset, str] = UNSET
    value_at_end: Union[Unset, float] = UNSET
    value_at_start: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.repo_value_over_time_entry import RepoValueOverTimeEntry
        end = self.end

        entries: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.entries, Unset):
            entries = []
            for entries_item_data in self.entries:
                entries_item = entries_item_data.to_dict()
                entries.append(entries_item)



        start = self.start

        value_at_end = self.value_at_end

        value_at_start = self.value_at_start


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if end is not UNSET:
            field_dict["end"] = end
        if entries is not UNSET:
            field_dict["entries"] = entries
        if start is not UNSET:
            field_dict["start"] = start
        if value_at_end is not UNSET:
            field_dict["valueAtEnd"] = value_at_end
        if value_at_start is not UNSET:
            field_dict["valueAtStart"] = value_at_start

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.repo_value_over_time_entry import RepoValueOverTimeEntry
        d = dict(src_dict)
        end = d.pop("end", UNSET)

        entries = []
        _entries = d.pop("entries", UNSET)
        for entries_item_data in (_entries or []):
            entries_item = RepoValueOverTimeEntry.from_dict(entries_item_data)



            entries.append(entries_item)


        start = d.pop("start", UNSET)

        value_at_end = d.pop("valueAtEnd", UNSET)

        value_at_start = d.pop("valueAtStart", UNSET)

        repo_value_over_time = cls(
            end=end,
            entries=entries,
            start=start,
            value_at_end=value_at_end,
            value_at_start=value_at_start,
        )


        repo_value_over_time.additional_properties = d
        return repo_value_over_time

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
