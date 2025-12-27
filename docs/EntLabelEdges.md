# EntLabelEdges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | [**EntGroup**](EntGroup.md) | Group holds the value of the group edge. | [optional] 
**items** | [**List[EntItem]**](EntItem.md) | Items holds the value of the items edge. | [optional] 

## Example

```python
from homebox_client.models.ent_label_edges import EntLabelEdges

# Example JSON string
json = "{}"
# create an instance of EntLabelEdges from a JSON string
ent_label_edges_instance = EntLabelEdges.from_json(json)
# print the JSON string representation of the object
print(ent_label_edges_instance.to_json())

# convert the object into a dict
ent_label_edges_dict = ent_label_edges_instance.to_dict()
# create an instance of EntLabelEdges from a dict
ent_label_edges_from_dict = EntLabelEdges.from_dict(ent_label_edges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


