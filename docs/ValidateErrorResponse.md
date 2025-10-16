# ValidateErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | [optional] 
**fields** | **str** |  | [optional] 

## Example

```python
from homebox_client.models.validate_error_response import ValidateErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ValidateErrorResponse from a JSON string
validate_error_response_instance = ValidateErrorResponse.from_json(json)
# print the JSON string representation of the object
print(ValidateErrorResponse.to_json())

# convert the object into a dict
validate_error_response_dict = validate_error_response_instance.to_dict()
# create an instance of ValidateErrorResponse from a dict
validate_error_response_from_dict = ValidateErrorResponse.from_dict(validate_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


