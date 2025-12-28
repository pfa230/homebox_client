from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.ent_item_template import EntItemTemplate
  from ..models.ent_location import EntLocation
  from ..models.ent_notifier import EntNotifier
  from ..models.ent_user import EntUser
  from ..models.ent_label import EntLabel
  from ..models.ent_group_invitation_token import EntGroupInvitationToken
  from ..models.ent_item import EntItem





T = TypeVar("T", bound="EntGroupEdges")



@_attrs_define
class EntGroupEdges:
    """ 
        Attributes:
            invitation_tokens (Union[Unset, list['EntGroupInvitationToken']]): InvitationTokens holds the value of the
                invitation_tokens edge.
            item_templates (Union[Unset, list['EntItemTemplate']]): ItemTemplates holds the value of the item_templates
                edge.
            items (Union[Unset, list['EntItem']]): Items holds the value of the items edge.
            labels (Union[Unset, list['EntLabel']]): Labels holds the value of the labels edge.
            locations (Union[Unset, list['EntLocation']]): Locations holds the value of the locations edge.
            notifiers (Union[Unset, list['EntNotifier']]): Notifiers holds the value of the notifiers edge.
            users (Union[Unset, list['EntUser']]): Users holds the value of the users edge.
     """

    invitation_tokens: Union[Unset, list['EntGroupInvitationToken']] = UNSET
    item_templates: Union[Unset, list['EntItemTemplate']] = UNSET
    items: Union[Unset, list['EntItem']] = UNSET
    labels: Union[Unset, list['EntLabel']] = UNSET
    locations: Union[Unset, list['EntLocation']] = UNSET
    notifiers: Union[Unset, list['EntNotifier']] = UNSET
    users: Union[Unset, list['EntUser']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ent_item_template import EntItemTemplate
        from ..models.ent_location import EntLocation
        from ..models.ent_notifier import EntNotifier
        from ..models.ent_user import EntUser
        from ..models.ent_label import EntLabel
        from ..models.ent_group_invitation_token import EntGroupInvitationToken
        from ..models.ent_item import EntItem
        invitation_tokens: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.invitation_tokens, Unset):
            invitation_tokens = []
            for invitation_tokens_item_data in self.invitation_tokens:
                invitation_tokens_item = invitation_tokens_item_data.to_dict()
                invitation_tokens.append(invitation_tokens_item)



        item_templates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.item_templates, Unset):
            item_templates = []
            for item_templates_item_data in self.item_templates:
                item_templates_item = item_templates_item_data.to_dict()
                item_templates.append(item_templates_item)



        items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)



        labels: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)



        locations: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.locations, Unset):
            locations = []
            for locations_item_data in self.locations:
                locations_item = locations_item_data.to_dict()
                locations.append(locations_item)



        notifiers: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.notifiers, Unset):
            notifiers = []
            for notifiers_item_data in self.notifiers:
                notifiers_item = notifiers_item_data.to_dict()
                notifiers.append(notifiers_item)



        users: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if invitation_tokens is not UNSET:
            field_dict["invitation_tokens"] = invitation_tokens
        if item_templates is not UNSET:
            field_dict["item_templates"] = item_templates
        if items is not UNSET:
            field_dict["items"] = items
        if labels is not UNSET:
            field_dict["labels"] = labels
        if locations is not UNSET:
            field_dict["locations"] = locations
        if notifiers is not UNSET:
            field_dict["notifiers"] = notifiers
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ent_item_template import EntItemTemplate
        from ..models.ent_location import EntLocation
        from ..models.ent_notifier import EntNotifier
        from ..models.ent_user import EntUser
        from ..models.ent_label import EntLabel
        from ..models.ent_group_invitation_token import EntGroupInvitationToken
        from ..models.ent_item import EntItem
        d = dict(src_dict)
        invitation_tokens = []
        _invitation_tokens = d.pop("invitation_tokens", UNSET)
        for invitation_tokens_item_data in (_invitation_tokens or []):
            invitation_tokens_item = EntGroupInvitationToken.from_dict(invitation_tokens_item_data)



            invitation_tokens.append(invitation_tokens_item)


        item_templates = []
        _item_templates = d.pop("item_templates", UNSET)
        for item_templates_item_data in (_item_templates or []):
            item_templates_item = EntItemTemplate.from_dict(item_templates_item_data)



            item_templates.append(item_templates_item)


        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in (_items or []):
            items_item = EntItem.from_dict(items_item_data)



            items.append(items_item)


        labels = []
        _labels = d.pop("labels", UNSET)
        for labels_item_data in (_labels or []):
            labels_item = EntLabel.from_dict(labels_item_data)



            labels.append(labels_item)


        locations = []
        _locations = d.pop("locations", UNSET)
        for locations_item_data in (_locations or []):
            locations_item = EntLocation.from_dict(locations_item_data)



            locations.append(locations_item)


        notifiers = []
        _notifiers = d.pop("notifiers", UNSET)
        for notifiers_item_data in (_notifiers or []):
            notifiers_item = EntNotifier.from_dict(notifiers_item_data)



            notifiers.append(notifiers_item)


        users = []
        _users = d.pop("users", UNSET)
        for users_item_data in (_users or []):
            users_item = EntUser.from_dict(users_item_data)



            users.append(users_item)


        ent_group_edges = cls(
            invitation_tokens=invitation_tokens,
            item_templates=item_templates,
            items=items,
            labels=labels,
            locations=locations,
            notifiers=notifiers,
            users=users,
        )


        ent_group_edges.additional_properties = d
        return ent_group_edges

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
