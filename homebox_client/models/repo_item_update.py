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
  from ..models.repo_item_field import RepoItemField





T = TypeVar("T", bound="RepoItemUpdate")



@_attrs_define
class RepoItemUpdate:
    """ 
        Attributes:
            name (str):
            archived (Union[Unset, bool]):
            asset_id (Union[Unset, str]):
            description (Union[Unset, str]):
            fields (Union[Unset, list['RepoItemField']]):
            id (Union[Unset, str]):
            insured (Union[Unset, bool]):
            label_ids (Union[Unset, list[str]]):
            lifetime_warranty (Union[Unset, bool]): Warranty
            location_id (Union[Unset, str]): Edges
            manufacturer (Union[Unset, str]):
            model_number (Union[Unset, str]):
            notes (Union[Unset, str]): Extras
            parent_id (Union[None, Unset, str]):
            purchase_from (Union[Unset, str]):
            purchase_price (Union[None, Unset, float]):
            purchase_time (Union[Unset, str]): Purchase
            quantity (Union[Unset, int]):
            serial_number (Union[Unset, str]): Identifications
            sold_notes (Union[Unset, str]):
            sold_price (Union[None, Unset, float]):
            sold_time (Union[Unset, str]): Sold
            sold_to (Union[Unset, str]):
            sync_child_items_locations (Union[Unset, bool]):
            warranty_details (Union[Unset, str]):
            warranty_expires (Union[Unset, str]):
     """

    name: str
    archived: Union[Unset, bool] = UNSET
    asset_id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    fields: Union[Unset, list['RepoItemField']] = UNSET
    id: Union[Unset, str] = UNSET
    insured: Union[Unset, bool] = UNSET
    label_ids: Union[Unset, list[str]] = UNSET
    lifetime_warranty: Union[Unset, bool] = UNSET
    location_id: Union[Unset, str] = UNSET
    manufacturer: Union[Unset, str] = UNSET
    model_number: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    parent_id: Union[None, Unset, str] = UNSET
    purchase_from: Union[Unset, str] = UNSET
    purchase_price: Union[None, Unset, float] = UNSET
    purchase_time: Union[Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    serial_number: Union[Unset, str] = UNSET
    sold_notes: Union[Unset, str] = UNSET
    sold_price: Union[None, Unset, float] = UNSET
    sold_time: Union[Unset, str] = UNSET
    sold_to: Union[Unset, str] = UNSET
    sync_child_items_locations: Union[Unset, bool] = UNSET
    warranty_details: Union[Unset, str] = UNSET
    warranty_expires: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.repo_item_field import RepoItemField
        name = self.name

        archived = self.archived

        asset_id = self.asset_id

        description = self.description

        fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)



        id = self.id

        insured = self.insured

        label_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.label_ids, Unset):
            label_ids = self.label_ids



        lifetime_warranty = self.lifetime_warranty

        location_id = self.location_id

        manufacturer = self.manufacturer

        model_number = self.model_number

        notes = self.notes

        parent_id: Union[None, Unset, str]
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        purchase_from = self.purchase_from

        purchase_price: Union[None, Unset, float]
        if isinstance(self.purchase_price, Unset):
            purchase_price = UNSET
        else:
            purchase_price = self.purchase_price

        purchase_time = self.purchase_time

        quantity = self.quantity

        serial_number = self.serial_number

        sold_notes = self.sold_notes

        sold_price: Union[None, Unset, float]
        if isinstance(self.sold_price, Unset):
            sold_price = UNSET
        else:
            sold_price = self.sold_price

        sold_time = self.sold_time

        sold_to = self.sold_to

        sync_child_items_locations = self.sync_child_items_locations

        warranty_details = self.warranty_details

        warranty_expires = self.warranty_expires


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
        })
        if archived is not UNSET:
            field_dict["archived"] = archived
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if description is not UNSET:
            field_dict["description"] = description
        if fields is not UNSET:
            field_dict["fields"] = fields
        if id is not UNSET:
            field_dict["id"] = id
        if insured is not UNSET:
            field_dict["insured"] = insured
        if label_ids is not UNSET:
            field_dict["labelIds"] = label_ids
        if lifetime_warranty is not UNSET:
            field_dict["lifetimeWarranty"] = lifetime_warranty
        if location_id is not UNSET:
            field_dict["locationId"] = location_id
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if model_number is not UNSET:
            field_dict["modelNumber"] = model_number
        if notes is not UNSET:
            field_dict["notes"] = notes
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if purchase_from is not UNSET:
            field_dict["purchaseFrom"] = purchase_from
        if purchase_price is not UNSET:
            field_dict["purchasePrice"] = purchase_price
        if purchase_time is not UNSET:
            field_dict["purchaseTime"] = purchase_time
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if serial_number is not UNSET:
            field_dict["serialNumber"] = serial_number
        if sold_notes is not UNSET:
            field_dict["soldNotes"] = sold_notes
        if sold_price is not UNSET:
            field_dict["soldPrice"] = sold_price
        if sold_time is not UNSET:
            field_dict["soldTime"] = sold_time
        if sold_to is not UNSET:
            field_dict["soldTo"] = sold_to
        if sync_child_items_locations is not UNSET:
            field_dict["syncChildItemsLocations"] = sync_child_items_locations
        if warranty_details is not UNSET:
            field_dict["warrantyDetails"] = warranty_details
        if warranty_expires is not UNSET:
            field_dict["warrantyExpires"] = warranty_expires

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.repo_item_field import RepoItemField
        d = dict(src_dict)
        name = d.pop("name")

        archived = d.pop("archived", UNSET)

        asset_id = d.pop("assetId", UNSET)

        description = d.pop("description", UNSET)

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in (_fields or []):
            fields_item = RepoItemField.from_dict(fields_item_data)



            fields.append(fields_item)


        id = d.pop("id", UNSET)

        insured = d.pop("insured", UNSET)

        label_ids = cast(list[str], d.pop("labelIds", UNSET))


        lifetime_warranty = d.pop("lifetimeWarranty", UNSET)

        location_id = d.pop("locationId", UNSET)

        manufacturer = d.pop("manufacturer", UNSET)

        model_number = d.pop("modelNumber", UNSET)

        notes = d.pop("notes", UNSET)

        def _parse_parent_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))


        purchase_from = d.pop("purchaseFrom", UNSET)

        def _parse_purchase_price(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        purchase_price = _parse_purchase_price(d.pop("purchasePrice", UNSET))


        purchase_time = d.pop("purchaseTime", UNSET)

        quantity = d.pop("quantity", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        sold_notes = d.pop("soldNotes", UNSET)

        def _parse_sold_price(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        sold_price = _parse_sold_price(d.pop("soldPrice", UNSET))


        sold_time = d.pop("soldTime", UNSET)

        sold_to = d.pop("soldTo", UNSET)

        sync_child_items_locations = d.pop("syncChildItemsLocations", UNSET)

        warranty_details = d.pop("warrantyDetails", UNSET)

        warranty_expires = d.pop("warrantyExpires", UNSET)

        repo_item_update = cls(
            name=name,
            archived=archived,
            asset_id=asset_id,
            description=description,
            fields=fields,
            id=id,
            insured=insured,
            label_ids=label_ids,
            lifetime_warranty=lifetime_warranty,
            location_id=location_id,
            manufacturer=manufacturer,
            model_number=model_number,
            notes=notes,
            parent_id=parent_id,
            purchase_from=purchase_from,
            purchase_price=purchase_price,
            purchase_time=purchase_time,
            quantity=quantity,
            serial_number=serial_number,
            sold_notes=sold_notes,
            sold_price=sold_price,
            sold_time=sold_time,
            sold_to=sold_to,
            sync_child_items_locations=sync_child_items_locations,
            warranty_details=warranty_details,
            warranty_expires=warranty_expires,
        )


        repo_item_update.additional_properties = d
        return repo_item_update

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
