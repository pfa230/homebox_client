# homebox_client.ActionsApi

All URIs are relative to *https://demo.homebox.software/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_actions_create_missing_thumbnails_post**](ActionsApi.md#v1_actions_create_missing_thumbnails_post) | **POST** /v1/actions/create-missing-thumbnails | Create Missing Thumbnails
[**v1_actions_ensure_asset_ids_post**](ActionsApi.md#v1_actions_ensure_asset_ids_post) | **POST** /v1/actions/ensure-asset-ids | Ensure Asset IDs
[**v1_actions_ensure_import_refs_post**](ActionsApi.md#v1_actions_ensure_import_refs_post) | **POST** /v1/actions/ensure-import-refs | Ensures Import Refs
[**v1_actions_set_primary_photos_post**](ActionsApi.md#v1_actions_set_primary_photos_post) | **POST** /v1/actions/set-primary-photos | Set Primary Photos
[**v1_actions_zero_item_time_fields_post**](ActionsApi.md#v1_actions_zero_item_time_fields_post) | **POST** /v1/actions/zero-item-time-fields | Zero Out Time Fields


# **v1_actions_create_missing_thumbnails_post**
> V1ActionAmountResult v1_actions_create_missing_thumbnails_post()

Create Missing Thumbnails

Creates thumbnails for items that are missing them

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.v1_action_amount_result import V1ActionAmountResult
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
    api_instance = homebox_client.ActionsApi(api_client)

    try:
        # Create Missing Thumbnails
        api_response = api_instance.v1_actions_create_missing_thumbnails_post()
        print("The response of ActionsApi->v1_actions_create_missing_thumbnails_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->v1_actions_create_missing_thumbnails_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1ActionAmountResult**](V1ActionAmountResult.md)

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

# **v1_actions_ensure_asset_ids_post**
> V1ActionAmountResult v1_actions_ensure_asset_ids_post()

Ensure Asset IDs

Ensures all items in the database have an asset ID

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.v1_action_amount_result import V1ActionAmountResult
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
    api_instance = homebox_client.ActionsApi(api_client)

    try:
        # Ensure Asset IDs
        api_response = api_instance.v1_actions_ensure_asset_ids_post()
        print("The response of ActionsApi->v1_actions_ensure_asset_ids_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->v1_actions_ensure_asset_ids_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1ActionAmountResult**](V1ActionAmountResult.md)

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

# **v1_actions_ensure_import_refs_post**
> V1ActionAmountResult v1_actions_ensure_import_refs_post()

Ensures Import Refs

Ensures all items in the database have an import ref

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.v1_action_amount_result import V1ActionAmountResult
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
    api_instance = homebox_client.ActionsApi(api_client)

    try:
        # Ensures Import Refs
        api_response = api_instance.v1_actions_ensure_import_refs_post()
        print("The response of ActionsApi->v1_actions_ensure_import_refs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->v1_actions_ensure_import_refs_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1ActionAmountResult**](V1ActionAmountResult.md)

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

# **v1_actions_set_primary_photos_post**
> V1ActionAmountResult v1_actions_set_primary_photos_post()

Set Primary Photos

Sets the first photo of each item as the primary photo

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.v1_action_amount_result import V1ActionAmountResult
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
    api_instance = homebox_client.ActionsApi(api_client)

    try:
        # Set Primary Photos
        api_response = api_instance.v1_actions_set_primary_photos_post()
        print("The response of ActionsApi->v1_actions_set_primary_photos_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->v1_actions_set_primary_photos_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1ActionAmountResult**](V1ActionAmountResult.md)

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

# **v1_actions_zero_item_time_fields_post**
> V1ActionAmountResult v1_actions_zero_item_time_fields_post()

Zero Out Time Fields

Resets all item date fields to the beginning of the day

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.v1_action_amount_result import V1ActionAmountResult
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
    api_instance = homebox_client.ActionsApi(api_client)

    try:
        # Zero Out Time Fields
        api_response = api_instance.v1_actions_zero_item_time_fields_post()
        print("The response of ActionsApi->v1_actions_zero_item_time_fields_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActionsApi->v1_actions_zero_item_time_fields_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1ActionAmountResult**](V1ActionAmountResult.md)

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

