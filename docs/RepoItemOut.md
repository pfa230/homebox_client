# RepoItemOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archived** | **bool** |  | [optional] 
**asset_id** | **str** |  | [optional] 
**attachments** | [**List[RepoItemAttachment]**](RepoItemAttachment.md) |  | [optional] 
**created_at** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**fields** | [**List[RepoItemField]**](RepoItemField.md) |  | [optional] 
**id** | **str** |  | [optional] 
**image_id** | **str** |  | [optional] 
**insured** | **bool** |  | [optional] 
**labels** | [**List[RepoLabelSummary]**](RepoLabelSummary.md) |  | [optional] 
**lifetime_warranty** | **bool** | Warranty | [optional] 
**location** | [**RepoLocationSummary**](RepoLocationSummary.md) | Edges | [optional] 
**manufacturer** | **str** |  | [optional] 
**model_number** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**notes** | **str** | Extras | [optional] 
**parent** | [**RepoItemSummary**](RepoItemSummary.md) |  | [optional] 
**purchase_from** | **str** |  | [optional] 
**purchase_price** | **float** |  | [optional] 
**purchase_time** | **str** | Purchase | [optional] 
**quantity** | **int** |  | [optional] 
**serial_number** | **str** |  | [optional] 
**sold_notes** | **str** |  | [optional] 
**sold_price** | **float** |  | [optional] 
**sold_time** | **str** | Sold | [optional] 
**sold_to** | **str** |  | [optional] 
**sync_child_items_locations** | **bool** |  | [optional] 
**thumbnail_id** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**warranty_details** | **str** |  | [optional] 
**warranty_expires** | **str** |  | [optional] 

## Example

```python
from homebox_client.models.repo_item_out import RepoItemOut

# Example JSON string
json = "{}"
# create an instance of RepoItemOut from a JSON string
repo_item_out_instance = RepoItemOut.from_json(json)
# print the JSON string representation of the object
print(repo_item_out_instance.to_json())

# convert the object into a dict
repo_item_out_dict = repo_item_out_instance.to_dict()
# create an instance of RepoItemOut from a dict
repo_item_out_from_dict = RepoItemOut.from_dict(repo_item_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


