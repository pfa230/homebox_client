# homebox_client.ItemsApi

All URIs are relative to *https://demo.homebox.software/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_assets_id_get**](ItemsApi.md#v1_assets_id_get) | **GET** /v1/assets/{id} | Get Item by Asset ID
[**v1_items_export_get**](ItemsApi.md#v1_items_export_get) | **GET** /v1/items/export | Export Items
[**v1_items_fields_get**](ItemsApi.md#v1_items_fields_get) | **GET** /v1/items/fields | Get All Custom Field Names
[**v1_items_fields_values_get**](ItemsApi.md#v1_items_fields_values_get) | **GET** /v1/items/fields/values | Get All Custom Field Values
[**v1_items_get**](ItemsApi.md#v1_items_get) | **GET** /v1/items | Query All Items
[**v1_items_id_delete**](ItemsApi.md#v1_items_id_delete) | **DELETE** /v1/items/{id} | Delete Item
[**v1_items_id_duplicate_post**](ItemsApi.md#v1_items_id_duplicate_post) | **POST** /v1/items/{id}/duplicate | Duplicate Item
[**v1_items_id_get**](ItemsApi.md#v1_items_id_get) | **GET** /v1/items/{id} | Get Item
[**v1_items_id_patch**](ItemsApi.md#v1_items_id_patch) | **PATCH** /v1/items/{id} | Update Item
[**v1_items_id_path_get**](ItemsApi.md#v1_items_id_path_get) | **GET** /v1/items/{id}/path | Get the full path of an item
[**v1_items_id_put**](ItemsApi.md#v1_items_id_put) | **PUT** /v1/items/{id} | Update Item
[**v1_items_import_post**](ItemsApi.md#v1_items_import_post) | **POST** /v1/items/import | Import Items
[**v1_items_post**](ItemsApi.md#v1_items_post) | **POST** /v1/items | Create Item
[**v1_labelmaker_assets_id_get**](ItemsApi.md#v1_labelmaker_assets_id_get) | **GET** /v1/labelmaker/assets/{id} | Get Asset label
[**v1_labelmaker_item_id_get**](ItemsApi.md#v1_labelmaker_item_id_get) | **GET** /v1/labelmaker/item/{id} | Get Item label
[**v1_products_search_from_barcode_get**](ItemsApi.md#v1_products_search_from_barcode_get) | **GET** /v1/products/search-from-barcode | Search EAN from Barcode
[**v1_qrcode_get**](ItemsApi.md#v1_qrcode_get) | **GET** /v1/qrcode | Create QR Code


# **v1_assets_id_get**
> RepoPaginationResultRepoItemSummary v1_assets_id_get(id)

Get Item by Asset ID

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.repo_pagination_result_repo_item_summary import RepoPaginationResultRepoItemSummary
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
    api_instance = homebox_client.ItemsApi(api_client)
    id = 'id_example' # str | Asset ID

    try:
        # Get Item by Asset ID
        api_response = api_instance.v1_assets_id_get(id)
        print("The response of ItemsApi->v1_assets_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->v1_assets_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Asset ID | 

### Return type

[**RepoPaginationResultRepoItemSummary**](RepoPaginationResultRepoItemSummary.md)

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

# **v1_items_export_get**
> str v1_items_export_get()

Export Items

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
    api_instance = homebox_client.ItemsApi(api_client)

    try:
        # Export Items
        api_response = api_instance.v1_items_export_get()
        print("The response of ItemsApi->v1_items_export_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->v1_items_export_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | text/csv |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_items_fields_get**
> List[str] v1_items_fields_get()

Get All Custom Field Names

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
    api_instance = homebox_client.ItemsApi(api_client)

    try:
        # Get All Custom Field Names
        api_response = api_instance.v1_items_fields_get()
        print("The response of ItemsApi->v1_items_fields_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->v1_items_fields_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[str]**

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

# **v1_items_fields_values_get**
> List[str] v1_items_fields_values_get()

Get All Custom Field Values

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
    api_instance = homebox_client.ItemsApi(api_client)

    try:
        # Get All Custom Field Values
        api_response = api_instance.v1_items_fields_values_get()
        print("The response of ItemsApi->v1_items_fields_values_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->v1_items_fields_values_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[str]**

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

# **v1_items_get**
> RepoPaginationResultRepoItemSummary v1_items_get(q=q, page=page, page_size=page_size, labels=labels, locations=locations, parent_ids=parent_ids)

Query All Items

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.repo_pagination_result_repo_item_summary import RepoPaginationResultRepoItemSummary
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
    api_instance = homebox_client.ItemsApi(api_client)
    q = 'q_example' # str | search string (optional)
    page = 56 # int | page number (optional)
    page_size = 56 # int | items per page (optional)
    labels = ['labels_example'] # List[str] | label Ids (optional)
    locations = ['locations_example'] # List[str] | location Ids (optional)
    parent_ids = ['parent_ids_example'] # List[str] | parent Ids (optional)

    try:
        # Query All Items
        api_response = api_instance.v1_items_get(q=q, page=page, page_size=page_size, labels=labels, locations=locations, parent_ids=parent_ids)
        print("The response of ItemsApi->v1_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->v1_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| search string | [optional] 
 **page** | **int**| page number | [optional] 
 **page_size** | **int**| items per page | [optional] 
 **labels** | [**List[str]**](str.md)| label Ids | [optional] 
 **locations** | [**List[str]**](str.md)| location Ids | [optional] 
 **parent_ids** | [**List[str]**](str.md)| parent Ids | [optional] 

### Return type

[**RepoPaginationResultRepoItemSummary**](RepoPaginationResultRepoItemSummary.md)

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

# **v1_items_id_delete**
> v1_items_id_delete(id)

Delete Item

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
    api_instance = homebox_client.ItemsApi(api_client)
    id = 'id_example' # str | Item ID

    try:
        # Delete Item
        api_instance.v1_items_id_delete(id)
    except Exception as e:
        print("Exception when calling ItemsApi->v1_items_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item ID | 

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

# **v1_items_id_duplicate_post**
> RepoItemOut v1_items_id_duplicate_post(id, payload)

Duplicate Item

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.repo_duplicate_options import RepoDuplicateOptions
from homebox_client.models.repo_item_out import RepoItemOut
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
    api_instance = homebox_client.ItemsApi(api_client)
    id = 'id_example' # str | Item ID
    payload = homebox_client.RepoDuplicateOptions() # RepoDuplicateOptions | Duplicate Options

    try:
        # Duplicate Item
        api_response = api_instance.v1_items_id_duplicate_post(id, payload)
        print("The response of ItemsApi->v1_items_id_duplicate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->v1_items_id_duplicate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item ID | 
 **payload** | [**RepoDuplicateOptions**](RepoDuplicateOptions.md)| Duplicate Options | 

### Return type

[**RepoItemOut**](RepoItemOut.md)

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

# **v1_items_id_get**
> RepoItemOut v1_items_id_get(id)

Get Item

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.repo_item_out import RepoItemOut
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
    api_instance = homebox_client.ItemsApi(api_client)
    id = 'id_example' # str | Item ID

    try:
        # Get Item
        api_response = api_instance.v1_items_id_get(id)
        print("The response of ItemsApi->v1_items_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->v1_items_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item ID | 

### Return type

[**RepoItemOut**](RepoItemOut.md)

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

# **v1_items_id_patch**
> RepoItemOut v1_items_id_patch(id, payload)

Update Item

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.repo_item_out import RepoItemOut
from homebox_client.models.repo_item_patch import RepoItemPatch
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
    api_instance = homebox_client.ItemsApi(api_client)
    id = 'id_example' # str | Item ID
    payload = homebox_client.RepoItemPatch() # RepoItemPatch | Item Data

    try:
        # Update Item
        api_response = api_instance.v1_items_id_patch(id, payload)
        print("The response of ItemsApi->v1_items_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->v1_items_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item ID | 
 **payload** | [**RepoItemPatch**](RepoItemPatch.md)| Item Data | 

### Return type

[**RepoItemOut**](RepoItemOut.md)

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

# **v1_items_id_path_get**
> List[RepoItemPath] v1_items_id_path_get(id)

Get the full path of an item

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.repo_item_path import RepoItemPath
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
    api_instance = homebox_client.ItemsApi(api_client)
    id = 'id_example' # str | Item ID

    try:
        # Get the full path of an item
        api_response = api_instance.v1_items_id_path_get(id)
        print("The response of ItemsApi->v1_items_id_path_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->v1_items_id_path_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item ID | 

### Return type

[**List[RepoItemPath]**](RepoItemPath.md)

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

# **v1_items_id_put**
> RepoItemOut v1_items_id_put(id, payload)

Update Item

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.repo_item_out import RepoItemOut
from homebox_client.models.repo_item_update import RepoItemUpdate
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
    api_instance = homebox_client.ItemsApi(api_client)
    id = 'id_example' # str | Item ID
    payload = homebox_client.RepoItemUpdate() # RepoItemUpdate | Item Data

    try:
        # Update Item
        api_response = api_instance.v1_items_id_put(id, payload)
        print("The response of ItemsApi->v1_items_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->v1_items_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item ID | 
 **payload** | [**RepoItemUpdate**](RepoItemUpdate.md)| Item Data | 

### Return type

[**RepoItemOut**](RepoItemOut.md)

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

# **v1_items_import_post**
> v1_items_import_post(csv)

Import Items

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
    api_instance = homebox_client.ItemsApi(api_client)
    csv = None # bytearray | Image to upload

    try:
        # Import Items
        api_instance.v1_items_import_post(csv)
    except Exception as e:
        print("Exception when calling ItemsApi->v1_items_import_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csv** | **bytearray**| Image to upload | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_items_post**
> RepoItemSummary v1_items_post(payload)

Create Item

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.repo_item_create import RepoItemCreate
from homebox_client.models.repo_item_summary import RepoItemSummary
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
    api_instance = homebox_client.ItemsApi(api_client)
    payload = homebox_client.RepoItemCreate() # RepoItemCreate | Item Data

    try:
        # Create Item
        api_response = api_instance.v1_items_post(payload)
        print("The response of ItemsApi->v1_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->v1_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**RepoItemCreate**](RepoItemCreate.md)| Item Data | 

### Return type

[**RepoItemSummary**](RepoItemSummary.md)

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

# **v1_labelmaker_assets_id_get**
> str v1_labelmaker_assets_id_get(id, var_print=var_print)

Get Asset label

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
    api_instance = homebox_client.ItemsApi(api_client)
    id = 'id_example' # str | Asset ID
    var_print = True # bool | Print this label, defaults to false (optional)

    try:
        # Get Asset label
        api_response = api_instance.v1_labelmaker_assets_id_get(id, var_print=var_print)
        print("The response of ItemsApi->v1_labelmaker_assets_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->v1_labelmaker_assets_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Asset ID | 
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

# **v1_labelmaker_item_id_get**
> str v1_labelmaker_item_id_get(id, var_print=var_print)

Get Item label

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
    api_instance = homebox_client.ItemsApi(api_client)
    id = 'id_example' # str | Item ID
    var_print = True # bool | Print this label, defaults to false (optional)

    try:
        # Get Item label
        api_response = api_instance.v1_labelmaker_item_id_get(id, var_print=var_print)
        print("The response of ItemsApi->v1_labelmaker_item_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->v1_labelmaker_item_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item ID | 
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

# **v1_products_search_from_barcode_get**
> List[RepoBarcodeProduct] v1_products_search_from_barcode_get(data=data)

Search EAN from Barcode

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.repo_barcode_product import RepoBarcodeProduct
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
    api_instance = homebox_client.ItemsApi(api_client)
    data = 'data_example' # str | barcode to be searched (optional)

    try:
        # Search EAN from Barcode
        api_response = api_instance.v1_products_search_from_barcode_get(data=data)
        print("The response of ItemsApi->v1_products_search_from_barcode_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->v1_products_search_from_barcode_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | **str**| barcode to be searched | [optional] 

### Return type

[**List[RepoBarcodeProduct]**](RepoBarcodeProduct.md)

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

# **v1_qrcode_get**
> str v1_qrcode_get(data=data)

Create QR Code

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
    api_instance = homebox_client.ItemsApi(api_client)
    data = 'data_example' # str | data to be encoded into qrcode (optional)

    try:
        # Create QR Code
        api_response = api_instance.v1_qrcode_get(data=data)
        print("The response of ItemsApi->v1_qrcode_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsApi->v1_qrcode_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | **str**| data to be encoded into qrcode | [optional] 

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
**200** | image/jpeg |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

