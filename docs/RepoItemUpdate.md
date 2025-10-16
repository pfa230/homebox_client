# RepoItemUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archived** | **bool** |  | [optional] 
**asset_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**fields** | [**List[RepoItemField]**](RepoItemField.md) |  | [optional] 
**id** | **str** |  | [optional] 
**insured** | **bool** |  | [optional] 
**label_ids** | **List[str]** |  | [optional] 
**lifetime_warranty** | **bool** | Warranty | [optional] 
**location_id** | **str** | Edges | [optional] 
**manufacturer** | **str** |  | [optional] 
**model_number** | **str** |  | [optional] 
**name** | **str** |  | 
**notes** | **str** | Extras | [optional] 
**parent_id** | **str** |  | [optional] 
**purchase_from** | **str** |  | [optional] 
**purchase_price** | **float** |  | [optional] 
**purchase_time** | **str** | Purchase | [optional] 
**quantity** | **int** |  | [optional] 
**serial_number** | **str** | Identifications | [optional] 
**sold_notes** | **str** |  | [optional] 
**sold_price** | **float** |  | [optional] 
**sold_time** | **str** | Sold | [optional] 
**sold_to** | **str** |  | [optional] 
**sync_child_items_locations** | **bool** |  | [optional] 
**warranty_details** | **str** |  | [optional] 
**warranty_expires** | **str** |  | [optional] 

## Example

```python
from homebox_client.models.repo_item_update import RepoItemUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of RepoItemUpdate from a JSON string
repo_item_update_instance = RepoItemUpdate.from_json(json)
# print the JSON string representation of the object
print(RepoItemUpdate.to_json())

# convert the object into a dict
repo_item_update_dict = repo_item_update_instance.to_dict()
# create an instance of RepoItemUpdate from a dict
repo_item_update_from_dict = RepoItemUpdate.from_dict(repo_item_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


