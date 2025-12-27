from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.repo_item_create import RepoItemCreate





T = TypeVar("T", bound="RepoBarcodeProduct")



@_attrs_define
class RepoBarcodeProduct:
    """ 
        Attributes:
            barcode (Union[Unset, str]):
            image_base_64 (Union[Unset, str]):
            image_url (Union[Unset, str]):
            item (Union[Unset, RepoItemCreate]):
            manufacturer (Union[Unset, str]):
            model_number (Union[Unset, str]): Identifications
            notes (Union[Unset, str]): Extras
            search_engine_name (Union[Unset, str]):
     """

    barcode: Union[Unset, str] = UNSET
    image_base_64: Union[Unset, str] = UNSET
    image_url: Union[Unset, str] = UNSET
    item: Union[Unset, 'RepoItemCreate'] = UNSET
    manufacturer: Union[Unset, str] = UNSET
    model_number: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    search_engine_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.repo_item_create import RepoItemCreate
        barcode = self.barcode

        image_base_64 = self.image_base_64

        image_url = self.image_url

        item: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.item, Unset):
            item = self.item.to_dict()

        manufacturer = self.manufacturer

        model_number = self.model_number

        notes = self.notes

        search_engine_name = self.search_engine_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if barcode is not UNSET:
            field_dict["barcode"] = barcode
        if image_base_64 is not UNSET:
            field_dict["imageBase64"] = image_base_64
        if image_url is not UNSET:
            field_dict["imageURL"] = image_url
        if item is not UNSET:
            field_dict["item"] = item
        if manufacturer is not UNSET:
            field_dict["manufacturer"] = manufacturer
        if model_number is not UNSET:
            field_dict["modelNumber"] = model_number
        if notes is not UNSET:
            field_dict["notes"] = notes
        if search_engine_name is not UNSET:
            field_dict["search_engine_name"] = search_engine_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.repo_item_create import RepoItemCreate
        d = dict(src_dict)
        barcode = d.pop("barcode", UNSET)

        image_base_64 = d.pop("imageBase64", UNSET)

        image_url = d.pop("imageURL", UNSET)

        _item = d.pop("item", UNSET)
        item: Union[Unset, RepoItemCreate]
        if isinstance(_item,  Unset):
            item = UNSET
        else:
            item = RepoItemCreate.from_dict(_item)




        manufacturer = d.pop("manufacturer", UNSET)

        model_number = d.pop("modelNumber", UNSET)

        notes = d.pop("notes", UNSET)

        search_engine_name = d.pop("search_engine_name", UNSET)

        repo_barcode_product = cls(
            barcode=barcode,
            image_base_64=image_base_64,
            image_url=image_url,
            item=item,
            manufacturer=manufacturer,
            model_number=model_number,
            notes=notes,
            search_engine_name=search_engine_name,
        )


        repo_barcode_product.additional_properties = d
        return repo_barcode_product

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
