# RepoItemAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**mime_type** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**primary** | **bool** |  | [optional] 
**thumbnail** | [**EntAttachment**](EntAttachment.md) |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from homebox_client.models.repo_item_attachment import RepoItemAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of RepoItemAttachment from a JSON string
repo_item_attachment_instance = RepoItemAttachment.from_json(json)
# print the JSON string representation of the object
print(RepoItemAttachment.to_json())

# convert the object into a dict
repo_item_attachment_dict = repo_item_attachment_instance.to_dict()
# create an instance of RepoItemAttachment from a dict
repo_item_attachment_from_dict = RepoItemAttachment.from_dict(repo_item_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


