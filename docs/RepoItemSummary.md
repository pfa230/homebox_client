# RepoItemSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archived** | **bool** |  | [optional] 
**asset_id** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**image_id** | **str** |  | [optional] 
**insured** | **bool** |  | [optional] 
**labels** | [**List[RepoLabelSummary]**](RepoLabelSummary.md) |  | [optional] 
**location** | [**RepoLocationSummary**](RepoLocationSummary.md) | Edges | [optional] 
**name** | **str** |  | [optional] 
**purchase_price** | **float** |  | [optional] 
**quantity** | **int** |  | [optional] 
**sold_time** | **str** | Sale details | [optional] 
**thumbnail_id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from homebox_client.models.repo_item_summary import RepoItemSummary

# Example JSON string
json = "{}"
# create an instance of RepoItemSummary from a JSON string
repo_item_summary_instance = RepoItemSummary.from_json(json)
# print the JSON string representation of the object
print(repo_item_summary_instance.to_json())

# convert the object into a dict
repo_item_summary_dict = repo_item_summary_instance.to_dict()
# create an instance of RepoItemSummary from a dict
repo_item_summary_from_dict = RepoItemSummary.from_dict(repo_item_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


