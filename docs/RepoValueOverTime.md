# RepoValueOverTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **str** |  | [optional] 
**entries** | [**List[RepoValueOverTimeEntry]**](RepoValueOverTimeEntry.md) |  | [optional] 
**start** | **str** |  | [optional] 
**value_at_end** | **float** |  | [optional] 
**value_at_start** | **float** |  | [optional] 

## Example

```python
from homebox_client.models.repo_value_over_time import RepoValueOverTime

# Example JSON string
json = "{}"
# create an instance of RepoValueOverTime from a JSON string
repo_value_over_time_instance = RepoValueOverTime.from_json(json)
# print the JSON string representation of the object
print(repo_value_over_time_instance.to_json())

# convert the object into a dict
repo_value_over_time_dict = repo_value_over_time_instance.to_dict()
# create an instance of RepoValueOverTime from a dict
repo_value_over_time_from_dict = RepoValueOverTime.from_dict(repo_value_over_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


