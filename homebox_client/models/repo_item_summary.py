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





T = TypeVar("T", bound="RepoItemSummary")



@_attrs_define
class RepoItemSummary:
    """ 
        Attributes:
            archived (Union[Unset, bool]):
            asset_id (Union[Unset, str]):  Example: 0.
            created_at (Union[Unset, str]):
            description (Union[Unset, str]):
            id (Union[Unset, str]):
            image_id (Union[None, Unset, str]):
            insured (Union[Unset, bool]):
            labels (Union[Unset, list['RepoLabelSummary']]):
            location (Union['RepoLocationSummary', None, Unset]): Edges
            name (Union[Unset, str]):
            purchase_price (Union[Unset, float]):
            quantity (Union[Unset, int]):
            sold_time (Union[Unset, str]): Sale details
            thumbnail_id (Union[None, Unset, str]):
            updated_at (Union[Unset, str]):
     """

    archived: Union[Unset, bool] = UNSET
    asset_id: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    image_id: Union[None, Unset, str] = UNSET
    insured: Union[Unset, bool] = UNSET
    labels: Union[Unset, list['RepoLabelSummary']] = UNSET
    location: Union['RepoLocationSummary', None, Unset] = UNSET
    name: Union[Unset, str] = UNSET
    purchase_price: Union[Unset, float] = UNSET
    quantity: Union[Unset, int] = UNSET
    sold_time: Union[Unset, str] = UNSET
    thumbnail_id: Union[None, Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.repo_location_summary import RepoLocationSummary
        from ..models.repo_label_summary import RepoLabelSummary
        archived = self.archived

        asset_id = self.asset_id

        created_at = self.created_at

        description = self.description

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



        location: Union[None, Unset, dict[str, Any]]
        if isinstance(self.location, Unset):
            location = UNSET
        elif isinstance(self.location, RepoLocationSummary):
            location = self.location.to_dict()
        else:
            location = self.location

        name = self.name

        purchase_price = self.purchase_price

        quantity = self.quantity

        sold_time = self.sold_time

        thumbnail_id: Union[None, Unset, str]
        if isinstance(self.thumbnail_id, Unset):
            thumbnail_id = UNSET
        else:
            thumbnail_id = self.thumbnail_id

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if archived is not UNSET:
            field_dict["archived"] = archived
        if asset_id is not UNSET:
            field_dict["assetId"] = asset_id
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if image_id is not UNSET:
            field_dict["imageId"] = image_id
        if insured is not UNSET:
            field_dict["insured"] = insured
        if labels is not UNSET:
            field_dict["labels"] = labels
        if location is not UNSET:
            field_dict["location"] = location
        if name is not UNSET:
            field_dict["name"] = name
        if purchase_price is not UNSET:
            field_dict["purchasePrice"] = purchase_price
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if sold_time is not UNSET:
            field_dict["soldTime"] = sold_time
        if thumbnail_id is not UNSET:
            field_dict["thumbnailId"] = thumbnail_id
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.repo_location_summary import RepoLocationSummary
        from ..models.repo_label_summary import RepoLabelSummary
        d = dict(src_dict)
        archived = d.pop("archived", UNSET)

        asset_id = d.pop("assetId", UNSET)

        created_at = d.pop("createdAt", UNSET)

        description = d.pop("description", UNSET)

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


        name = d.pop("name", UNSET)

        purchase_price = d.pop("purchasePrice", UNSET)

        quantity = d.pop("quantity", UNSET)

        sold_time = d.pop("soldTime", UNSET)

        def _parse_thumbnail_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        thumbnail_id = _parse_thumbnail_id(d.pop("thumbnailId", UNSET))


        updated_at = d.pop("updatedAt", UNSET)

        repo_item_summary = cls(
            archived=archived,
            asset_id=asset_id,
            created_at=created_at,
            description=description,
            id=id,
            image_id=image_id,
            insured=insured,
            labels=labels,
            location=location,
            name=name,
            purchase_price=purchase_price,
            quantity=quantity,
            sold_time=sold_time,
            thumbnail_id=thumbnail_id,
            updated_at=updated_at,
        )


        repo_item_summary.additional_properties = d
        return repo_item_summary

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
