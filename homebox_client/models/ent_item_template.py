from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.ent_item_template_edges import EntItemTemplateEdges





T = TypeVar("T", bound="EntItemTemplate")



@_attrs_define
class EntItemTemplate:
    """ 
        Attributes:
            created_at (Union[Unset, str]): CreatedAt holds the value of the "created_at" field.
            default_description (Union[Unset, str]): Default description for items created from this template
            default_insured (Union[Unset, bool]): DefaultInsured holds the value of the "default_insured" field.
            default_label_ids (Union[Unset, list[str]]): Default label IDs for items created from this template
            default_lifetime_warranty (Union[Unset, bool]): DefaultLifetimeWarranty holds the value of the
                "default_lifetime_warranty" field.
            default_manufacturer (Union[Unset, str]): DefaultManufacturer holds the value of the "default_manufacturer"
                field.
            default_model_number (Union[Unset, str]): Default model number for items created from this template
            default_name (Union[Unset, str]): Default name template for items (can use placeholders)
            default_quantity (Union[Unset, int]): DefaultQuantity holds the value of the "default_quantity" field.
            default_warranty_details (Union[Unset, str]): DefaultWarrantyDetails holds the value of the
                "default_warranty_details" field.
            description (Union[Unset, str]): Description holds the value of the "description" field.
            edges (Union[Unset, EntItemTemplateEdges]):
            id (Union[Unset, str]): ID of the ent.
            include_purchase_fields (Union[Unset, bool]): Whether to include purchase fields in items created from this
                template
            include_sold_fields (Union[Unset, bool]): Whether to include sold fields in items created from this template
            include_warranty_fields (Union[Unset, bool]): Whether to include warranty fields in items created from this
                template
            name (Union[Unset, str]): Name holds the value of the "name" field.
            notes (Union[Unset, str]): Notes holds the value of the "notes" field.
            updated_at (Union[Unset, str]): UpdatedAt holds the value of the "updated_at" field.
     """

    created_at: Union[Unset, str] = UNSET
    default_description: Union[Unset, str] = UNSET
    default_insured: Union[Unset, bool] = UNSET
    default_label_ids: Union[Unset, list[str]] = UNSET
    default_lifetime_warranty: Union[Unset, bool] = UNSET
    default_manufacturer: Union[Unset, str] = UNSET
    default_model_number: Union[Unset, str] = UNSET
    default_name: Union[Unset, str] = UNSET
    default_quantity: Union[Unset, int] = UNSET
    default_warranty_details: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    edges: Union[Unset, 'EntItemTemplateEdges'] = UNSET
    id: Union[Unset, str] = UNSET
    include_purchase_fields: Union[Unset, bool] = UNSET
    include_sold_fields: Union[Unset, bool] = UNSET
    include_warranty_fields: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ent_item_template_edges import EntItemTemplateEdges
        created_at = self.created_at

        default_description = self.default_description

        default_insured = self.default_insured

        default_label_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.default_label_ids, Unset):
            default_label_ids = self.default_label_ids



        default_lifetime_warranty = self.default_lifetime_warranty

        default_manufacturer = self.default_manufacturer

        default_model_number = self.default_model_number

        default_name = self.default_name

        default_quantity = self.default_quantity

        default_warranty_details = self.default_warranty_details

        description = self.description

        edges: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.edges, Unset):
            edges = self.edges.to_dict()

        id = self.id

        include_purchase_fields = self.include_purchase_fields

        include_sold_fields = self.include_sold_fields

        include_warranty_fields = self.include_warranty_fields

        name = self.name

        notes = self.notes

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if default_description is not UNSET:
            field_dict["default_description"] = default_description
        if default_insured is not UNSET:
            field_dict["default_insured"] = default_insured
        if default_label_ids is not UNSET:
            field_dict["default_label_ids"] = default_label_ids
        if default_lifetime_warranty is not UNSET:
            field_dict["default_lifetime_warranty"] = default_lifetime_warranty
        if default_manufacturer is not UNSET:
            field_dict["default_manufacturer"] = default_manufacturer
        if default_model_number is not UNSET:
            field_dict["default_model_number"] = default_model_number
        if default_name is not UNSET:
            field_dict["default_name"] = default_name
        if default_quantity is not UNSET:
            field_dict["default_quantity"] = default_quantity
        if default_warranty_details is not UNSET:
            field_dict["default_warranty_details"] = default_warranty_details
        if description is not UNSET:
            field_dict["description"] = description
        if edges is not UNSET:
            field_dict["edges"] = edges
        if id is not UNSET:
            field_dict["id"] = id
        if include_purchase_fields is not UNSET:
            field_dict["include_purchase_fields"] = include_purchase_fields
        if include_sold_fields is not UNSET:
            field_dict["include_sold_fields"] = include_sold_fields
        if include_warranty_fields is not UNSET:
            field_dict["include_warranty_fields"] = include_warranty_fields
        if name is not UNSET:
            field_dict["name"] = name
        if notes is not UNSET:
            field_dict["notes"] = notes
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ent_item_template_edges import EntItemTemplateEdges
        d = dict(src_dict)
        created_at = d.pop("created_at", UNSET)

        default_description = d.pop("default_description", UNSET)

        default_insured = d.pop("default_insured", UNSET)

        default_label_ids = cast(list[str], d.pop("default_label_ids", UNSET))


        default_lifetime_warranty = d.pop("default_lifetime_warranty", UNSET)

        default_manufacturer = d.pop("default_manufacturer", UNSET)

        default_model_number = d.pop("default_model_number", UNSET)

        default_name = d.pop("default_name", UNSET)

        default_quantity = d.pop("default_quantity", UNSET)

        default_warranty_details = d.pop("default_warranty_details", UNSET)

        description = d.pop("description", UNSET)

        _edges = d.pop("edges", UNSET)
        edges: Union[Unset, EntItemTemplateEdges]
        if isinstance(_edges,  Unset):
            edges = UNSET
        else:
            edges = EntItemTemplateEdges.from_dict(_edges)




        id = d.pop("id", UNSET)

        include_purchase_fields = d.pop("include_purchase_fields", UNSET)

        include_sold_fields = d.pop("include_sold_fields", UNSET)

        include_warranty_fields = d.pop("include_warranty_fields", UNSET)

        name = d.pop("name", UNSET)

        notes = d.pop("notes", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        ent_item_template = cls(
            created_at=created_at,
            default_description=default_description,
            default_insured=default_insured,
            default_label_ids=default_label_ids,
            default_lifetime_warranty=default_lifetime_warranty,
            default_manufacturer=default_manufacturer,
            default_model_number=default_model_number,
            default_name=default_name,
            default_quantity=default_quantity,
            default_warranty_details=default_warranty_details,
            description=description,
            edges=edges,
            id=id,
            include_purchase_fields=include_purchase_fields,
            include_sold_fields=include_sold_fields,
            include_warranty_fields=include_warranty_fields,
            name=name,
            notes=notes,
            updated_at=updated_at,
        )


        ent_item_template.additional_properties = d
        return ent_item_template

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
