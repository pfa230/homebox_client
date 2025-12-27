# EntAuthTokensEdges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roles** | [**EntAuthRoles**](EntAuthRoles.md) | Roles holds the value of the roles edge. | [optional] 
**user** | [**EntUser**](EntUser.md) | User holds the value of the user edge. | [optional] 

## Example

```python
from homebox_client.models.ent_auth_tokens_edges import EntAuthTokensEdges

# Example JSON string
json = "{}"
# create an instance of EntAuthTokensEdges from a JSON string
ent_auth_tokens_edges_instance = EntAuthTokensEdges.from_json(json)
# print the JSON string representation of the object
print(ent_auth_tokens_edges_instance.to_json())

# convert the object into a dict
ent_auth_tokens_edges_dict = ent_auth_tokens_edges_instance.to_dict()
# create an instance of EntAuthTokensEdges from a dict
ent_auth_tokens_edges_from_dict = EntAuthTokensEdges.from_dict(ent_auth_tokens_edges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


