from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.ent_user import EntUser
  from ..models.ent_group import EntGroup





T = TypeVar("T", bound="EntNotifierEdges")



@_attrs_define
class EntNotifierEdges:
    """ 
        Attributes:
            group (Union[Unset, EntGroup]):
            user (Union[Unset, EntUser]):
     """

    group: Union[Unset, 'EntGroup'] = UNSET
    user: Union[Unset, 'EntUser'] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ent_user import EntUser
        from ..models.ent_group import EntGroup
        group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        user: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.user, Unset):
            user = self.user.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if group is not UNSET:
            field_dict["group"] = group
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ent_user import EntUser
        from ..models.ent_group import EntGroup
        d = dict(src_dict)
        _group = d.pop("group", UNSET)
        group: Union[Unset, EntGroup]
        if isinstance(_group,  Unset):
            group = UNSET
        else:
            group = EntGroup.from_dict(_group)




        _user = d.pop("user", UNSET)
        user: Union[Unset, EntUser]
        if isinstance(_user,  Unset):
            user = UNSET
        else:
            user = EntUser.from_dict(_user)




        ent_notifier_edges = cls(
            group=group,
            user=user,
        )


        ent_notifier_edges.additional_properties = d
        return ent_notifier_edges

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
