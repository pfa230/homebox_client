# EntMaintenanceEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost** | **float** | Cost holds the value of the \&quot;cost\&quot; field. | [optional] 
**created_at** | **str** | CreatedAt holds the value of the \&quot;created_at\&quot; field. | [optional] 
**var_date** | **str** | Date holds the value of the \&quot;date\&quot; field. | [optional] 
**description** | **str** | Description holds the value of the \&quot;description\&quot; field. | [optional] 
**edges** | [**EntMaintenanceEntryEdges**](EntMaintenanceEntryEdges.md) | Edges holds the relations/edges for other nodes in the graph. The values are being populated by the MaintenanceEntryQuery when eager-loading is set. | [optional] 
**id** | **str** | ID of the ent. | [optional] 
**item_id** | **str** | ItemID holds the value of the \&quot;item_id\&quot; field. | [optional] 
**name** | **str** | Name holds the value of the \&quot;name\&quot; field. | [optional] 
**scheduled_date** | **str** | ScheduledDate holds the value of the \&quot;scheduled_date\&quot; field. | [optional] 
**updated_at** | **str** | UpdatedAt holds the value of the \&quot;updated_at\&quot; field. | [optional] 

## Example

```python
from homebox_client.models.ent_maintenance_entry import EntMaintenanceEntry

# Example JSON string
json = "{}"
# create an instance of EntMaintenanceEntry from a JSON string
ent_maintenance_entry_instance = EntMaintenanceEntry.from_json(json)
# print the JSON string representation of the object
print(ent_maintenance_entry_instance.to_json())

# convert the object into a dict
ent_maintenance_entry_dict = ent_maintenance_entry_instance.to_dict()
# create an instance of EntMaintenanceEntry from a dict
ent_maintenance_entry_from_dict = EntMaintenanceEntry.from_dict(ent_maintenance_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


