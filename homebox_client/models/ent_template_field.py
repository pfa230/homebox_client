from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.templatefield_type import TemplatefieldType
from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.ent_template_field_edges import EntTemplateFieldEdges





T = TypeVar("T", bound="EntTemplateField")



@_attrs_define
class EntTemplateField:
    """ 
        Attributes:
            created_at (Union[Unset, str]): CreatedAt holds the value of the "created_at" field.
            description (Union[Unset, str]): Description holds the value of the "description" field.
            edges (Union[Unset, EntTemplateFieldEdges]):
            id (Union[Unset, str]): ID of the ent.
            name (Union[Unset, str]): Name holds the value of the "name" field.
            text_value (Union[Unset, str]): TextValue holds the value of the "text_value" field.
            type_ (Union[Unset, TemplatefieldType]):
            updated_at (Union[Unset, str]): UpdatedAt holds the value of the "updated_at" field.
     """

    created_at: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    edges: Union[Unset, 'EntTemplateFieldEdges'] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    text_value: Union[Unset, str] = UNSET
    type_: Union[Unset, TemplatefieldType] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ent_template_field_edges import EntTemplateFieldEdges
        created_at = self.created_at

        description = self.description

        edges: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.edges, Unset):
            edges = self.edges.to_dict()

        id = self.id

        name = self.name

        text_value = self.text_value

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
        if description is not UNSET:
            field_dict["description"] = description
        if edges is not UNSET:
            field_dict["edges"] = edges
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if text_value is not UNSET:
            field_dict["text_value"] = text_value
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ent_template_field_edges import EntTemplateFieldEdges
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        description = d.pop("description", UNSET)

        _edges = d.pop("edges", UNSET)
        edges: Union[Unset, EntTemplateFieldEdges]
        if isinstance(_edges,  Unset):
            edges = UNSET
        else:
            edges = EntTemplateFieldEdges.from_dict(_edges)




        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        text_value = d.pop("text_value", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, TemplatefieldType]
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = TemplatefieldType(_type_)




        updated_at = d.pop("updated_at", UNSET)

        ent_template_field = cls(
            created_at=created_at,
            description=description,
            edges=edges,
            id=id,
            name=name,
            text_value=text_value,
            type_=type_,
            updated_at=updated_at,
        )


        ent_template_field.additional_properties = d
        return ent_template_field

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
