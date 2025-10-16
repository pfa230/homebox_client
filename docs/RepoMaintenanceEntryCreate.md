# RepoMaintenanceEntryCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed_date** | **str** |  | [optional] 
**cost** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | 
**scheduled_date** | **str** |  | [optional] 

## Example

```python
from homebox_client.models.repo_maintenance_entry_create import RepoMaintenanceEntryCreate

# TODO update the JSON string below
json = "{}"
# create an instance of RepoMaintenanceEntryCreate from a JSON string
repo_maintenance_entry_create_instance = RepoMaintenanceEntryCreate.from_json(json)
# print the JSON string representation of the object
print(RepoMaintenanceEntryCreate.to_json())

# convert the object into a dict
repo_maintenance_entry_create_dict = repo_maintenance_entry_create_instance.to_dict()
# create an instance of RepoMaintenanceEntryCreate from a dict
repo_maintenance_entry_create_from_dict = RepoMaintenanceEntryCreate.from_dict(repo_maintenance_entry_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


