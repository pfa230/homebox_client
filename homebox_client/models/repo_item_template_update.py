from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union

if TYPE_CHECKING:
  from ..models.repo_template_field import RepoTemplateField





T = TypeVar("T", bound="RepoItemTemplateUpdate")



@_attrs_define
class RepoItemTemplateUpdate:
    """ 
        Attributes:
            name (str):
            default_description (Union[None, Unset, str]):
            default_insured (Union[Unset, bool]):
            default_label_ids (Union[None, Unset, list[str]]):
            default_lifetime_warranty (Union[Unset, bool]):
            default_location_id (Union[None, Unset, str]): Default location and labels
            default_manufacturer (Union[None, Unset, str]):
            default_model_number (Union[None, Unset, str]):
            default_name (Union[None, Unset, str]):
            default_quantity (Union[None, Unset, int]): Default values for items
            default_warranty_details (Union[None, Unset, str]):
            description (Union[Unset, str]):
            fields (Union[Unset, list['RepoTemplateField']]): Custom fields
            id (Union[Unset, str]):
            include_purchase_fields (Union[Unset, bool]):
            include_sold_fields (Union[Unset, bool]):
            include_warranty_fields (Union[Unset, bool]): Metadata flags
            notes (Union[Unset, str]):
     """

    name: str
    default_description: Union[None, Unset, str] = UNSET
    default_insured: Union[Unset, bool] = UNSET
    default_label_ids: Union[None, Unset, list[str]] = UNSET
    default_lifetime_warranty: Union[Unset, bool] = UNSET
    default_location_id: Union[None, Unset, str] = UNSET
    default_manufacturer: Union[None, Unset, str] = UNSET
    default_model_number: Union[None, Unset, str] = UNSET
    default_name: Union[None, Unset, str] = UNSET
    default_quantity: Union[None, Unset, int] = UNSET
    default_warranty_details: Union[None, Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    fields: Union[Unset, list['RepoTemplateField']] = UNSET
    id: Union[Unset, str] = UNSET
    include_purchase_fields: Union[Unset, bool] = UNSET
    include_sold_fields: Union[Unset, bool] = UNSET
    include_warranty_fields: Union[Unset, bool] = UNSET
    notes: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.repo_template_field import RepoTemplateField
        name = self.name

        default_description: Union[None, Unset, str]
        if isinstance(self.default_description, Unset):
            default_description = UNSET
        else:
            default_description = self.default_description

        default_insured = self.default_insured

        default_label_ids: Union[None, Unset, list[str]]
        if isinstance(self.default_label_ids, Unset):
            default_label_ids = UNSET
        elif isinstance(self.default_label_ids, list):
            default_label_ids = self.default_label_ids


        else:
            default_label_ids = self.default_label_ids

        default_lifetime_warranty = self.default_lifetime_warranty

        default_location_id: Union[None, Unset, str]
        if isinstance(self.default_location_id, Unset):
            default_location_id = UNSET
        else:
            default_location_id = self.default_location_id

        default_manufacturer: Union[None, Unset, str]
        if isinstance(self.default_manufacturer, Unset):
            default_manufacturer = UNSET
        else:
            default_manufacturer = self.default_manufacturer

        default_model_number: Union[None, Unset, str]
        if isinstance(self.default_model_number, Unset):
            default_model_number = UNSET
        else:
            default_model_number = self.default_model_number

        default_name: Union[None, Unset, str]
        if isinstance(self.default_name, Unset):
            default_name = UNSET
        else:
            default_name = self.default_name

        default_quantity: Union[None, Unset, int]
        if isinstance(self.default_quantity, Unset):
            default_quantity = UNSET
        else:
            default_quantity = self.default_quantity

        default_warranty_details: Union[None, Unset, str]
        if isinstance(self.default_warranty_details, Unset):
            default_warranty_details = UNSET
        else:
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

        notes = self.notes


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
        })
        if default_description is not UNSET:
            field_dict["defaultDescription"] = default_description
        if default_insured is not UNSET:
            field_dict["defaultInsured"] = default_insured
        if default_label_ids is not UNSET:
            field_dict["defaultLabelIds"] = default_label_ids
        if default_lifetime_warranty is not UNSET:
            field_dict["defaultLifetimeWarranty"] = default_lifetime_warranty
        if default_location_id is not UNSET:
            field_dict["defaultLocationId"] = default_location_id
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
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.repo_template_field import RepoTemplateField
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_default_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        default_description = _parse_default_description(d.pop("defaultDescription", UNSET))


        default_insured = d.pop("defaultInsured", UNSET)

        def _parse_default_label_ids(data: object) -> Union[None, Unset, list[str]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                default_label_ids_type_0 = cast(list[str], data)

                return default_label_ids_type_0
            except: # noqa: E722
                pass
            return cast(Union[None, Unset, list[str]], data)

        default_label_ids = _parse_default_label_ids(d.pop("defaultLabelIds", UNSET))


        default_lifetime_warranty = d.pop("defaultLifetimeWarranty", UNSET)

        def _parse_default_location_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        default_location_id = _parse_default_location_id(d.pop("defaultLocationId", UNSET))


        def _parse_default_manufacturer(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        default_manufacturer = _parse_default_manufacturer(d.pop("defaultManufacturer", UNSET))


        def _parse_default_model_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        default_model_number = _parse_default_model_number(d.pop("defaultModelNumber", UNSET))


        def _parse_default_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        default_name = _parse_default_name(d.pop("defaultName", UNSET))


        def _parse_default_quantity(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        default_quantity = _parse_default_quantity(d.pop("defaultQuantity", UNSET))


        def _parse_default_warranty_details(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        default_warranty_details = _parse_default_warranty_details(d.pop("defaultWarrantyDetails", UNSET))


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

        notes = d.pop("notes", UNSET)

        repo_item_template_update = cls(
            name=name,
            default_description=default_description,
            default_insured=default_insured,
            default_label_ids=default_label_ids,
            default_lifetime_warranty=default_lifetime_warranty,
            default_location_id=default_location_id,
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
            notes=notes,
        )


        repo_item_template_update.additional_properties = d
        return repo_item_template_update

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
