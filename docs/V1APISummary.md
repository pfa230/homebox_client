# V1APISummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_registration** | **bool** |  | [optional] 
**build** | [**V1Build**](V1Build.md) |  | [optional] 
**demo** | **bool** |  | [optional] 
**health** | **bool** |  | [optional] 
**label_printing** | **bool** |  | [optional] 
**latest** | [**ServicesLatest**](ServicesLatest.md) |  | [optional] 
**message** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**versions** | **List[str]** |  | [optional] 

## Example

```python
from homebox_client.models.v1_api_summary import V1APISummary

# Example JSON string
json = "{}"
# create an instance of V1APISummary from a JSON string
v1_api_summary_instance = V1APISummary.from_json(json)
# print the JSON string representation of the object
print(v1_api_summary_instance.to_json())

# convert the object into a dict
v1_api_summary_dict = v1_api_summary_instance.to_dict()
# create an instance of V1APISummary from a dict
v1_api_summary_from_dict = V1APISummary.from_dict(v1_api_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


