# RepoLabelSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from homebox_client.models.repo_label_summary import RepoLabelSummary

# Example JSON string
json = "{}"
# create an instance of RepoLabelSummary from a JSON string
repo_label_summary_instance = RepoLabelSummary.from_json(json)
# print the JSON string representation of the object
print(repo_label_summary_instance.to_json())

# convert the object into a dict
repo_label_summary_dict = repo_label_summary_instance.to_dict()
# create an instance of RepoLabelSummary from a dict
repo_label_summary_from_dict = RepoLabelSummary.from_dict(repo_label_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


