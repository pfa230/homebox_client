from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.authroles_role import AuthrolesRole
from ..types import UNSET, Unset
from typing import cast
from typing import Union

if TYPE_CHECKING:
  from ..models.ent_auth_roles_edges import EntAuthRolesEdges





T = TypeVar("T", bound="EntAuthRoles")



@_attrs_define
class EntAuthRoles:
    """ 
        Attributes:
            edges (Union[Unset, EntAuthRolesEdges]):
            id (Union[Unset, int]): ID of the ent.
            role (Union[Unset, AuthrolesRole]):
     """

    edges: Union[Unset, 'EntAuthRolesEdges'] = UNSET
    id: Union[Unset, int] = UNSET
    role: Union[Unset, AuthrolesRole] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.ent_auth_roles_edges import EntAuthRolesEdges
        edges: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.edges, Unset):
            edges = self.edges.to_dict()

        id = self.id

        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if edges is not UNSET:
            field_dict["edges"] = edges
        if id is not UNSET:
            field_dict["id"] = id
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ent_auth_roles_edges import EntAuthRolesEdges
        d = dict(src_dict)
        _edges = d.pop("edges", UNSET)
        edges: Union[Unset, EntAuthRolesEdges]
        if isinstance(_edges,  Unset):
            edges = UNSET
        else:
            edges = EntAuthRolesEdges.from_dict(_edges)




        id = d.pop("id", UNSET)

        _role = d.pop("role", UNSET)
        role: Union[Unset, AuthrolesRole]
        if isinstance(_role,  Unset):
            role = UNSET
        else:
            role = AuthrolesRole(_role)




        ent_auth_roles = cls(
            edges=edges,
            id=id,
            role=role,
        )


        ent_auth_roles.additional_properties = d
        return ent_auth_roles

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
