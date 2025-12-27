# EntGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | CreatedAt holds the value of the \&quot;created_at\&quot; field. | [optional] 
**currency** | **str** | Currency holds the value of the \&quot;currency\&quot; field. | [optional] 
**edges** | [**EntGroupEdges**](EntGroupEdges.md) | Edges holds the relations/edges for other nodes in the graph. The values are being populated by the GroupQuery when eager-loading is set. | [optional] 
**id** | **str** | ID of the ent. | [optional] 
**name** | **str** | Name holds the value of the \&quot;name\&quot; field. | [optional] 
**updated_at** | **str** | UpdatedAt holds the value of the \&quot;updated_at\&quot; field. | [optional] 

## Example

```python
from homebox_client.models.ent_group import EntGroup

# Example JSON string
json = "{}"
# create an instance of EntGroup from a JSON string
ent_group_instance = EntGroup.from_json(json)
# print the JSON string representation of the object
print(ent_group_instance.to_json())

# convert the object into a dict
ent_group_dict = ent_group_instance.to_dict()
# create an instance of EntGroup from a dict
ent_group_from_dict = EntGroup.from_dict(ent_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


