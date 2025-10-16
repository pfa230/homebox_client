# EntAuthRolesEdges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | [**EntAuthTokens**](EntAuthTokens.md) | Token holds the value of the token edge. | [optional] 

## Example

```python
from homebox_client.models.ent_auth_roles_edges import EntAuthRolesEdges

# TODO update the JSON string below
json = "{}"
# create an instance of EntAuthRolesEdges from a JSON string
ent_auth_roles_edges_instance = EntAuthRolesEdges.from_json(json)
# print the JSON string representation of the object
print(EntAuthRolesEdges.to_json())

# convert the object into a dict
ent_auth_roles_edges_dict = ent_auth_roles_edges_instance.to_dict()
# create an instance of EntAuthRolesEdges from a dict
ent_auth_roles_edges_from_dict = EntAuthRolesEdges.from_dict(ent_auth_roles_edges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


