# V1GroupInvitationCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **str** |  | [optional] 
**uses** | **int** |  | 

## Example

```python
from homebox_client.models.v1_group_invitation_create import V1GroupInvitationCreate

# Example JSON string
json = "{}"
# create an instance of V1GroupInvitationCreate from a JSON string
v1_group_invitation_create_instance = V1GroupInvitationCreate.from_json(json)
# print the JSON string representation of the object
print(v1_group_invitation_create_instance.to_json())

# convert the object into a dict
v1_group_invitation_create_dict = v1_group_invitation_create_instance.to_dict()
# create an instance of V1GroupInvitationCreate from a dict
v1_group_invitation_create_from_dict = V1GroupInvitationCreate.from_dict(v1_group_invitation_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


