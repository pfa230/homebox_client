# EntGroupEdges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invitation_tokens** | [**List[EntGroupInvitationToken]**](EntGroupInvitationToken.md) | InvitationTokens holds the value of the invitation_tokens edge. | [optional] 
**items** | [**List[EntItem]**](EntItem.md) | Items holds the value of the items edge. | [optional] 
**labels** | [**List[EntLabel]**](EntLabel.md) | Labels holds the value of the labels edge. | [optional] 
**locations** | [**List[EntLocation]**](EntLocation.md) | Locations holds the value of the locations edge. | [optional] 
**notifiers** | [**List[EntNotifier]**](EntNotifier.md) | Notifiers holds the value of the notifiers edge. | [optional] 
**users** | [**List[EntUser]**](EntUser.md) | Users holds the value of the users edge. | [optional] 

## Example

```python
from homebox_client.models.ent_group_edges import EntGroupEdges

# TODO update the JSON string below
json = "{}"
# create an instance of EntGroupEdges from a JSON string
ent_group_edges_instance = EntGroupEdges.from_json(json)
# print the JSON string representation of the object
print(EntGroupEdges.to_json())

# convert the object into a dict
ent_group_edges_dict = ent_group_edges_instance.to_dict()
# create an instance of EntGroupEdges from a dict
ent_group_edges_from_dict = EntGroupEdges.from_dict(ent_group_edges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


