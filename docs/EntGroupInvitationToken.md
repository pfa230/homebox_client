# EntGroupInvitationToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | CreatedAt holds the value of the \&quot;created_at\&quot; field. | [optional] 
**edges** | [**EntGroupInvitationTokenEdges**](EntGroupInvitationTokenEdges.md) | Edges holds the relations/edges for other nodes in the graph. The values are being populated by the GroupInvitationTokenQuery when eager-loading is set. | [optional] 
**expires_at** | **str** | ExpiresAt holds the value of the \&quot;expires_at\&quot; field. | [optional] 
**id** | **str** | ID of the ent. | [optional] 
**token** | **List[int]** | Token holds the value of the \&quot;token\&quot; field. | [optional] 
**updated_at** | **str** | UpdatedAt holds the value of the \&quot;updated_at\&quot; field. | [optional] 
**uses** | **int** | Uses holds the value of the \&quot;uses\&quot; field. | [optional] 

## Example

```python
from homebox_client.models.ent_group_invitation_token import EntGroupInvitationToken

# TODO update the JSON string below
json = "{}"
# create an instance of EntGroupInvitationToken from a JSON string
ent_group_invitation_token_instance = EntGroupInvitationToken.from_json(json)
# print the JSON string representation of the object
print(EntGroupInvitationToken.to_json())

# convert the object into a dict
ent_group_invitation_token_dict = ent_group_invitation_token_instance.to_dict()
# create an instance of EntGroupInvitationToken from a dict
ent_group_invitation_token_from_dict = EntGroupInvitationToken.from_dict(ent_group_invitation_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


