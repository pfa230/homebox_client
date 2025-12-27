from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.attachment_type import AttachmentType
from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.ent_attachment_edges import EntAttachmentEdges





T = TypeVar("T", bound="EntAttachment")



@_attrs_define
class EntAttachment:
    """ 
        Attributes:
            created_at (Union[Unset, str]): CreatedAt holds the value of the "created_at" field.
            edges (Union[Unset, EntAttachmentEdges]):
            id (Union[Unset, str]): ID of the ent.
            mime_type (Union[Unset, str]): MimeType holds the value of the "mime_type" field.
            path (Union[Unset, str]): Path holds the value of the "path" field.
            primary (Union[Unset, bool]): Primary holds the value of the "primary" field.
            title (Union[Unset, str]): Title holds the value of the "title" field.
            type_ (Union[Unset, AttachmentType]):
            updated_at (Union[Unset, str]): UpdatedAt holds the value of the "updated_at" field.
     """

    created_at: Union[Unset, str] = UNSET
    edges: Union[Unset, 'EntAttachmentEdges'] = UNSET
    id: Union[Unset, str] = UNSET
    mime_type: Union[Unset, str] = UNSET
    path: Union[Unset, str] = UNSET
    primary: Union[Unset, bool] = UNSET
    title: Union[Unset, str] = UNSET
    type_: Union[Unset, AttachmentType] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ent_attachment_edges import EntAttachmentEdges
        created_at = self.created_at

        edges: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.edges, Unset):
            edges = self.edges.to_dict()

        id = self.id

        mime_type = self.mime_type

        path = self.path

        primary = self.primary

        title = self.title

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if edges is not UNSET:
            field_dict["edges"] = edges
        if id is not UNSET:
            field_dict["id"] = id
        if mime_type is not UNSET:
            field_dict["mime_type"] = mime_type
        if path is not UNSET:
            field_dict["path"] = path
        if primary is not UNSET:
            field_dict["primary"] = primary
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ent_attachment_edges import EntAttachmentEdges
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        _edges = d.pop("edges", UNSET)
        edges: Union[Unset, EntAttachmentEdges]
        if isinstance(_edges,  Unset):
            edges = UNSET
        else:
            edges = EntAttachmentEdges.from_dict(_edges)




        id = d.pop("id", UNSET)

        mime_type = d.pop("mime_type", UNSET)

        path = d.pop("path", UNSET)

        primary = d.pop("primary", UNSET)

        title = d.pop("title", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, AttachmentType]
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = AttachmentType(_type_)




        updated_at = d.pop("updated_at", UNSET)

        ent_attachment = cls(
            created_at=created_at,
            edges=edges,
            id=id,
            mime_type=mime_type,
            path=path,
            primary=primary,
            title=title,
            type_=type_,
            updated_at=updated_at,
        )


        ent_attachment.additional_properties = d
        return ent_attachment

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
