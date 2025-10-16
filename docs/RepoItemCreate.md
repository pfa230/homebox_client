# RepoItemCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**label_ids** | **List[str]** |  | [optional] 
**location_id** | **str** | Edges | [optional] 
**name** | **str** |  | 
**parent_id** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 

## Example

```python
from homebox_client.models.repo_item_create import RepoItemCreate

# TODO update the JSON string below
json = "{}"
# create an instance of RepoItemCreate from a JSON string
repo_item_create_instance = RepoItemCreate.from_json(json)
# print the JSON string representation of the object
print(RepoItemCreate.to_json())

# convert the object into a dict
repo_item_create_dict = repo_item_create_instance.to_dict()
# create an instance of RepoItemCreate from a dict
repo_item_create_from_dict = RepoItemCreate.from_dict(repo_item_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


