from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.ent_group import EntGroup
  from ..models.ent_auth_tokens import EntAuthTokens
  from ..models.ent_notifier import EntNotifier





T = TypeVar("T", bound="EntUserEdges")



@_attrs_define
class EntUserEdges:
    """ 
        Attributes:
            auth_tokens (Union[Unset, list['EntAuthTokens']]): AuthTokens holds the value of the auth_tokens edge.
            group (Union[Unset, EntGroup]):
            notifiers (Union[Unset, list['EntNotifier']]): Notifiers holds the value of the notifiers edge.
     """

    auth_tokens: Union[Unset, list['EntAuthTokens']] = UNSET
    group: Union[Unset, 'EntGroup'] = UNSET
    notifiers: Union[Unset, list['EntNotifier']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ent_group import EntGroup
        from ..models.ent_auth_tokens import EntAuthTokens
        from ..models.ent_notifier import EntNotifier
        auth_tokens: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.auth_tokens, Unset):
            auth_tokens = []
            for auth_tokens_item_data in self.auth_tokens:
                auth_tokens_item = auth_tokens_item_data.to_dict()
                auth_tokens.append(auth_tokens_item)



        group: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        notifiers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.notifiers, Unset):
            notifiers = []
            for notifiers_item_data in self.notifiers:
                notifiers_item = notifiers_item_data.to_dict()
                notifiers.append(notifiers_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if auth_tokens is not UNSET:
            field_dict["auth_tokens"] = auth_tokens
        if group is not UNSET:
            field_dict["group"] = group
        if notifiers is not UNSET:
            field_dict["notifiers"] = notifiers

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ent_group import EntGroup
        from ..models.ent_auth_tokens import EntAuthTokens
        from ..models.ent_notifier import EntNotifier
        d = dict(src_dict)
        auth_tokens = []
        _auth_tokens = d.pop("auth_tokens", UNSET)
        for auth_tokens_item_data in (_auth_tokens or []):
            auth_tokens_item = EntAuthTokens.from_dict(auth_tokens_item_data)



            auth_tokens.append(auth_tokens_item)


        _group = d.pop("group", UNSET)
        group: Union[Unset, EntGroup]
        if isinstance(_group,  Unset):
            group = UNSET
        else:
            group = EntGroup.from_dict(_group)




        notifiers = []
        _notifiers = d.pop("notifiers", UNSET)
        for notifiers_item_data in (_notifiers or []):
            notifiers_item = EntNotifier.from_dict(notifiers_item_data)



            notifiers.append(notifiers_item)


        ent_user_edges = cls(
            auth_tokens=auth_tokens,
            group=group,
            notifiers=notifiers,
        )


        ent_user_edges.additional_properties = d
        return ent_user_edges

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
