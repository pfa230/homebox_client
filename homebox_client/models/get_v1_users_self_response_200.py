from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.repo_user_out import RepoUserOut





T = TypeVar("T", bound="GetV1UsersSelfResponse200")



@_attrs_define
class GetV1UsersSelfResponse200:
    """ 
        Attributes:
            item (Union[Unset, RepoUserOut]):
     """

    item: Union[Unset, 'RepoUserOut'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.repo_user_out import RepoUserOut
        item: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.item, Unset):
            item = self.item.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if item is not UNSET:
            field_dict["item"] = item

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.repo_user_out import RepoUserOut
        d = dict(src_dict)
        _item = d.pop("item", UNSET)
        item: Union[Unset, RepoUserOut]
        if isinstance(_item,  Unset):
            item = UNSET
        else:
            item = RepoUserOut.from_dict(_item)




        get_v1_users_self_response_200 = cls(
            item=item,
        )


        get_v1_users_self_response_200.additional_properties = d
        return get_v1_users_self_response_200

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
