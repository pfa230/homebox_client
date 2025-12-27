# RepoPaginationResultRepoItemSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[RepoItemSummary]**](RepoItemSummary.md) |  | [optional] 
**page** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from homebox_client.models.repo_pagination_result_repo_item_summary import RepoPaginationResultRepoItemSummary

# Example JSON string
json = "{}"
# create an instance of RepoPaginationResultRepoItemSummary from a JSON string
repo_pagination_result_repo_item_summary_instance = RepoPaginationResultRepoItemSummary.from_json(json)
# print the JSON string representation of the object
print(repo_pagination_result_repo_item_summary_instance.to_json())

# convert the object into a dict
repo_pagination_result_repo_item_summary_dict = repo_pagination_result_repo_item_summary_instance.to_dict()
# create an instance of RepoPaginationResultRepoItemSummary from a dict
repo_pagination_result_repo_item_summary_from_dict = RepoPaginationResultRepoItemSummary.from_dict(repo_pagination_result_repo_item_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


