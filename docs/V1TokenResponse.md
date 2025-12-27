# V1TokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachment_token** | **str** |  | [optional] 
**expires_at** | **str** |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from homebox_client.models.v1_token_response import V1TokenResponse

# Example JSON string
json = "{}"
# create an instance of V1TokenResponse from a JSON string
v1_token_response_instance = V1TokenResponse.from_json(json)
# print the JSON string representation of the object
print(v1_token_response_instance.to_json())

# convert the object into a dict
v1_token_response_dict = v1_token_response_instance.to_dict()
# create an instance of V1TokenResponse from a dict
v1_token_response_from_dict = V1TokenResponse.from_dict(v1_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


