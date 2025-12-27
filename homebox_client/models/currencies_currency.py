from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import Union






T = TypeVar("T", bound="CurrenciesCurrency")



@_attrs_define
class CurrenciesCurrency:
    """ 
        Attributes:
            code (Union[Unset, str]):
            decimals (Union[Unset, int]):
            local (Union[Unset, str]):
            name (Union[Unset, str]):
            symbol (Union[Unset, str]):
     """

    code: Union[Unset, str] = UNSET
    decimals: Union[Unset, int] = UNSET
    local: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    symbol: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        code = self.code

        decimals = self.decimals

        local = self.local

        name = self.name

        symbol = self.symbol


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if code is not UNSET:
            field_dict["code"] = code
        if decimals is not UNSET:
            field_dict["decimals"] = decimals
        if local is not UNSET:
            field_dict["local"] = local
        if name is not UNSET:
            field_dict["name"] = name
        if symbol is not UNSET:
            field_dict["symbol"] = symbol

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        decimals = d.pop("decimals", UNSET)

        local = d.pop("local", UNSET)

        name = d.pop("name", UNSET)

        symbol = d.pop("symbol", UNSET)

        currencies_currency = cls(
            code=code,
            decimals=decimals,
            local=local,
            name=name,
            symbol=symbol,
        )


        currencies_currency.additional_properties = d
        return currencies_currency

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
