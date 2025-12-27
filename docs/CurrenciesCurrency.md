# CurrenciesCurrency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**local** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from homebox_client.models.currencies_currency import CurrenciesCurrency

# Example JSON string
json = "{}"
# create an instance of CurrenciesCurrency from a JSON string
currencies_currency_instance = CurrenciesCurrency.from_json(json)
# print the JSON string representation of the object
print(currencies_currency_instance.to_json())

# convert the object into a dict
currencies_currency_dict = currencies_currency_instance.to_dict()
# create an instance of CurrenciesCurrency from a dict
currencies_currency_from_dict = CurrenciesCurrency.from_dict(currencies_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


