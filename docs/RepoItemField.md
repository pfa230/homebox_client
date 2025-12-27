# RepoItemField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boolean_value** | **bool** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**number_value** | **int** |  | [optional] 
**text_value** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from homebox_client.models.repo_item_field import RepoItemField

# Example JSON string
json = "{}"
# create an instance of RepoItemField from a JSON string
repo_item_field_instance = RepoItemField.from_json(json)
# print the JSON string representation of the object
print(repo_item_field_instance.to_json())

# convert the object into a dict
repo_item_field_dict = repo_item_field_instance.to_dict()
# create an instance of RepoItemField from a dict
repo_item_field_from_dict = RepoItemField.from_dict(repo_item_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


