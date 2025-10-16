# EntUserEdges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_tokens** | [**List[EntAuthTokens]**](EntAuthTokens.md) | AuthTokens holds the value of the auth_tokens edge. | [optional] 
**group** | [**EntGroup**](EntGroup.md) | Group holds the value of the group edge. | [optional] 
**notifiers** | [**List[EntNotifier]**](EntNotifier.md) | Notifiers holds the value of the notifiers edge. | [optional] 

## Example

```python
from homebox_client.models.ent_user_edges import EntUserEdges

# TODO update the JSON string below
json = "{}"
# create an instance of EntUserEdges from a JSON string
ent_user_edges_instance = EntUserEdges.from_json(json)
# print the JSON string representation of the object
print(EntUserEdges.to_json())

# convert the object into a dict
ent_user_edges_dict = ent_user_edges_instance.to_dict()
# create an instance of EntUserEdges from a dict
ent_user_edges_from_dict = EntUserEdges.from_dict(ent_user_edges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


