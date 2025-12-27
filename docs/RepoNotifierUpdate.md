# RepoNotifierUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_active** | **bool** |  | [optional] 
**name** | **str** |  | 
**url** | **str** |  | [optional] 

## Example

```python
from homebox_client.models.repo_notifier_update import RepoNotifierUpdate

# Example JSON string
json = "{}"
# create an instance of RepoNotifierUpdate from a JSON string
repo_notifier_update_instance = RepoNotifierUpdate.from_json(json)
# print the JSON string representation of the object
print(repo_notifier_update_instance.to_json())

# convert the object into a dict
repo_notifier_update_dict = repo_notifier_update_instance.to_dict()
# create an instance of RepoNotifierUpdate from a dict
repo_notifier_update_from_dict = RepoNotifierUpdate.from_dict(repo_notifier_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


