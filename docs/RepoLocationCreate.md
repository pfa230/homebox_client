# RepoLocationCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 

## Example

```python
from homebox_client.models.repo_location_create import RepoLocationCreate

# TODO update the JSON string below
json = "{}"
# create an instance of RepoLocationCreate from a JSON string
repo_location_create_instance = RepoLocationCreate.from_json(json)
# print the JSON string representation of the object
print(RepoLocationCreate.to_json())

# convert the object into a dict
repo_location_create_dict = repo_location_create_instance.to_dict()
# create an instance of RepoLocationCreate from a dict
repo_location_create_from_dict = RepoLocationCreate.from_dict(repo_location_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


