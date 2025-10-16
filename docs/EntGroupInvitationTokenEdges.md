# EntGroupInvitationTokenEdges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | [**EntGroup**](EntGroup.md) | Group holds the value of the group edge. | [optional] 

## Example

```python
from homebox_client.models.ent_group_invitation_token_edges import EntGroupInvitationTokenEdges

# TODO update the JSON string below
json = "{}"
# create an instance of EntGroupInvitationTokenEdges from a JSON string
ent_group_invitation_token_edges_instance = EntGroupInvitationTokenEdges.from_json(json)
# print the JSON string representation of the object
print(EntGroupInvitationTokenEdges.to_json())

# convert the object into a dict
ent_group_invitation_token_edges_dict = ent_group_invitation_token_edges_instance.to_dict()
# create an instance of EntGroupInvitationTokenEdges from a dict
ent_group_invitation_token_edges_from_dict = EntGroupInvitationTokenEdges.from_dict(ent_group_invitation_token_edges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


