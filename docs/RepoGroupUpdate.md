# RepoGroupUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from homebox_client.models.repo_group_update import RepoGroupUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of RepoGroupUpdate from a JSON string
repo_group_update_instance = RepoGroupUpdate.from_json(json)
# print the JSON string representation of the object
print(RepoGroupUpdate.to_json())

# convert the object into a dict
repo_group_update_dict = repo_group_update_instance.to_dict()
# create an instance of RepoGroupUpdate from a dict
repo_group_update_from_dict = RepoGroupUpdate.from_dict(repo_group_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


