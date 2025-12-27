# RepoGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from homebox_client.models.repo_group import RepoGroup

# Example JSON string
json = "{}"
# create an instance of RepoGroup from a JSON string
repo_group_instance = RepoGroup.from_json(json)
# print the JSON string representation of the object
print(repo_group_instance.to_json())

# convert the object into a dict
repo_group_dict = repo_group_instance.to_dict()
# create an instance of RepoGroup from a dict
repo_group_from_dict = RepoGroup.from_dict(repo_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


