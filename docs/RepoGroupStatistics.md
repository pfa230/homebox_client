# RepoGroupStatistics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_item_price** | **float** |  | [optional] 
**total_items** | **int** |  | [optional] 
**total_labels** | **int** |  | [optional] 
**total_locations** | **int** |  | [optional] 
**total_users** | **int** |  | [optional] 
**total_with_warranty** | **int** |  | [optional] 

## Example

```python
from homebox_client.models.repo_group_statistics import RepoGroupStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of RepoGroupStatistics from a JSON string
repo_group_statistics_instance = RepoGroupStatistics.from_json(json)
# print the JSON string representation of the object
print(RepoGroupStatistics.to_json())

# convert the object into a dict
repo_group_statistics_dict = repo_group_statistics_instance.to_dict()
# create an instance of RepoGroupStatistics from a dict
repo_group_statistics_from_dict = RepoGroupStatistics.from_dict(repo_group_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


