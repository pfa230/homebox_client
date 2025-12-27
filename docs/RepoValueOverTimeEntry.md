# RepoValueOverTimeEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from homebox_client.models.repo_value_over_time_entry import RepoValueOverTimeEntry

# Example JSON string
json = "{}"
# create an instance of RepoValueOverTimeEntry from a JSON string
repo_value_over_time_entry_instance = RepoValueOverTimeEntry.from_json(json)
# print the JSON string representation of the object
print(repo_value_over_time_entry_instance.to_json())

# convert the object into a dict
repo_value_over_time_entry_dict = repo_value_over_time_entry_instance.to_dict()
# create an instance of RepoValueOverTimeEntry from a dict
repo_value_over_time_entry_from_dict = RepoValueOverTimeEntry.from_dict(repo_value_over_time_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


