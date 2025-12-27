from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.user_role import UserRole
from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.ent_user_edges import EntUserEdges





T = TypeVar("T", bound="EntUser")



@_attrs_define
class EntUser:
    """ 
        Attributes:
            activated_on (Union[Unset, str]): ActivatedOn holds the value of the "activated_on" field.
            created_at (Union[Unset, str]): CreatedAt holds the value of the "created_at" field.
            edges (Union[Unset, EntUserEdges]):
            email (Union[Unset, str]): Email holds the value of the "email" field.
            id (Union[Unset, str]): ID of the ent.
            is_superuser (Union[Unset, bool]): IsSuperuser holds the value of the "is_superuser" field.
            name (Union[Unset, str]): Name holds the value of the "name" field.
            oidc_issuer (Union[Unset, str]): OidcIssuer holds the value of the "oidc_issuer" field.
            oidc_subject (Union[Unset, str]): OidcSubject holds the value of the "oidc_subject" field.
            role (Union[Unset, UserRole]):
            superuser (Union[Unset, bool]): Superuser holds the value of the "superuser" field.
            updated_at (Union[Unset, str]): UpdatedAt holds the value of the "updated_at" field.
     """

    activated_on: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    edges: Union[Unset, 'EntUserEdges'] = UNSET
    email: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    is_superuser: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    oidc_issuer: Union[Unset, str] = UNSET
    oidc_subject: Union[Unset, str] = UNSET
    role: Union[Unset, UserRole] = UNSET
    superuser: Union[Unset, bool] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ent_user_edges import EntUserEdges
        activated_on = self.activated_on

        created_at = self.created_at

        edges: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.edges, Unset):
            edges = self.edges.to_dict()

        email = self.email

        id = self.id

        is_superuser = self.is_superuser

        name = self.name

        oidc_issuer = self.oidc_issuer

        oidc_subject = self.oidc_subject

        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value


        superuser = self.superuser

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if activated_on is not UNSET:
            field_dict["activated_on"] = activated_on
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if edges is not UNSET:
            field_dict["edges"] = edges
        if email is not UNSET:
            field_dict["email"] = email
        if id is not UNSET:
            field_dict["id"] = id
        if is_superuser is not UNSET:
            field_dict["is_superuser"] = is_superuser
        if name is not UNSET:
            field_dict["name"] = name
        if oidc_issuer is not UNSET:
            field_dict["oidc_issuer"] = oidc_issuer
        if oidc_subject is not UNSET:
            field_dict["oidc_subject"] = oidc_subject
        if role is not UNSET:
            field_dict["role"] = role
        if superuser is not UNSET:
            field_dict["superuser"] = superuser
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ent_user_edges import EntUserEdges
        d = dict(src_dict)
        activated_on = d.pop("activated_on", UNSET)

        created_at = d.pop("created_at", UNSET)

        _edges = d.pop("edges", UNSET)
        edges: Union[Unset, EntUserEdges]
        if isinstance(_edges,  Unset):
            edges = UNSET
        else:
            edges = EntUserEdges.from_dict(_edges)




        email = d.pop("email", UNSET)

        id = d.pop("id", UNSET)

        is_superuser = d.pop("is_superuser", UNSET)

        name = d.pop("name", UNSET)

        oidc_issuer = d.pop("oidc_issuer", UNSET)

        oidc_subject = d.pop("oidc_subject", UNSET)

        _role = d.pop("role", UNSET)
        role: Union[Unset, UserRole]
        if isinstance(_role,  Unset):
            role = UNSET
        else:
            role = UserRole(_role)




        superuser = d.pop("superuser", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        ent_user = cls(
            activated_on=activated_on,
            created_at=created_at,
            edges=edges,
            email=email,
            id=id,
            is_superuser=is_superuser,
            name=name,
            oidc_issuer=oidc_issuer,
            oidc_subject=oidc_subject,
            role=role,
            superuser=superuser,
            updated_at=updated_at,
        )


        ent_user.additional_properties = d
        return ent_user

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
