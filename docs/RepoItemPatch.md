# RepoItemPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 

## Example

```python
from homebox_client.models.repo_item_patch import RepoItemPatch

# TODO update the JSON string below
json = "{}"
# create an instance of RepoItemPatch from a JSON string
repo_item_patch_instance = RepoItemPatch.from_json(json)
# print the JSON string representation of the object
print(RepoItemPatch.to_json())

# convert the object into a dict
repo_item_patch_dict = repo_item_patch_instance.to_dict()
# create an instance of RepoItemPatch from a dict
repo_item_patch_from_dict = RepoItemPatch.from_dict(repo_item_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


