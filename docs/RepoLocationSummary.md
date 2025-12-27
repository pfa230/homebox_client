# RepoLocationSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from homebox_client.models.repo_location_summary import RepoLocationSummary

# Example JSON string
json = "{}"
# create an instance of RepoLocationSummary from a JSON string
repo_location_summary_instance = RepoLocationSummary.from_json(json)
# print the JSON string representation of the object
print(repo_location_summary_instance.to_json())

# convert the object into a dict
repo_location_summary_dict = repo_location_summary_instance.to_dict()
# create an instance of RepoLocationSummary from a dict
repo_location_summary_from_dict = RepoLocationSummary.from_dict(repo_location_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


