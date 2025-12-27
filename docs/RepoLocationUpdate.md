# RepoLocationUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 

## Example

```python
from homebox_client.models.repo_location_update import RepoLocationUpdate

# Example JSON string
json = "{}"
# create an instance of RepoLocationUpdate from a JSON string
repo_location_update_instance = RepoLocationUpdate.from_json(json)
# print the JSON string representation of the object
print(repo_location_update_instance.to_json())

# convert the object into a dict
repo_location_update_dict = repo_location_update_instance.to_dict()
# create an instance of RepoLocationUpdate from a dict
repo_location_update_from_dict = RepoLocationUpdate.from_dict(repo_location_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


