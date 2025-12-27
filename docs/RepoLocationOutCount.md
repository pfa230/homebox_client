# RepoLocationOutCount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**item_count** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from homebox_client.models.repo_location_out_count import RepoLocationOutCount

# Example JSON string
json = "{}"
# create an instance of RepoLocationOutCount from a JSON string
repo_location_out_count_instance = RepoLocationOutCount.from_json(json)
# print the JSON string representation of the object
print(repo_location_out_count_instance.to_json())

# convert the object into a dict
repo_location_out_count_dict = repo_location_out_count_instance.to_dict()
# create an instance of RepoLocationOutCount from a dict
repo_location_out_count_from_dict = RepoLocationOutCount.from_dict(repo_location_out_count_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


