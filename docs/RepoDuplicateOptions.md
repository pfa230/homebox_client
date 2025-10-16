# RepoDuplicateOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copy_attachments** | **bool** |  | [optional] 
**copy_custom_fields** | **bool** |  | [optional] 
**copy_maintenance** | **bool** |  | [optional] 
**copy_prefix** | **str** |  | [optional] 

## Example

```python
from homebox_client.models.repo_duplicate_options import RepoDuplicateOptions

# TODO update the JSON string below
json = "{}"
# create an instance of RepoDuplicateOptions from a JSON string
repo_duplicate_options_instance = RepoDuplicateOptions.from_json(json)
# print the JSON string representation of the object
print(RepoDuplicateOptions.to_json())

# convert the object into a dict
repo_duplicate_options_dict = repo_duplicate_options_instance.to_dict()
# create an instance of RepoDuplicateOptions from a dict
repo_duplicate_options_from_dict = RepoDuplicateOptions.from_dict(repo_duplicate_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


