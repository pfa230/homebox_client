# EntItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archived** | **bool** | Archived holds the value of the \&quot;archived\&quot; field. | [optional] 
**asset_id** | **int** | AssetID holds the value of the \&quot;asset_id\&quot; field. | [optional] 
**created_at** | **str** | CreatedAt holds the value of the \&quot;created_at\&quot; field. | [optional] 
**description** | **str** | Description holds the value of the \&quot;description\&quot; field. | [optional] 
**edges** | [**EntItemEdges**](EntItemEdges.md) | Edges holds the relations/edges for other nodes in the graph. The values are being populated by the ItemQuery when eager-loading is set. | [optional] 
**id** | **str** | ID of the ent. | [optional] 
**import_ref** | **str** | ImportRef holds the value of the \&quot;import_ref\&quot; field. | [optional] 
**insured** | **bool** | Insured holds the value of the \&quot;insured\&quot; field. | [optional] 
**lifetime_warranty** | **bool** | LifetimeWarranty holds the value of the \&quot;lifetime_warranty\&quot; field. | [optional] 
**manufacturer** | **str** | Manufacturer holds the value of the \&quot;manufacturer\&quot; field. | [optional] 
**model_number** | **str** | ModelNumber holds the value of the \&quot;model_number\&quot; field. | [optional] 
**name** | **str** | Name holds the value of the \&quot;name\&quot; field. | [optional] 
**notes** | **str** | Notes holds the value of the \&quot;notes\&quot; field. | [optional] 
**purchase_from** | **str** | PurchaseFrom holds the value of the \&quot;purchase_from\&quot; field. | [optional] 
**purchase_price** | **float** | PurchasePrice holds the value of the \&quot;purchase_price\&quot; field. | [optional] 
**purchase_time** | **str** | PurchaseTime holds the value of the \&quot;purchase_time\&quot; field. | [optional] 
**quantity** | **int** | Quantity holds the value of the \&quot;quantity\&quot; field. | [optional] 
**serial_number** | **str** | SerialNumber holds the value of the \&quot;serial_number\&quot; field. | [optional] 
**sold_notes** | **str** | SoldNotes holds the value of the \&quot;sold_notes\&quot; field. | [optional] 
**sold_price** | **float** | SoldPrice holds the value of the \&quot;sold_price\&quot; field. | [optional] 
**sold_time** | **str** | SoldTime holds the value of the \&quot;sold_time\&quot; field. | [optional] 
**sold_to** | **str** | SoldTo holds the value of the \&quot;sold_to\&quot; field. | [optional] 
**sync_child_items_locations** | **bool** | SyncChildItemsLocations holds the value of the \&quot;sync_child_items_locations\&quot; field. | [optional] 
**updated_at** | **str** | UpdatedAt holds the value of the \&quot;updated_at\&quot; field. | [optional] 
**warranty_details** | **str** | WarrantyDetails holds the value of the \&quot;warranty_details\&quot; field. | [optional] 
**warranty_expires** | **str** | WarrantyExpires holds the value of the \&quot;warranty_expires\&quot; field. | [optional] 

## Example

```python
from homebox_client.models.ent_item import EntItem

# TODO update the JSON string below
json = "{}"
# create an instance of EntItem from a JSON string
ent_item_instance = EntItem.from_json(json)
# print the JSON string representation of the object
print(EntItem.to_json())

# convert the object into a dict
ent_item_dict = ent_item_instance.to_dict()
# create an instance of EntItem from a dict
ent_item_from_dict = EntItem.from_dict(ent_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


