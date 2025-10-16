# ServicesUserRegistration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from homebox_client.models.services_user_registration import ServicesUserRegistration

# TODO update the JSON string below
json = "{}"
# create an instance of ServicesUserRegistration from a JSON string
services_user_registration_instance = ServicesUserRegistration.from_json(json)
# print the JSON string representation of the object
print(ServicesUserRegistration.to_json())

# convert the object into a dict
services_user_registration_dict = services_user_registration_instance.to_dict()
# create an instance of ServicesUserRegistration from a dict
services_user_registration_from_dict = ServicesUserRegistration.from_dict(services_user_registration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


