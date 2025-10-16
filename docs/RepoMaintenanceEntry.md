# RepoMaintenanceEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed_date** | **str** |  | [optional] 
**cost** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**scheduled_date** | **str** |  | [optional] 

## Example

```python
from homebox_client.models.repo_maintenance_entry import RepoMaintenanceEntry

# TODO update the JSON string below
json = "{}"
# create an instance of RepoMaintenanceEntry from a JSON string
repo_maintenance_entry_instance = RepoMaintenanceEntry.from_json(json)
# print the JSON string representation of the object
print(RepoMaintenanceEntry.to_json())

# convert the object into a dict
repo_maintenance_entry_dict = repo_maintenance_entry_instance.to_dict()
# create an instance of RepoMaintenanceEntry from a dict
repo_maintenance_entry_from_dict = RepoMaintenanceEntry.from_dict(repo_maintenance_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


