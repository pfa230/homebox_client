from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.ent_item_edges import EntItemEdges





T = TypeVar("T", bound="EntItem")



@_attrs_define
class EntItem:
    """ 
        Attributes:
            archived (Union[Unset, bool]): Archived holds the value of the "archived" field.
            asset_id (Union[Unset, int]): AssetID holds the value of the "asset_id" field.
            created_at (Union[Unset, str]): CreatedAt holds the value of the "created_at" field.
            description (Union[Unset, str]): Description holds the value of the "description" field.
            edges (Union[Unset, EntItemEdges]):
            id (Union[Unset, str]): ID of the ent.
            import_ref (Union[Unset, str]): ImportRef holds the value of the "import_ref" field.
            insured (Union[Unset, bool]): Insured holds the value of the "insured" field.
            lifetime_warranty (Union[Unset, bool]): LifetimeWarranty holds the value of the "lifetime_warranty" field.
            manufacturer (Union[Unset, str]): Manufacturer holds the value of the "manufacturer" field.
            model_number (Union[Unset, str]): ModelNumber holds the value of the "model_number" field.
            name (Union[Unset, str]): Name holds the value of the "name" field.
            notes (Union[Unset, str]): Notes holds the value of the "notes" field.
            purchase_from (Union[Unset, str]): PurchaseFrom holds the value of the "purchase_from" field.
            purchase_price (Union[Unset, float]): PurchasePrice holds the value of the "purchase_price" field.
            purchase_time (Union[Unset, str]): PurchaseTime holds the value of the "purchase_time" field.
            quantity (Union[Unset, int]): Quantity holds the value of the "quantity" field.
            serial_number (Union[Unset, str]): SerialNumber holds the value of the "serial_number" field.
            sold_notes (Union[Unset, str]): SoldNotes holds the value of the "sold_notes" field.
            sold_price (Union[Unset, float]): SoldPrice holds the value of the "sold_price" field.
            sold_time (Union[Unset, str]): SoldTime holds the value of the "sold_time" field.
            sold_to (Union[Unset, str]): SoldTo holds the value of the "sold_to" field.
            sync_child_items_locations (Union[Unset, bool]): SyncChildItemsLocations holds the value of the
                "sync_child_items_locations" field.
            updated_at (Union[Unset, str]): UpdatedAt holds the value of the "updated_at" field.
            warranty_details (Union[Unset, str]): WarrantyDetails holds the value of the "warranty_details" field.
            warranty_expires (Union[Unset, str]): WarrantyExpires holds the value of the "warranty_expires" field.
     """

    archived: Union[Unset, bool] = UNSET
    asset_id: Union[Unset, int] = UNSET
    created_at: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    edges: Union[Unset, 'EntItemEdges'] = UNSET
    id: Union[Unset, str] = UNSET
    import_ref: Union[Unset, str] = UNSET
    insured: Union[Unset, bool] = UNSET
    lifetime_warranty: Union[Unset, bool] = UNSET
    manufacturer: Union[Unset, str] = UNSET
    model_number: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
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
    updated_at: Union[Unset, str] = UNSET
    warranty_details: Union[Unset, str] = UNSET
    warranty_expires: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ent_item_edges import EntItemEdges
        archived = self.archived

        asset_id = self.asset_id

        created_at = self.created_at

        description = self.description

        edges: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.edges, Unset):
            edges = self.edges.to_dict()

        id = self.id

        import_ref = self.import_ref

        insured = self.insured

        lifetime_warranty = self.lifetime_warranty

        manufacturer = self.manufacturer

        model_number = self.model_number

        name = self.name

        notes = self.notes

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
            field_dict["asset_id"] = asset_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if edges is not UNSET:
            field_dict["edges"] = edges
        if id is not UNSET:
            field_dict["id"] = id
        if import_ref is not UNSET:
            field_dict["import_ref"] = import_ref
        if insured is not UNSET:
            field_dict["insured"] = insured
        if lifetime_warranty is not UNSET:
            field_dict["lifetime_warranty"] = lifetime_warranty
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if model_number is not UNSET:
            field_dict["model_number"] = model_number
        if name is not UNSET:
            field_dict["name"] = name
        if notes is not UNSET:
            field_dict["notes"] = notes
        if purchase_from is not UNSET:
            field_dict["purchase_from"] = purchase_from
        if purchase_price is not UNSET:
            field_dict["purchase_price"] = purchase_price
        if purchase_time is not UNSET:
            field_dict["purchase_time"] = purchase_time
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if serial_number is not UNSET:
            field_dict["serial_number"] = serial_number
        if sold_notes is not UNSET:
            field_dict["sold_notes"] = sold_notes
        if sold_price is not UNSET:
            field_dict["sold_price"] = sold_price
        if sold_time is not UNSET:
            field_dict["sold_time"] = sold_time
        if sold_to is not UNSET:
            field_dict["sold_to"] = sold_to
        if sync_child_items_locations is not UNSET:
            field_dict["sync_child_items_locations"] = sync_child_items_locations
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if warranty_details is not UNSET:
            field_dict["warranty_details"] = warranty_details
        if warranty_expires is not UNSET:
            field_dict["warranty_expires"] = warranty_expires

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ent_item_edges import EntItemEdges
        d = dict(src_dict)
        archived = d.pop("archived", UNSET)

        asset_id = d.pop("asset_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        description = d.pop("description", UNSET)

        _edges = d.pop("edges", UNSET)
        edges: Union[Unset, EntItemEdges]
        if isinstance(_edges,  Unset):
            edges = UNSET
        else:
            edges = EntItemEdges.from_dict(_edges)




        id = d.pop("id", UNSET)

        import_ref = d.pop("import_ref", UNSET)

        insured = d.pop("insured", UNSET)

        lifetime_warranty = d.pop("lifetime_warranty", UNSET)

        manufacturer = d.pop("manufacturer", UNSET)

        model_number = d.pop("model_number", UNSET)

        name = d.pop("name", UNSET)

        notes = d.pop("notes", UNSET)

        purchase_from = d.pop("purchase_from", UNSET)

        purchase_price = d.pop("purchase_price", UNSET)

        purchase_time = d.pop("purchase_time", UNSET)

        quantity = d.pop("quantity", UNSET)

        serial_number = d.pop("serial_number", UNSET)

        sold_notes = d.pop("sold_notes", UNSET)

        sold_price = d.pop("sold_price", UNSET)

        sold_time = d.pop("sold_time", UNSET)

        sold_to = d.pop("sold_to", UNSET)

        sync_child_items_locations = d.pop("sync_child_items_locations", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        warranty_details = d.pop("warranty_details", UNSET)

        warranty_expires = d.pop("warranty_expires", UNSET)

        ent_item = cls(
            archived=archived,
            asset_id=asset_id,
            created_at=created_at,
            description=description,
            edges=edges,
            id=id,
            import_ref=import_ref,
            insured=insured,
            lifetime_warranty=lifetime_warranty,
            manufacturer=manufacturer,
            model_number=model_number,
            name=name,
            notes=notes,
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
            updated_at=updated_at,
            warranty_details=warranty_details,
            warranty_expires=warranty_expires,
        )


        ent_item.additional_properties = d
        return ent_item

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
