# EntAuthRoles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edges** | [**EntAuthRolesEdges**](EntAuthRolesEdges.md) | Edges holds the relations/edges for other nodes in the graph. The values are being populated by the AuthRolesQuery when eager-loading is set. | [optional] 
**id** | **int** | ID of the ent. | [optional] 
**role** | [**AuthrolesRole**](AuthrolesRole.md) | Role holds the value of the \&quot;role\&quot; field. | [optional] 

## Example

```python
from homebox_client.models.ent_auth_roles import EntAuthRoles

# TODO update the JSON string below
json = "{}"
# create an instance of EntAuthRoles from a JSON string
ent_auth_roles_instance = EntAuthRoles.from_json(json)
# print the JSON string representation of the object
print(EntAuthRoles.to_json())

# convert the object into a dict
ent_auth_roles_dict = ent_auth_roles_instance.to_dict()
# create an instance of EntAuthRoles from a dict
ent_auth_roles_from_dict = EntAuthRoles.from_dict(ent_auth_roles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


