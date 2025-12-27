from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.ent_attachment import EntAttachment





T = TypeVar("T", bound="RepoItemAttachment")



@_attrs_define
class RepoItemAttachment:
    """ 
        Attributes:
            created_at (Union[Unset, str]):
            id (Union[Unset, str]):
            mime_type (Union[Unset, str]):
            path (Union[Unset, str]):
            primary (Union[Unset, bool]):
            thumbnail (Union[Unset, EntAttachment]):
            title (Union[Unset, str]):
            type_ (Union[Unset, str]):
            updated_at (Union[Unset, str]):
     """

    created_at: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    mime_type: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    primary: Union[Unset, bool] = UNSET
    thumbnail: Union[Unset, 'EntAttachment'] = UNSET
    title: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ent_attachment import EntAttachment
        created_at = self.created_at

        id = self.id

        mime_type = self.mime_type

        path = self.path

        primary = self.primary

        thumbnail: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.thumbnail, Unset):
            thumbnail = self.thumbnail.to_dict()

        title = self.title

        type_ = self.type_

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if id is not UNSET:
            field_dict["id"] = id
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if path is not UNSET:
            field_dict["path"] = path
        if primary is not UNSET:
            field_dict["primary"] = primary
        if thumbnail is not UNSET:
            field_dict["thumbnail"] = thumbnail
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ent_attachment import EntAttachment
        d = dict(src_dict)
        created_at = d.pop("createdAt", UNSET)

        id = d.pop("id", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        path = d.pop("path", UNSET)

        primary = d.pop("primary", UNSET)

        _thumbnail = d.pop("thumbnail", UNSET)
        thumbnail: Union[Unset, EntAttachment]
        if isinstance(_thumbnail,  Unset):
            thumbnail = UNSET
        else:
            thumbnail = EntAttachment.from_dict(_thumbnail)




        title = d.pop("title", UNSET)

        type_ = d.pop("type", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        repo_item_attachment = cls(
            created_at=created_at,
            id=id,
            mime_type=mime_type,
            path=path,
            primary=primary,
            thumbnail=thumbnail,
            title=title,
            type_=type_,
            updated_at=updated_at,
        )


        repo_item_attachment.additional_properties = d
        return repo_item_attachment

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
