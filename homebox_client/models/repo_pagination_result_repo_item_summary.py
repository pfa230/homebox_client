from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.repo_item_summary import RepoItemSummary





T = TypeVar("T", bound="RepoPaginationResultRepoItemSummary")



@_attrs_define
class RepoPaginationResultRepoItemSummary:
    """ 
        Attributes:
            items (Union[Unset, list['RepoItemSummary']]):
            page (Union[Unset, int]):
            page_size (Union[Unset, int]):
            total (Union[Unset, int]):
     """

    items: Union[Unset, list['RepoItemSummary']] = UNSET
    page: Union[Unset, int] = UNSET
    page_size: Union[Unset, int] = UNSET
    total: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.repo_item_summary import RepoItemSummary
        items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)



        page = self.page

        page_size = self.page_size

        total = self.total


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if items is not UNSET:
            field_dict["items"] = items
        if page is not UNSET:
            field_dict["page"] = page
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if total is not UNSET:
            field_dict["total"] = total

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.repo_item_summary import RepoItemSummary
        d = dict(src_dict)
        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in (_items or []):
            items_item = RepoItemSummary.from_dict(items_item_data)



            items.append(items_item)


        page = d.pop("page", UNSET)

        page_size = d.pop("pageSize", UNSET)

        total = d.pop("total", UNSET)

        repo_pagination_result_repo_item_summary = cls(
            items=items,
            page=page,
            page_size=page_size,
            total=total,
        )


        repo_pagination_result_repo_item_summary.additional_properties = d
        return repo_pagination_result_repo_item_summary

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
