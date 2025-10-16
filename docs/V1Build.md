# V1Build


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_time** | **str** |  | [optional] 
**commit** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from homebox_client.models.v1_build import V1Build

# TODO update the JSON string below
json = "{}"
# create an instance of V1Build from a JSON string
v1_build_instance = V1Build.from_json(json)
# print the JSON string representation of the object
print(V1Build.to_json())

# convert the object into a dict
v1_build_dict = v1_build_instance.to_dict()
# create an instance of V1Build from a dict
v1_build_from_dict = V1Build.from_dict(v1_build_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


