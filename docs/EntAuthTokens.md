# EntAuthTokens


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | CreatedAt holds the value of the \&quot;created_at\&quot; field. | [optional] 
**edges** | [**EntAuthTokensEdges**](EntAuthTokensEdges.md) | Edges holds the relations/edges for other nodes in the graph. The values are being populated by the AuthTokensQuery when eager-loading is set. | [optional] 
**expires_at** | **str** | ExpiresAt holds the value of the \&quot;expires_at\&quot; field. | [optional] 
**id** | **str** | ID of the ent. | [optional] 
**token** | **List[int]** | Token holds the value of the \&quot;token\&quot; field. | [optional] 
**updated_at** | **str** | UpdatedAt holds the value of the \&quot;updated_at\&quot; field. | [optional] 

## Example

```python
from homebox_client.models.ent_auth_tokens import EntAuthTokens

# Example JSON string
json = "{}"
# create an instance of EntAuthTokens from a JSON string
ent_auth_tokens_instance = EntAuthTokens.from_json(json)
# print the JSON string representation of the object
print(ent_auth_tokens_instance.to_json())

# convert the object into a dict
ent_auth_tokens_dict = ent_auth_tokens_instance.to_dict()
# create an instance of EntAuthTokens from a dict
ent_auth_tokens_from_dict = EntAuthTokens.from_dict(ent_auth_tokens_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


