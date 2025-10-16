# RepoLabelCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from homebox_client.models.repo_label_create import RepoLabelCreate

# TODO update the JSON string below
json = "{}"
# create an instance of RepoLabelCreate from a JSON string
repo_label_create_instance = RepoLabelCreate.from_json(json)
# print the JSON string representation of the object
print(RepoLabelCreate.to_json())

# convert the object into a dict
repo_label_create_dict = repo_label_create_instance.to_dict()
# create an instance of RepoLabelCreate from a dict
repo_label_create_from_dict = RepoLabelCreate.from_dict(repo_label_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


