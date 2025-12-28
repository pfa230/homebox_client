from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.repo_template_label_summary import RepoTemplateLabelSummary
  from ..models.repo_template_location_summary import RepoTemplateLocationSummary
  from ..models.repo_template_field import RepoTemplateField





T = TypeVar("T", bound="RepoItemTemplateOut")



@_attrs_define
class RepoItemTemplateOut:
    """ 
        Attributes:
            created_at (Union[Unset, str]):
            default_description (Union[Unset, str]):
            default_insured (Union[Unset, bool]):
            default_labels (Union[Unset, list['RepoTemplateLabelSummary']]):
            default_lifetime_warranty (Union[Unset, bool]):
            default_location (Union[Unset, RepoTemplateLocationSummary]):
            default_manufacturer (Union[Unset, str]):
            default_model_number (Union[Unset, str]):
            default_name (Union[Unset, str]):
            default_quantity (Union[Unset, int]): Default values for items
            default_warranty_details (Union[Unset, str]):
            description (Union[Unset, str]):
            fields (Union[Unset, list['RepoTemplateField']]): Custom fields
            id (Union[Unset, str]):
            include_purchase_fields (Union[Unset, bool]):
            include_sold_fields (Union[Unset, bool]):
            include_warranty_fields (Union[Unset, bool]): Metadata flags
            name (Union[Unset, str]):
            notes (Union[Unset, str]):
            updated_at (Union[Unset, str]):
     """

    created_at: Union[Unset, str] = UNSET
    default_description: Union[Unset, str] = UNSET
    default_insured: Union[Unset, bool] = UNSET
    default_labels: Union[Unset, list['RepoTemplateLabelSummary']] = UNSET
    default_lifetime_warranty: Union[Unset, bool] = UNSET
    default_location: Union[Unset, 'RepoTemplateLocationSummary'] = UNSET
    default_manufacturer: Union[Unset, str] = UNSET
    default_model_number: Union[Unset, str] = UNSET
    default_name: Union[Unset, str] = UNSET
    default_quantity: Union[Unset, int] = UNSET
    default_warranty_details: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    fields: Union[Unset, list['RepoTemplateField']] = UNSET
    id: Union[Unset, str] = UNSET
    include_purchase_fields: Union[Unset, bool] = UNSET
    include_sold_fields: Union[Unset, bool] = UNSET
    include_warranty_fields: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.repo_template_label_summary import RepoTemplateLabelSummary
        from ..models.repo_template_location_summary import RepoTemplateLocationSummary
        from ..models.repo_template_field import RepoTemplateField
        created_at = self.created_at

        default_description = self.default_description

        default_insured = self.default_insured

        default_labels: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.default_labels, Unset):
            default_labels = []
            for default_labels_item_data in self.default_labels:
                default_labels_item = default_labels_item_data.to_dict()
                default_labels.append(default_labels_item)



        default_lifetime_warranty = self.default_lifetime_warranty

        default_location: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.default_location, Unset):
            default_location = self.default_location.to_dict()

        default_manufacturer = self.default_manufacturer

        default_model_number = self.default_model_number

        default_name = self.default_name

        default_quantity = self.default_quantity

        default_warranty_details = self.default_warranty_details

        description = self.description

        fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)



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
            field_dict["createdAt"] = created_at
        if default_description is not UNSET:
            field_dict["defaultDescription"] = default_description
        if default_insured is not UNSET:
            field_dict["defaultInsured"] = default_insured
        if default_labels is not UNSET:
            field_dict["defaultLabels"] = default_labels
        if default_lifetime_warranty is not UNSET:
            field_dict["defaultLifetimeWarranty"] = default_lifetime_warranty
        if default_location is not UNSET:
            field_dict["defaultLocation"] = default_location
        if default_manufacturer is not UNSET:
            field_dict["defaultManufacturer"] = default_manufacturer
        if default_model_number is not UNSET:
            field_dict["defaultModelNumber"] = default_model_number
        if default_name is not UNSET:
            field_dict["defaultName"] = default_name
        if default_quantity is not UNSET:
            field_dict["defaultQuantity"] = default_quantity
        if default_warranty_details is not UNSET:
            field_dict["defaultWarrantyDetails"] = default_warranty_details
        if description is not UNSET:
            field_dict["description"] = description
        if fields is not UNSET:
            field_dict["fields"] = fields
        if id is not UNSET:
            field_dict["id"] = id
        if include_purchase_fields is not UNSET:
            field_dict["includePurchaseFields"] = include_purchase_fields
        if include_sold_fields is not UNSET:
            field_dict["includeSoldFields"] = include_sold_fields
        if include_warranty_fields is not UNSET:
            field_dict["includeWarrantyFields"] = include_warranty_fields
        if name is not UNSET:
            field_dict["name"] = name
        if notes is not UNSET:
            field_dict["notes"] = notes
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.repo_template_label_summary import RepoTemplateLabelSummary
        from ..models.repo_template_location_summary import RepoTemplateLocationSummary
        from ..models.repo_template_field import RepoTemplateField
        d = dict(src_dict)
        created_at = d.pop("createdAt", UNSET)

        default_description = d.pop("defaultDescription", UNSET)

        default_insured = d.pop("defaultInsured", UNSET)

        default_labels = []
        _default_labels = d.pop("defaultLabels", UNSET)
        for default_labels_item_data in (_default_labels or []):
            default_labels_item = RepoTemplateLabelSummary.from_dict(default_labels_item_data)



            default_labels.append(default_labels_item)


        default_lifetime_warranty = d.pop("defaultLifetimeWarranty", UNSET)

        _default_location = d.pop("defaultLocation", UNSET)
        default_location: Union[Unset, RepoTemplateLocationSummary]
        if isinstance(_default_location,  Unset):
            default_location = UNSET
        else:
            default_location = RepoTemplateLocationSummary.from_dict(_default_location)




        default_manufacturer = d.pop("defaultManufacturer", UNSET)

        default_model_number = d.pop("defaultModelNumber", UNSET)

        default_name = d.pop("defaultName", UNSET)

        default_quantity = d.pop("defaultQuantity", UNSET)

        default_warranty_details = d.pop("defaultWarrantyDetails", UNSET)

        description = d.pop("description", UNSET)

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in (_fields or []):
            fields_item = RepoTemplateField.from_dict(fields_item_data)



            fields.append(fields_item)


        id = d.pop("id", UNSET)

        include_purchase_fields = d.pop("includePurchaseFields", UNSET)

        include_sold_fields = d.pop("includeSoldFields", UNSET)

        include_warranty_fields = d.pop("includeWarrantyFields", UNSET)

        name = d.pop("name", UNSET)

        notes = d.pop("notes", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        repo_item_template_out = cls(
            created_at=created_at,
            default_description=default_description,
            default_insured=default_insured,
            default_labels=default_labels,
            default_lifetime_warranty=default_lifetime_warranty,
            default_location=default_location,
            default_manufacturer=default_manufacturer,
            default_model_number=default_model_number,
            default_name=default_name,
            default_quantity=default_quantity,
            default_warranty_details=default_warranty_details,
            description=description,
            fields=fields,
            id=id,
            include_purchase_fields=include_purchase_fields,
            include_sold_fields=include_sold_fields,
            include_warranty_fields=include_warranty_fields,
            name=name,
            notes=notes,
            updated_at=updated_at,
        )


        repo_item_template_out.additional_properties = d
        return repo_item_template_out

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
