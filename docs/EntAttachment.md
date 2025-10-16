# EntAttachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | CreatedAt holds the value of the \&quot;created_at\&quot; field. | [optional] 
**edges** | [**EntAttachmentEdges**](EntAttachmentEdges.md) | Edges holds the relations/edges for other nodes in the graph. The values are being populated by the AttachmentQuery when eager-loading is set. | [optional] 
**id** | **str** | ID of the ent. | [optional] 
**mime_type** | **str** | MimeType holds the value of the \&quot;mime_type\&quot; field. | [optional] 
**path** | **str** | Path holds the value of the \&quot;path\&quot; field. | [optional] 
**primary** | **bool** | Primary holds the value of the \&quot;primary\&quot; field. | [optional] 
**title** | **str** | Title holds the value of the \&quot;title\&quot; field. | [optional] 
**type** | [**AttachmentType**](AttachmentType.md) | Type holds the value of the \&quot;type\&quot; field. | [optional] 
**updated_at** | **str** | UpdatedAt holds the value of the \&quot;updated_at\&quot; field. | [optional] 

## Example

```python
from homebox_client.models.ent_attachment import EntAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of EntAttachment from a JSON string
ent_attachment_instance = EntAttachment.from_json(json)
# print the JSON string representation of the object
print(EntAttachment.to_json())

# convert the object into a dict
ent_attachment_dict = ent_attachment_instance.to_dict()
# create an instance of EntAttachment from a dict
ent_attachment_from_dict = EntAttachment.from_dict(ent_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


