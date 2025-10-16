# V1GroupInvitation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **str** |  | [optional] 
**token** | **str** |  | [optional] 
**uses** | **int** |  | [optional] 

## Example

```python
from homebox_client.models.v1_group_invitation import V1GroupInvitation

# TODO update the JSON string below
json = "{}"
# create an instance of V1GroupInvitation from a JSON string
v1_group_invitation_instance = V1GroupInvitation.from_json(json)
# print the JSON string representation of the object
print(V1GroupInvitation.to_json())

# convert the object into a dict
v1_group_invitation_dict = v1_group_invitation_instance.to_dict()
# create an instance of V1GroupInvitation from a dict
v1_group_invitation_from_dict = V1GroupInvitation.from_dict(v1_group_invitation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


