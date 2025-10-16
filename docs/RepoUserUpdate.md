# RepoUserUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from homebox_client.models.repo_user_update import RepoUserUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of RepoUserUpdate from a JSON string
repo_user_update_instance = RepoUserUpdate.from_json(json)
# print the JSON string representation of the object
print(RepoUserUpdate.to_json())

# convert the object into a dict
repo_user_update_dict = repo_user_update_instance.to_dict()
# create an instance of RepoUserUpdate from a dict
repo_user_update_from_dict = RepoUserUpdate.from_dict(repo_user_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


