# EntItemFieldEdges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item** | [**EntItem**](EntItem.md) | Item holds the value of the item edge. | [optional] 

## Example

```python
from homebox_client.models.ent_item_field_edges import EntItemFieldEdges

# Example JSON string
json = "{}"
# create an instance of EntItemFieldEdges from a JSON string
ent_item_field_edges_instance = EntItemFieldEdges.from_json(json)
# print the JSON string representation of the object
print(ent_item_field_edges_instance.to_json())

# convert the object into a dict
ent_item_field_edges_dict = ent_item_field_edges_instance.to_dict()
# create an instance of EntItemFieldEdges from a dict
ent_item_field_edges_from_dict = EntItemFieldEdges.from_dict(ent_item_field_edges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


