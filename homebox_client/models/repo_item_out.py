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
  from ..models.repo_location_summary import RepoLocationSummary
  from ..models.repo_label_summary import RepoLabelSummary
  from ..models.repo_item_attachment import RepoItemAttachment
  from ..models.repo_item_summary import RepoItemSummary
  from ..models.repo_item_field import RepoItemField





T = TypeVar("T", bound="RepoItemOut")



@_attrs_define
class RepoItemOut:
    """ 
        Attributes:
            archived (Union[Unset, bool]):
            asset_id (Union[Unset, str]):  Example: 0.
            attachments (Union[Unset, list['RepoItemAttachment']]):
            created_at (Union[Unset, str]):
            description (Union[Unset, str]):
            fields (Union[Unset, list['RepoItemField']]):
            id (Union[Unset, str]):
            image_id (Union[None, Unset, str]):
            insured (Union[Unset, bool]):
            labels (Union[Unset, list['RepoLabelSummary']]):
            lifetime_warranty (Union[Unset, bool]): Warranty
            location (Union['RepoLocationSummary', None, Unset]): Edges
            manufacturer (Union[Unset, str]):
            model_number (Union[Unset, str]):
            name (Union[Unset, str]):
            notes (Union[Unset, str]): Extras
            parent (Union['RepoItemSummary', None, Unset]):
            purchase_from (Union[Unset, str]):
            purchase_price (Union[Unset, float]):
            purchase_time (Union[Unset, str]): Purchase
            quantity (Union[Unset, int]):
            serial_number (Union[Unset, str]):
            sold_notes (Union[Unset, str]):
            sold_price (Union[Unset, float]):
            sold_time (Union[Unset, str]): Sold
            sold_to (Union[Unset, str]):
            sync_child_items_locations (Union[Unset, bool]):
            thumbnail_id (Union[None, Unset, str]):
            updated_at (Union[Unset, str]):
            warranty_details (Union[Unset, str]):
            warranty_expires (Union[Unset, str]):
     """

    archived: Union[Unset, bool] = UNSET
    asset_id: Union[Unset, str] = UNSET
    attachments: Union[Unset, list['RepoItemAttachment']] = UNSET
    created_at: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    fields: Union[Unset, list['RepoItemField']] = UNSET
    id: Union[Unset, str] = UNSET
    image_id: Union[None, Unset, str] = UNSET
    insured: Union[Unset, bool] = UNSET
    labels: Union[Unset, list['RepoLabelSummary']] = UNSET
    lifetime_warranty: Union[Unset, bool] = UNSET
    location: Union['RepoLocationSummary', None, Unset] = UNSET
    manufacturer: Union[Unset, str] = UNSET
    model_number: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    parent: Union['RepoItemSummary', None, Unset] = UNSET
    purchase_from: Union[Unset, str] = UNSET
    purchase_price: Union[Unset, float] = UNSET
    purchase_time: Union[Unset, str] = UNSET
    quantity: Union[Unset, int] = UNSET
    serial_number: Union[Unset, str] = UNSET
    sold_notes: Union[Unset, str] = UNSET
    sold_price: Union[Unset, float] = UNSET
    sold_time: Union[Unset, str] = UNSET
    sold_to: Union[Unset, str] = UNSET
    sync_child_items_locations: Union[Unset, bool] = UNSET
    thumbnail_id: Union[None, Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    warranty_details: Union[Unset, str] = UNSET
    warranty_expires: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.repo_location_summary import RepoLocationSummary
        from ..models.repo_label_summary import RepoLabelSummary
        from ..models.repo_item_attachment import RepoItemAttachment
        from ..models.repo_item_summary import RepoItemSummary
        from ..models.repo_item_field import RepoItemField
        archived = self.archived

        asset_id = self.asset_id

        attachments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)



        created_at = self.created_at

        description = self.description

        fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)



        id = self.id

        image_id: Union[None, Unset, str]
        if isinstance(self.image_id, Unset):
            image_id = UNSET
        else:
            image_id = self.image_id

        insured = self.insured

        labels: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)



        lifetime_warranty = self.lifetime_warranty

        location: Union[None, Unset, dict[str, Any]]
        if isinstance(self.location, Unset):
            location = UNSET
        elif isinstance(self.location, RepoLocationSummary):
            location = self.location.to_dict()
        else:
            location = self.location

        manufacturer = self.manufacturer

        model_number = self.model_number

        name = self.name

        notes = self.notes

        parent: Union[None, Unset, dict[str, Any]]
        if isinstance(self.parent, Unset):
            parent = UNSET
        elif isinstance(self.parent, RepoItemSummary):
            parent = self.parent.to_dict()
        else:
            parent = self.parent

        purchase_from = self.purchase_from

        purchase_price = self.purchase_price

        purchase_time = self.purchase_time

        quantity = self.quantity

        serial_number = self.serial_number

        sold_notes = self.sold_notes

        sold_price = self.sold_price

        sold_time = self.sold_time

        sold_to = self.sold_to

        sync_child_items_locations = self.sync_child_items_locations

        thumbnail_id: Union[None, Unset, str]
        if isinstance(self.thumbnail_id, Unset):
            thumbnail_id = UNSET
        else:
            thumbnail_id = self.thumbnail_id

        updated_at = self.updated_at

        warranty_details = self.warranty_details

        warranty_expires = self.warranty_expires


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if archived is not UNSET:
            field_dict["archived"] = archived
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if fields is not UNSET:
            field_dict["fields"] = fields
        if id is not UNSET:
            field_dict["id"] = id
        if image_id is not UNSET:
            field_dict["imageId"] = image_id
        if insured is not UNSET:
            field_dict["insured"] = insured
        if labels is not UNSET:
            field_dict["labels"] = labels
        if lifetime_warranty is not UNSET:
            field_dict["lifetimeWarranty"] = lifetime_warranty
        if location is not UNSET:
            field_dict["location"] = location
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if model_number is not UNSET:
            field_dict["modelNumber"] = model_number
        if name is not UNSET:
            field_dict["name"] = name
        if notes is not UNSET:
            field_dict["notes"] = notes
        if parent is not UNSET:
            field_dict["parent"] = parent
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
        if thumbnail_id is not UNSET:
            field_dict["thumbnailId"] = thumbnail_id
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if warranty_details is not UNSET:
            field_dict["warrantyDetails"] = warranty_details
        if warranty_expires is not UNSET:
            field_dict["warrantyExpires"] = warranty_expires

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.repo_location_summary import RepoLocationSummary
        from ..models.repo_label_summary import RepoLabelSummary
        from ..models.repo_item_attachment import RepoItemAttachment
        from ..models.repo_item_summary import RepoItemSummary
        from ..models.repo_item_field import RepoItemField
        d = dict(src_dict)
        archived = d.pop("archived", UNSET)

        asset_id = d.pop("assetId", UNSET)

        attachments = []
        _attachments = d.pop("attachments", UNSET)
        for attachments_item_data in (_attachments or []):
            attachments_item = RepoItemAttachment.from_dict(attachments_item_data)



            attachments.append(attachments_item)


        created_at = d.pop("createdAt", UNSET)

        description = d.pop("description", UNSET)

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in (_fields or []):
            fields_item = RepoItemField.from_dict(fields_item_data)



            fields.append(fields_item)


        id = d.pop("id", UNSET)

        def _parse_image_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        image_id = _parse_image_id(d.pop("imageId", UNSET))


        insured = d.pop("insured", UNSET)

        labels = []
        _labels = d.pop("labels", UNSET)
        for labels_item_data in (_labels or []):
            labels_item = RepoLabelSummary.from_dict(labels_item_data)



            labels.append(labels_item)


        lifetime_warranty = d.pop("lifetimeWarranty", UNSET)

        def _parse_location(data: object) -> Union['RepoLocationSummary', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                location_type_1 = RepoLocationSummary.from_dict(data)



                return location_type_1
            except: # noqa: E722
                pass
            return cast(Union['RepoLocationSummary', None, Unset], data)

        location = _parse_location(d.pop("location", UNSET))


        manufacturer = d.pop("manufacturer", UNSET)

        model_number = d.pop("modelNumber", UNSET)

        name = d.pop("name", UNSET)

        notes = d.pop("notes", UNSET)

        def _parse_parent(data: object) -> Union['RepoItemSummary', None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                parent_type_1 = RepoItemSummary.from_dict(data)



                return parent_type_1
            except: # noqa: E722
                pass
            return cast(Union['RepoItemSummary', None, Unset], data)

        parent = _parse_parent(d.pop("parent", UNSET))


        purchase_from = d.pop("purchaseFrom", UNSET)

        purchase_price = d.pop("purchasePrice", UNSET)

        purchase_time = d.pop("purchaseTime", UNSET)

        quantity = d.pop("quantity", UNSET)

        serial_number = d.pop("serialNumber", UNSET)

        sold_notes = d.pop("soldNotes", UNSET)

        sold_price = d.pop("soldPrice", UNSET)

        sold_time = d.pop("soldTime", UNSET)

        sold_to = d.pop("soldTo", UNSET)

        sync_child_items_locations = d.pop("syncChildItemsLocations", UNSET)

        def _parse_thumbnail_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        thumbnail_id = _parse_thumbnail_id(d.pop("thumbnailId", UNSET))


        updated_at = d.pop("updatedAt", UNSET)

        warranty_details = d.pop("warrantyDetails", UNSET)

        warranty_expires = d.pop("warrantyExpires", UNSET)

        repo_item_out = cls(
            archived=archived,
            asset_id=asset_id,
            attachments=attachments,
            created_at=created_at,
            description=description,
            fields=fields,
            id=id,
            image_id=image_id,
            insured=insured,
            labels=labels,
            lifetime_warranty=lifetime_warranty,
            location=location,
            manufacturer=manufacturer,
            model_number=model_number,
            name=name,
            notes=notes,
            parent=parent,
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
            thumbnail_id=thumbnail_id,
            updated_at=updated_at,
            warranty_details=warranty_details,
            warranty_expires=warranty_expires,
        )


        repo_item_out.additional_properties = d
        return repo_item_out

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
