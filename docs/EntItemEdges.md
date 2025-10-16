# EntItemEdges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**List[EntAttachment]**](EntAttachment.md) | Attachments holds the value of the attachments edge. | [optional] 
**children** | [**List[EntItem]**](EntItem.md) | Children holds the value of the children edge. | [optional] 
**fields** | [**List[EntItemField]**](EntItemField.md) | Fields holds the value of the fields edge. | [optional] 
**group** | [**EntGroup**](EntGroup.md) | Group holds the value of the group edge. | [optional] 
**label** | [**List[EntLabel]**](EntLabel.md) | Label holds the value of the label edge. | [optional] 
**location** | [**EntLocation**](EntLocation.md) | Location holds the value of the location edge. | [optional] 
**maintenance_entries** | [**List[EntMaintenanceEntry]**](EntMaintenanceEntry.md) | MaintenanceEntries holds the value of the maintenance_entries edge. | [optional] 
**parent** | [**EntItem**](EntItem.md) | Parent holds the value of the parent edge. | [optional] 

## Example

```python
from homebox_client.models.ent_item_edges import EntItemEdges

# TODO update the JSON string below
json = "{}"
# create an instance of EntItemEdges from a JSON string
ent_item_edges_instance = EntItemEdges.from_json(json)
# print the JSON string representation of the object
print(EntItemEdges.to_json())

# convert the object into a dict
ent_item_edges_dict = ent_item_edges_instance.to_dict()
# create an instance of EntItemEdges from a dict
ent_item_edges_from_dict = EntItemEdges.from_dict(ent_item_edges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


