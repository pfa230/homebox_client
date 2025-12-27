# RepoBarcodeProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**barcode** | **str** |  | [optional] 
**image_base64** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**item** | [**RepoItemCreate**](RepoItemCreate.md) |  | [optional] 
**manufacturer** | **str** |  | [optional] 
**model_number** | **str** | Identifications | [optional] 
**notes** | **str** | Extras | [optional] 
**search_engine_name** | **str** |  | [optional] 

## Example

```python
from homebox_client.models.repo_barcode_product import RepoBarcodeProduct

# Example JSON string
json = "{}"
# create an instance of RepoBarcodeProduct from a JSON string
repo_barcode_product_instance = RepoBarcodeProduct.from_json(json)
# print the JSON string representation of the object
print(repo_barcode_product_instance.to_json())

# convert the object into a dict
repo_barcode_product_dict = repo_barcode_product_instance.to_dict()
# create an instance of RepoBarcodeProduct from a dict
repo_barcode_product_from_dict = RepoBarcodeProduct.from_dict(repo_barcode_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


