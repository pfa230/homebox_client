from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.v1_build import V1Build
  from ..models.v1oidc_status import V1OIDCStatus
  from ..models.services_latest import ServicesLatest





T = TypeVar("T", bound="V1APISummary")



@_attrs_define
class V1APISummary:
    """ 
        Attributes:
            allow_registration (Union[Unset, bool]):
            build (Union[Unset, V1Build]):
            demo (Union[Unset, bool]):
            health (Union[Unset, bool]):
            label_printing (Union[Unset, bool]):
            latest (Union[Unset, ServicesLatest]):
            message (Union[Unset, str]):
            oidc (Union[Unset, V1OIDCStatus]):
            title (Union[Unset, str]):
            versions (Union[Unset, list[str]]):
     """

    allow_registration: Union[Unset, bool] = UNSET
    build: Union[Unset, 'V1Build'] = UNSET
    demo: Union[Unset, bool] = UNSET
    health: Union[Unset, bool] = UNSET
    label_printing: Union[Unset, bool] = UNSET
    latest: Union[Unset, 'ServicesLatest'] = UNSET
    message: Union[Unset, str] = UNSET
    oidc: Union[Unset, 'V1OIDCStatus'] = UNSET
    title: Union[Unset, str] = UNSET
    versions: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.v1_build import V1Build
        from ..models.v1oidc_status import V1OIDCStatus
        from ..models.services_latest import ServicesLatest
        allow_registration = self.allow_registration

        build: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.build, Unset):
            build = self.build.to_dict()

        demo = self.demo

        health = self.health

        label_printing = self.label_printing

        latest: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.latest, Unset):
            latest = self.latest.to_dict()

        message = self.message

        oidc: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.oidc, Unset):
            oidc = self.oidc.to_dict()

        title = self.title

        versions: Union[Unset, list[str]] = UNSET
        if not isinstance(self.versions, Unset):
            versions = self.versions




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if allow_registration is not UNSET:
            field_dict["allowRegistration"] = allow_registration
        if build is not UNSET:
            field_dict["build"] = build
        if demo is not UNSET:
            field_dict["demo"] = demo
        if health is not UNSET:
            field_dict["health"] = health
        if label_printing is not UNSET:
            field_dict["labelPrinting"] = label_printing
        if latest is not UNSET:
            field_dict["latest"] = latest
        if message is not UNSET:
            field_dict["message"] = message
        if oidc is not UNSET:
            field_dict["oidc"] = oidc
        if title is not UNSET:
            field_dict["title"] = title
        if versions is not UNSET:
            field_dict["versions"] = versions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.v1_build import V1Build
        from ..models.v1oidc_status import V1OIDCStatus
        from ..models.services_latest import ServicesLatest
        d = dict(src_dict)
        allow_registration = d.pop("allowRegistration", UNSET)

        _build = d.pop("build", UNSET)
        build: Union[Unset, V1Build]
        if isinstance(_build,  Unset):
            build = UNSET
        else:
            build = V1Build.from_dict(_build)




        demo = d.pop("demo", UNSET)

        health = d.pop("health", UNSET)

        label_printing = d.pop("labelPrinting", UNSET)

        _latest = d.pop("latest", UNSET)
        latest: Union[Unset, ServicesLatest]
        if isinstance(_latest,  Unset):
            latest = UNSET
        else:
            latest = ServicesLatest.from_dict(_latest)




        message = d.pop("message", UNSET)

        _oidc = d.pop("oidc", UNSET)
        oidc: Union[Unset, V1OIDCStatus]
        if isinstance(_oidc,  Unset):
            oidc = UNSET
        else:
            oidc = V1OIDCStatus.from_dict(_oidc)




        title = d.pop("title", UNSET)

        versions = cast(list[str], d.pop("versions", UNSET))


        v1api_summary = cls(
            allow_registration=allow_registration,
            build=build,
            demo=demo,
            health=health,
            label_printing=label_printing,
            latest=latest,
            message=message,
            oidc=oidc,
            title=title,
            versions=versions,
        )


        v1api_summary.additional_properties = d
        return v1api_summary

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
