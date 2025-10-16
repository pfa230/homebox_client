# RepoUserOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**group_id** | **str** |  | [optional] 
**group_name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**is_owner** | **bool** |  | [optional] 
**is_superuser** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from homebox_client.models.repo_user_out import RepoUserOut

# TODO update the JSON string below
json = "{}"
# create an instance of RepoUserOut from a JSON string
repo_user_out_instance = RepoUserOut.from_json(json)
# print the JSON string representation of the object
print(RepoUserOut.to_json())

# convert the object into a dict
repo_user_out_dict = repo_user_out_instance.to_dict()
# create an instance of RepoUserOut from a dict
repo_user_out_from_dict = RepoUserOut.from_dict(repo_user_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


