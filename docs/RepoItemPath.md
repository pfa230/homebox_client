# RepoItemPath


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | [**RepoItemType**](RepoItemType.md) |  | [optional] 

## Example

```python
from homebox_client.models.repo_item_path import RepoItemPath

# Example JSON string
json = "{}"
# create an instance of RepoItemPath from a JSON string
repo_item_path_instance = RepoItemPath.from_json(json)
# print the JSON string representation of the object
print(repo_item_path_instance.to_json())

# convert the object into a dict
repo_item_path_dict = repo_item_path_instance.to_dict()
# create an instance of RepoItemPath from a dict
repo_item_path_from_dict = RepoItemPath.from_dict(repo_item_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


