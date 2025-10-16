# RepoLabelOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from homebox_client.models.repo_label_out import RepoLabelOut

# TODO update the JSON string below
json = "{}"
# create an instance of RepoLabelOut from a JSON string
repo_label_out_instance = RepoLabelOut.from_json(json)
# print the JSON string representation of the object
print(RepoLabelOut.to_json())

# convert the object into a dict
repo_label_out_dict = repo_label_out_instance.to_dict()
# create an instance of RepoLabelOut from a dict
repo_label_out_from_dict = RepoLabelOut.from_dict(repo_label_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


