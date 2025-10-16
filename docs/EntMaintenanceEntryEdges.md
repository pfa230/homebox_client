# EntMaintenanceEntryEdges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item** | [**EntItem**](EntItem.md) | Item holds the value of the item edge. | [optional] 

## Example

```python
from homebox_client.models.ent_maintenance_entry_edges import EntMaintenanceEntryEdges

# TODO update the JSON string below
json = "{}"
# create an instance of EntMaintenanceEntryEdges from a JSON string
ent_maintenance_entry_edges_instance = EntMaintenanceEntryEdges.from_json(json)
# print the JSON string representation of the object
print(EntMaintenanceEntryEdges.to_json())

# convert the object into a dict
ent_maintenance_entry_edges_dict = ent_maintenance_entry_edges_instance.to_dict()
# create an instance of EntMaintenanceEntryEdges from a dict
ent_maintenance_entry_edges_from_dict = EntMaintenanceEntryEdges.from_dict(ent_maintenance_entry_edges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


