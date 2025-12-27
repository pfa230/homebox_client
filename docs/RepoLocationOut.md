# RepoLocationOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**children** | [**List[RepoLocationSummary]**](RepoLocationSummary.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**parent** | [**RepoLocationSummary**](RepoLocationSummary.md) |  | [optional] 
**total_price** | **float** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from homebox_client.models.repo_location_out import RepoLocationOut

# Example JSON string
json = "{}"
# create an instance of RepoLocationOut from a JSON string
repo_location_out_instance = RepoLocationOut.from_json(json)
# print the JSON string representation of the object
print(repo_location_out_instance.to_json())

# convert the object into a dict
repo_location_out_dict = repo_location_out_instance.to_dict()
# create an instance of RepoLocationOut from a dict
repo_location_out_from_dict = RepoLocationOut.from_dict(repo_location_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


