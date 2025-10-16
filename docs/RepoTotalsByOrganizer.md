# RepoTotalsByOrganizer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**total** | **float** |  | [optional] 

## Example

```python
from homebox_client.models.repo_totals_by_organizer import RepoTotalsByOrganizer

# TODO update the JSON string below
json = "{}"
# create an instance of RepoTotalsByOrganizer from a JSON string
repo_totals_by_organizer_instance = RepoTotalsByOrganizer.from_json(json)
# print the JSON string representation of the object
print(RepoTotalsByOrganizer.to_json())

# convert the object into a dict
repo_totals_by_organizer_dict = repo_totals_by_organizer_instance.to_dict()
# create an instance of RepoTotalsByOrganizer from a dict
repo_totals_by_organizer_from_dict = RepoTotalsByOrganizer.from_dict(repo_totals_by_organizer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


