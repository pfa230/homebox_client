# EntNotifierEdges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | [**EntGroup**](EntGroup.md) | Group holds the value of the group edge. | [optional] 
**user** | [**EntUser**](EntUser.md) | User holds the value of the user edge. | [optional] 

## Example

```python
from homebox_client.models.ent_notifier_edges import EntNotifierEdges

# TODO update the JSON string below
json = "{}"
# create an instance of EntNotifierEdges from a JSON string
ent_notifier_edges_instance = EntNotifierEdges.from_json(json)
# print the JSON string representation of the object
print(EntNotifierEdges.to_json())

# convert the object into a dict
ent_notifier_edges_dict = ent_notifier_edges_instance.to_dict()
# create an instance of EntNotifierEdges from a dict
ent_notifier_edges_from_dict = EntNotifierEdges.from_dict(ent_notifier_edges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


