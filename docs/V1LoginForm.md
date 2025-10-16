# V1LoginForm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | [optional] 
**stay_logged_in** | **bool** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from homebox_client.models.v1_login_form import V1LoginForm

# TODO update the JSON string below
json = "{}"
# create an instance of V1LoginForm from a JSON string
v1_login_form_instance = V1LoginForm.from_json(json)
# print the JSON string representation of the object
print(V1LoginForm.to_json())

# convert the object into a dict
v1_login_form_dict = v1_login_form_instance.to_dict()
# create an instance of V1LoginForm from a dict
v1_login_form_from_dict = V1LoginForm.from_dict(v1_login_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


