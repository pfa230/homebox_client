# homebox_client.MaintenanceApi

All URIs are relative to *https://demo.homebox.software/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_maintenance_get**](MaintenanceApi.md#v1_maintenance_get) | **GET** /v1/maintenance | Query All Maintenance
[**v1_maintenance_id_delete**](MaintenanceApi.md#v1_maintenance_id_delete) | **DELETE** /v1/maintenance/{id} | Delete Maintenance Entry
[**v1_maintenance_id_put**](MaintenanceApi.md#v1_maintenance_id_put) | **PUT** /v1/maintenance/{id} | Update Maintenance Entry


# **v1_maintenance_get**
> List[RepoMaintenanceEntryWithDetails] v1_maintenance_get(status=status)

Query All Maintenance

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
    api_instance = homebox_client.MaintenanceApi(api_client)
    status = 'status_example' # str |  (optional)

    try:
        # Query All Maintenance
        api_response = api_instance.v1_maintenance_get(status=status)
        print("The response of MaintenanceApi->v1_maintenance_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaintenanceApi->v1_maintenance_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **v1_maintenance_id_delete**
> v1_maintenance_id_delete(id)

Delete Maintenance Entry

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
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
    api_instance = homebox_client.MaintenanceApi(api_client)
    id = 'id_example' # str | Maintenance ID

    try:
        # Delete Maintenance Entry
        api_instance.v1_maintenance_id_delete(id)
    except Exception as e:
        print("Exception when calling MaintenanceApi->v1_maintenance_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Maintenance ID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_maintenance_id_put**
> RepoMaintenanceEntry v1_maintenance_id_put(id, payload)

Update Maintenance Entry

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.repo_maintenance_entry import RepoMaintenanceEntry
from homebox_client.models.repo_maintenance_entry_update import RepoMaintenanceEntryUpdate
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
    api_instance = homebox_client.MaintenanceApi(api_client)
    id = 'id_example' # str | Maintenance ID
    payload = homebox_client.RepoMaintenanceEntryUpdate() # RepoMaintenanceEntryUpdate | Entry Data

    try:
        # Update Maintenance Entry
        api_response = api_instance.v1_maintenance_id_put(id, payload)
        print("The response of MaintenanceApi->v1_maintenance_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaintenanceApi->v1_maintenance_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Maintenance ID | 
 **payload** | [**RepoMaintenanceEntryUpdate**](RepoMaintenanceEntryUpdate.md)| Entry Data | 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

