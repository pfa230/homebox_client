# RepoMaintenanceEntryUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed_date** | **str** |  | [optional] 
**cost** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**scheduled_date** | **str** |  | [optional] 

## Example

```python
from homebox_client.models.repo_maintenance_entry_update import RepoMaintenanceEntryUpdate

# Example JSON string
json = "{}"
# create an instance of RepoMaintenanceEntryUpdate from a JSON string
repo_maintenance_entry_update_instance = RepoMaintenanceEntryUpdate.from_json(json)
# print the JSON string representation of the object
print(repo_maintenance_entry_update_instance.to_json())

# convert the object into a dict
repo_maintenance_entry_update_dict = repo_maintenance_entry_update_instance.to_dict()
# create an instance of RepoMaintenanceEntryUpdate from a dict
repo_maintenance_entry_update_from_dict = RepoMaintenanceEntryUpdate.from_dict(repo_maintenance_entry_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


