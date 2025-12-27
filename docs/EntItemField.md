# EntItemField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boolean_value** | **bool** | BooleanValue holds the value of the \&quot;boolean_value\&quot; field. | [optional] 
**created_at** | **str** | CreatedAt holds the value of the \&quot;created_at\&quot; field. | [optional] 
**description** | **str** | Description holds the value of the \&quot;description\&quot; field. | [optional] 
**edges** | [**EntItemFieldEdges**](EntItemFieldEdges.md) | Edges holds the relations/edges for other nodes in the graph. The values are being populated by the ItemFieldQuery when eager-loading is set. | [optional] 
**id** | **str** | ID of the ent. | [optional] 
**name** | **str** | Name holds the value of the \&quot;name\&quot; field. | [optional] 
**number_value** | **int** | NumberValue holds the value of the \&quot;number_value\&quot; field. | [optional] 
**text_value** | **str** | TextValue holds the value of the \&quot;text_value\&quot; field. | [optional] 
**time_value** | **str** | TimeValue holds the value of the \&quot;time_value\&quot; field. | [optional] 
**type** | [**ItemfieldType**](ItemfieldType.md) | Type holds the value of the \&quot;type\&quot; field. | [optional] 
**updated_at** | **str** | UpdatedAt holds the value of the \&quot;updated_at\&quot; field. | [optional] 

## Example

```python
from homebox_client.models.ent_item_field import EntItemField

# Example JSON string
json = "{}"
# create an instance of EntItemField from a JSON string
ent_item_field_instance = EntItemField.from_json(json)
# print the JSON string representation of the object
print(ent_item_field_instance.to_json())

# convert the object into a dict
ent_item_field_dict = ent_item_field_instance.to_dict()
# create an instance of EntItemField from a dict
ent_item_field_from_dict = EntItemField.from_dict(ent_item_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


