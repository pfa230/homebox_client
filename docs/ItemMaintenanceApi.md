# homebox_client.ItemMaintenanceApi

All URIs are relative to *https://demo.homebox.software/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_items_id_maintenance_get**](ItemMaintenanceApi.md#v1_items_id_maintenance_get) | **GET** /v1/items/{id}/maintenance | Get Maintenance Log
[**v1_items_id_maintenance_post**](ItemMaintenanceApi.md#v1_items_id_maintenance_post) | **POST** /v1/items/{id}/maintenance | Create Maintenance Entry


# **v1_items_id_maintenance_get**
> List[RepoMaintenanceEntryWithDetails] v1_items_id_maintenance_get(id, status=status)

Get Maintenance Log

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.repo_maintenance_entry_with_details import RepoMaintenanceEntryWithDetails
from homebox_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demo.homebox.software/api
# See configuration.py for a list of all supported configuration parameters.
configuration = homebox_client.Configuration(
    host = "https://demo.homebox.software/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with homebox_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = homebox_client.ItemMaintenanceApi(api_client)
    id = 'id_example' # str | Item ID
    status = 'status_example' # str |  (optional)

    try:
        # Get Maintenance Log
        api_response = api_instance.v1_items_id_maintenance_get(id, status=status)
        print("The response of ItemMaintenanceApi->v1_items_id_maintenance_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemMaintenanceApi->v1_items_id_maintenance_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item ID | 
 **status** | **str**|  | [optional] 

### Return type

[**List[RepoMaintenanceEntryWithDetails]**](RepoMaintenanceEntryWithDetails.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_items_id_maintenance_post**
> RepoMaintenanceEntry v1_items_id_maintenance_post(id, payload)

Create Maintenance Entry

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.repo_maintenance_entry import RepoMaintenanceEntry
from homebox_client.models.repo_maintenance_entry_create import RepoMaintenanceEntryCreate
from homebox_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demo.homebox.software/api
# See configuration.py for a list of all supported configuration parameters.
configuration = homebox_client.Configuration(
    host = "https://demo.homebox.software/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with homebox_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = homebox_client.ItemMaintenanceApi(api_client)
    id = 'id_example' # str | Item ID
    payload = homebox_client.RepoMaintenanceEntryCreate() # RepoMaintenanceEntryCreate | Entry Data

    try:
        # Create Maintenance Entry
        api_response = api_instance.v1_items_id_maintenance_post(id, payload)
        print("The response of ItemMaintenanceApi->v1_items_id_maintenance_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemMaintenanceApi->v1_items_id_maintenance_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item ID | 
 **payload** | [**RepoMaintenanceEntryCreate**](RepoMaintenanceEntryCreate.md)| Entry Data | 

### Return type

[**RepoMaintenanceEntry**](RepoMaintenanceEntry.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

