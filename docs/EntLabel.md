# EntLabel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** | Color holds the value of the \&quot;color\&quot; field. | [optional] 
**created_at** | **str** | CreatedAt holds the value of the \&quot;created_at\&quot; field. | [optional] 
**description** | **str** | Description holds the value of the \&quot;description\&quot; field. | [optional] 
**edges** | [**EntLabelEdges**](EntLabelEdges.md) | Edges holds the relations/edges for other nodes in the graph. The values are being populated by the LabelQuery when eager-loading is set. | [optional] 
**id** | **str** | ID of the ent. | [optional] 
**name** | **str** | Name holds the value of the \&quot;name\&quot; field. | [optional] 
**updated_at** | **str** | UpdatedAt holds the value of the \&quot;updated_at\&quot; field. | [optional] 

## Example

```python
from homebox_client.models.ent_label import EntLabel

# Example JSON string
json = "{}"
# create an instance of EntLabel from a JSON string
ent_label_instance = EntLabel.from_json(json)
# print the JSON string representation of the object
print(ent_label_instance.to_json())

# convert the object into a dict
ent_label_dict = ent_label_instance.to_dict()
# create an instance of EntLabel from a dict
ent_label_from_dict = EntLabel.from_dict(ent_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


