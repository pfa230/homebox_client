# homebox_client.LocationsApi

All URIs are relative to *https://demo.homebox.software/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_labelmaker_location_id_get**](LocationsApi.md#v1_labelmaker_location_id_get) | **GET** /v1/labelmaker/location/{id} | Get Location label
[**v1_locations_get**](LocationsApi.md#v1_locations_get) | **GET** /v1/locations | Get All Locations
[**v1_locations_id_delete**](LocationsApi.md#v1_locations_id_delete) | **DELETE** /v1/locations/{id} | Delete Location
[**v1_locations_id_get**](LocationsApi.md#v1_locations_id_get) | **GET** /v1/locations/{id} | Get Location
[**v1_locations_id_put**](LocationsApi.md#v1_locations_id_put) | **PUT** /v1/locations/{id} | Update Location
[**v1_locations_post**](LocationsApi.md#v1_locations_post) | **POST** /v1/locations | Create Location
[**v1_locations_tree_get**](LocationsApi.md#v1_locations_tree_get) | **GET** /v1/locations/tree | Get Locations Tree


# **v1_labelmaker_location_id_get**
> str v1_labelmaker_location_id_get(id, var_print=var_print)

Get Location label

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
    api_instance = homebox_client.LocationsApi(api_client)
    id = 'id_example' # str | Location ID
    var_print = True # bool | Print this label, defaults to false (optional)

    try:
        # Get Location label
        api_response = api_instance.v1_labelmaker_location_id_get(id, var_print=var_print)
        print("The response of LocationsApi->v1_labelmaker_location_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->v1_labelmaker_location_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Location ID | 
 **var_print** | **bool**| Print this label, defaults to false | [optional] 

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | image/png |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_locations_get**
> List[RepoLocationOutCount] v1_locations_get(filter_children=filter_children)

Get All Locations

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.repo_location_out_count import RepoLocationOutCount
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
    api_instance = homebox_client.LocationsApi(api_client)
    filter_children = True # bool | Filter locations with parents (optional)

    try:
        # Get All Locations
        api_response = api_instance.v1_locations_get(filter_children=filter_children)
        print("The response of LocationsApi->v1_locations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->v1_locations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_children** | **bool**| Filter locations with parents | [optional] 

### Return type

[**List[RepoLocationOutCount]**](RepoLocationOutCount.md)

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

# **v1_locations_id_delete**
> v1_locations_id_delete(id)

Delete Location

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
    api_instance = homebox_client.LocationsApi(api_client)
    id = 'id_example' # str | Location ID

    try:
        # Delete Location
        api_instance.v1_locations_id_delete(id)
    except Exception as e:
        print("Exception when calling LocationsApi->v1_locations_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Location ID | 

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

# **v1_locations_id_get**
> RepoLocationOut v1_locations_id_get(id)

Get Location

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.repo_location_out import RepoLocationOut
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
    api_instance = homebox_client.LocationsApi(api_client)
    id = 'id_example' # str | Location ID

    try:
        # Get Location
        api_response = api_instance.v1_locations_id_get(id)
        print("The response of LocationsApi->v1_locations_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->v1_locations_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Location ID | 

### Return type

[**RepoLocationOut**](RepoLocationOut.md)

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

# **v1_locations_id_put**
> RepoLocationOut v1_locations_id_put(id, payload)

Update Location

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.repo_location_out import RepoLocationOut
from homebox_client.models.repo_location_update import RepoLocationUpdate
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
    api_instance = homebox_client.LocationsApi(api_client)
    id = 'id_example' # str | Location ID
    payload = homebox_client.RepoLocationUpdate() # RepoLocationUpdate | Location Data

    try:
        # Update Location
        api_response = api_instance.v1_locations_id_put(id, payload)
        print("The response of LocationsApi->v1_locations_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->v1_locations_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Location ID | 
 **payload** | [**RepoLocationUpdate**](RepoLocationUpdate.md)| Location Data | 

### Return type

[**RepoLocationOut**](RepoLocationOut.md)

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

# **v1_locations_post**
> RepoLocationSummary v1_locations_post(payload)

Create Location

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.repo_location_create import RepoLocationCreate
from homebox_client.models.repo_location_summary import RepoLocationSummary
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
    api_instance = homebox_client.LocationsApi(api_client)
    payload = homebox_client.RepoLocationCreate() # RepoLocationCreate | Location Data

    try:
        # Create Location
        api_response = api_instance.v1_locations_post(payload)
        print("The response of LocationsApi->v1_locations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->v1_locations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**RepoLocationCreate**](RepoLocationCreate.md)| Location Data | 

### Return type

[**RepoLocationSummary**](RepoLocationSummary.md)

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

# **v1_locations_tree_get**
> List[RepoTreeItem] v1_locations_tree_get(with_items=with_items)

Get Locations Tree

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.repo_tree_item import RepoTreeItem
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
    api_instance = homebox_client.LocationsApi(api_client)
    with_items = True # bool | include items in response tree (optional)

    try:
        # Get Locations Tree
        api_response = api_instance.v1_locations_tree_get(with_items=with_items)
        print("The response of LocationsApi->v1_locations_tree_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->v1_locations_tree_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **with_items** | **bool**| include items in response tree | [optional] 

### Return type

[**List[RepoTreeItem]**](RepoTreeItem.md)

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

