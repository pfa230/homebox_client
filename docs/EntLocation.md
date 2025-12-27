# EntLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | CreatedAt holds the value of the \&quot;created_at\&quot; field. | [optional] 
**description** | **str** | Description holds the value of the \&quot;description\&quot; field. | [optional] 
**edges** | [**EntLocationEdges**](EntLocationEdges.md) | Edges holds the relations/edges for other nodes in the graph. The values are being populated by the LocationQuery when eager-loading is set. | [optional] 
**id** | **str** | ID of the ent. | [optional] 
**name** | **str** | Name holds the value of the \&quot;name\&quot; field. | [optional] 
**updated_at** | **str** | UpdatedAt holds the value of the \&quot;updated_at\&quot; field. | [optional] 

## Example

```python
from homebox_client.models.ent_location import EntLocation

# Example JSON string
json = "{}"
# create an instance of EntLocation from a JSON string
ent_location_instance = EntLocation.from_json(json)
# print the JSON string representation of the object
print(ent_location_instance.to_json())

# convert the object into a dict
ent_location_dict = ent_location_instance.to_dict()
# create an instance of EntLocation from a dict
ent_location_from_dict = EntLocation.from_dict(ent_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


