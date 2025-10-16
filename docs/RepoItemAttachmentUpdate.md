# RepoItemAttachmentUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary** | **bool** |  | [optional] 
**title** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from homebox_client.models.repo_item_attachment_update import RepoItemAttachmentUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of RepoItemAttachmentUpdate from a JSON string
repo_item_attachment_update_instance = RepoItemAttachmentUpdate.from_json(json)
# print the JSON string representation of the object
print(RepoItemAttachmentUpdate.to_json())

# convert the object into a dict
repo_item_attachment_update_dict = repo_item_attachment_update_instance.to_dict()
# create an instance of RepoItemAttachmentUpdate from a dict
repo_item_attachment_update_from_dict = RepoItemAttachmentUpdate.from_dict(repo_item_attachment_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


