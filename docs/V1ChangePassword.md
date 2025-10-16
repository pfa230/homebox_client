# V1ChangePassword


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | **str** |  | [optional] 
**new** | **str** |  | [optional] 

## Example

```python
from homebox_client.models.v1_change_password import V1ChangePassword

# TODO update the JSON string below
json = "{}"
# create an instance of V1ChangePassword from a JSON string
v1_change_password_instance = V1ChangePassword.from_json(json)
# print the JSON string representation of the object
print(V1ChangePassword.to_json())

# convert the object into a dict
v1_change_password_dict = v1_change_password_instance.to_dict()
# create an instance of V1ChangePassword from a dict
v1_change_password_from_dict = V1ChangePassword.from_dict(v1_change_password_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


