# RepoNotifierOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**group_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 

## Example

```python
from homebox_client.models.repo_notifier_out import RepoNotifierOut

# TODO update the JSON string below
json = "{}"
# create an instance of RepoNotifierOut from a JSON string
repo_notifier_out_instance = RepoNotifierOut.from_json(json)
# print the JSON string representation of the object
print(RepoNotifierOut.to_json())

# convert the object into a dict
repo_notifier_out_dict = repo_notifier_out_instance.to_dict()
# create an instance of RepoNotifierOut from a dict
repo_notifier_out_from_dict = RepoNotifierOut.from_dict(repo_notifier_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


