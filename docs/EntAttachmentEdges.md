# EntAttachmentEdges


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item** | [**EntItem**](EntItem.md) | Item holds the value of the item edge. | [optional] 
**thumbnail** | [**EntAttachment**](EntAttachment.md) | Thumbnail holds the value of the thumbnail edge. | [optional] 

## Example

```python
from homebox_client.models.ent_attachment_edges import EntAttachmentEdges

# TODO update the JSON string below
json = "{}"
# create an instance of EntAttachmentEdges from a JSON string
ent_attachment_edges_instance = EntAttachmentEdges.from_json(json)
# print the JSON string representation of the object
print(EntAttachmentEdges.to_json())

# convert the object into a dict
ent_attachment_edges_dict = ent_attachment_edges_instance.to_dict()
# create an instance of EntAttachmentEdges from a dict
ent_attachment_edges_from_dict = EntAttachmentEdges.from_dict(ent_attachment_edges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


