# EntNotifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | CreatedAt holds the value of the \&quot;created_at\&quot; field. | [optional] 
**edges** | [**EntNotifierEdges**](EntNotifierEdges.md) | Edges holds the relations/edges for other nodes in the graph. The values are being populated by the NotifierQuery when eager-loading is set. | [optional] 
**group_id** | **str** | GroupID holds the value of the \&quot;group_id\&quot; field. | [optional] 
**id** | **str** | ID of the ent. | [optional] 
**is_active** | **bool** | IsActive holds the value of the \&quot;is_active\&quot; field. | [optional] 
**name** | **str** | Name holds the value of the \&quot;name\&quot; field. | [optional] 
**updated_at** | **str** | UpdatedAt holds the value of the \&quot;updated_at\&quot; field. | [optional] 
**user_id** | **str** | UserID holds the value of the \&quot;user_id\&quot; field. | [optional] 

## Example

```python
from homebox_client.models.ent_notifier import EntNotifier

# TODO update the JSON string below
json = "{}"
# create an instance of EntNotifier from a JSON string
ent_notifier_instance = EntNotifier.from_json(json)
# print the JSON string representation of the object
print(EntNotifier.to_json())

# convert the object into a dict
ent_notifier_dict = ent_notifier_instance.to_dict()
# create an instance of EntNotifier from a dict
ent_notifier_from_dict = EntNotifier.from_dict(ent_notifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


