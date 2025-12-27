from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.itemfield_type import ItemfieldType
from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.ent_item_field_edges import EntItemFieldEdges





T = TypeVar("T", bound="EntItemField")



@_attrs_define
class EntItemField:
    """ 
        Attributes:
            boolean_value (Union[Unset, bool]): BooleanValue holds the value of the "boolean_value" field.
            created_at (Union[Unset, str]): CreatedAt holds the value of the "created_at" field.
            description (Union[Unset, str]): Description holds the value of the "description" field.
            edges (Union[Unset, EntItemFieldEdges]):
            id (Union[Unset, str]): ID of the ent.
            name (Union[Unset, str]): Name holds the value of the "name" field.
            number_value (Union[Unset, int]): NumberValue holds the value of the "number_value" field.
            text_value (Union[Unset, str]): TextValue holds the value of the "text_value" field.
            time_value (Union[Unset, str]): TimeValue holds the value of the "time_value" field.
            type_ (Union[Unset, ItemfieldType]):
            updated_at (Union[Unset, str]): UpdatedAt holds the value of the "updated_at" field.
     """

    boolean_value: Union[Unset, bool] = UNSET
    created_at: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    edges: Union[Unset, 'EntItemFieldEdges'] = UNSET
    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    number_value: Union[Unset, int] = UNSET
    text_value: Union[Unset, str] = UNSET
    time_value: Union[Unset, str] = UNSET
    type_: Union[Unset, ItemfieldType] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ent_item_field_edges import EntItemFieldEdges
        boolean_value = self.boolean_value

        created_at = self.created_at

        description = self.description

        edges: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.edges, Unset):
            edges = self.edges.to_dict()

        id = self.id

        name = self.name

        number_value = self.number_value

        text_value = self.text_value

        time_value = self.time_value

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if boolean_value is not UNSET:
            field_dict["boolean_value"] = boolean_value
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
        if number_value is not UNSET:
            field_dict["number_value"] = number_value
        if text_value is not UNSET:
            field_dict["text_value"] = text_value
        if time_value is not UNSET:
            field_dict["time_value"] = time_value
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ent_item_field_edges import EntItemFieldEdges
        d = dict(src_dict)
        boolean_value = d.pop("boolean_value", UNSET)

        created_at = d.pop("created_at", UNSET)

        description = d.pop("description", UNSET)

        _edges = d.pop("edges", UNSET)
        edges: Union[Unset, EntItemFieldEdges]
        if isinstance(_edges,  Unset):
            edges = UNSET
        else:
            edges = EntItemFieldEdges.from_dict(_edges)




        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        number_value = d.pop("number_value", UNSET)

        text_value = d.pop("text_value", UNSET)

        time_value = d.pop("time_value", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, ItemfieldType]
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = ItemfieldType(_type_)




        updated_at = d.pop("updated_at", UNSET)

        ent_item_field = cls(
            boolean_value=boolean_value,
            created_at=created_at,
            description=description,
            edges=edges,
            id=id,
            name=name,
            number_value=number_value,
            text_value=text_value,
            time_value=time_value,
            type_=type_,
            updated_at=updated_at,
        )


        ent_item_field.additional_properties = d
        return ent_item_field

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
