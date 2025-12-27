# EntLocationEdges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**List[EntLocation]**](EntLocation.md) | Children holds the value of the children edge. | [optional] 
**group** | [**EntGroup**](EntGroup.md) | Group holds the value of the group edge. | [optional] 
**items** | [**List[EntItem]**](EntItem.md) | Items holds the value of the items edge. | [optional] 
**parent** | [**EntLocation**](EntLocation.md) | Parent holds the value of the parent edge. | [optional] 

## Example

```python
from homebox_client.models.ent_location_edges import EntLocationEdges

# Example JSON string
json = "{}"
# create an instance of EntLocationEdges from a JSON string
ent_location_edges_instance = EntLocationEdges.from_json(json)
# print the JSON string representation of the object
print(ent_location_edges_instance.to_json())

# convert the object into a dict
ent_location_edges_dict = ent_location_edges_instance.to_dict()
# create an instance of EntLocationEdges from a dict
ent_location_edges_from_dict = EntLocationEdges.from_dict(ent_location_edges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


