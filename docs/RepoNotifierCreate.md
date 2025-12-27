# RepoNotifierCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_active** | **bool** |  | [optional] 
**name** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from homebox_client.models.repo_notifier_create import RepoNotifierCreate

# Example JSON string
json = "{}"
# create an instance of RepoNotifierCreate from a JSON string
repo_notifier_create_instance = RepoNotifierCreate.from_json(json)
# print the JSON string representation of the object
print(repo_notifier_create_instance.to_json())

# convert the object into a dict
repo_notifier_create_dict = repo_notifier_create_instance.to_dict()
# create an instance of RepoNotifierCreate from a dict
repo_notifier_create_from_dict = RepoNotifierCreate.from_dict(repo_notifier_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


