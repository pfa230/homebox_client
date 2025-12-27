# RepoTreeItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**List[RepoTreeItem]**](RepoTreeItem.md) |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from homebox_client.models.repo_tree_item import RepoTreeItem

# Example JSON string
json = "{}"
# create an instance of RepoTreeItem from a JSON string
repo_tree_item_instance = RepoTreeItem.from_json(json)
# print the JSON string representation of the object
print(repo_tree_item_instance.to_json())

# convert the object into a dict
repo_tree_item_dict = repo_tree_item_instance.to_dict()
# create an instance of RepoTreeItem from a dict
repo_tree_item_from_dict = RepoTreeItem.from_dict(repo_tree_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


