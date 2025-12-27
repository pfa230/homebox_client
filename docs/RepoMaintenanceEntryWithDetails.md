# RepoMaintenanceEntryWithDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed_date** | **str** |  | [optional] 
**cost** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**item_id** | **str** |  | [optional] 
**item_name** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**scheduled_date** | **str** |  | [optional] 

## Example

```python
from homebox_client.models.repo_maintenance_entry_with_details import RepoMaintenanceEntryWithDetails

# Example JSON string
json = "{}"
# create an instance of RepoMaintenanceEntryWithDetails from a JSON string
repo_maintenance_entry_with_details_instance = RepoMaintenanceEntryWithDetails.from_json(json)
# print the JSON string representation of the object
print(repo_maintenance_entry_with_details_instance.to_json())

# convert the object into a dict
repo_maintenance_entry_with_details_dict = repo_maintenance_entry_with_details_instance.to_dict()
# create an instance of RepoMaintenanceEntryWithDetails from a dict
repo_maintenance_entry_with_details_from_dict = RepoMaintenanceEntryWithDetails.from_dict(repo_maintenance_entry_with_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


