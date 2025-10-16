# EntUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activated_on** | **str** | ActivatedOn holds the value of the \&quot;activated_on\&quot; field. | [optional] 
**created_at** | **str** | CreatedAt holds the value of the \&quot;created_at\&quot; field. | [optional] 
**edges** | [**EntUserEdges**](EntUserEdges.md) | Edges holds the relations/edges for other nodes in the graph. The values are being populated by the UserQuery when eager-loading is set. | [optional] 
**email** | **str** | Email holds the value of the \&quot;email\&quot; field. | [optional] 
**id** | **str** | ID of the ent. | [optional] 
**is_superuser** | **bool** | IsSuperuser holds the value of the \&quot;is_superuser\&quot; field. | [optional] 
**name** | **str** | Name holds the value of the \&quot;name\&quot; field. | [optional] 
**role** | [**UserRole**](UserRole.md) | Role holds the value of the \&quot;role\&quot; field. | [optional] 
**superuser** | **bool** | Superuser holds the value of the \&quot;superuser\&quot; field. | [optional] 
**updated_at** | **str** | UpdatedAt holds the value of the \&quot;updated_at\&quot; field. | [optional] 

## Example

```python
from homebox_client.models.ent_user import EntUser

# TODO update the JSON string below
json = "{}"
# create an instance of EntUser from a JSON string
ent_user_instance = EntUser.from_json(json)
# print the JSON string representation of the object
print(EntUser.to_json())

# convert the object into a dict
ent_user_dict = ent_user_instance.to_dict()
# create an instance of EntUser from a dict
ent_user_from_dict = EntUser.from_dict(ent_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


