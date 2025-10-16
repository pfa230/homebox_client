# homebox_client.NotifiersApi

All URIs are relative to *https://demo.homebox.software/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_notifiers_get**](NotifiersApi.md#v1_notifiers_get) | **GET** /v1/notifiers | Get Notifiers
[**v1_notifiers_id_delete**](NotifiersApi.md#v1_notifiers_id_delete) | **DELETE** /v1/notifiers/{id} | Delete a Notifier
[**v1_notifiers_id_put**](NotifiersApi.md#v1_notifiers_id_put) | **PUT** /v1/notifiers/{id} | Update Notifier
[**v1_notifiers_post**](NotifiersApi.md#v1_notifiers_post) | **POST** /v1/notifiers | Create Notifier
[**v1_notifiers_test_post**](NotifiersApi.md#v1_notifiers_test_post) | **POST** /v1/notifiers/test | Test Notifier


# **v1_notifiers_get**
> List[RepoNotifierOut] v1_notifiers_get()

Get Notifiers

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.repo_notifier_out import RepoNotifierOut
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
    api_instance = homebox_client.NotifiersApi(api_client)

    try:
        # Get Notifiers
        api_response = api_instance.v1_notifiers_get()
        print("The response of NotifiersApi->v1_notifiers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotifiersApi->v1_notifiers_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[RepoNotifierOut]**](RepoNotifierOut.md)

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

# **v1_notifiers_id_delete**
> v1_notifiers_id_delete(id)

Delete a Notifier

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
    api_instance = homebox_client.NotifiersApi(api_client)
    id = 'id_example' # str | Notifier ID

    try:
        # Delete a Notifier
        api_instance.v1_notifiers_id_delete(id)
    except Exception as e:
        print("Exception when calling NotifiersApi->v1_notifiers_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Notifier ID | 

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

# **v1_notifiers_id_put**
> RepoNotifierOut v1_notifiers_id_put(id, payload)

Update Notifier

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.repo_notifier_out import RepoNotifierOut
from homebox_client.models.repo_notifier_update import RepoNotifierUpdate
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
    api_instance = homebox_client.NotifiersApi(api_client)
    id = 'id_example' # str | Notifier ID
    payload = homebox_client.RepoNotifierUpdate() # RepoNotifierUpdate | Notifier Data

    try:
        # Update Notifier
        api_response = api_instance.v1_notifiers_id_put(id, payload)
        print("The response of NotifiersApi->v1_notifiers_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotifiersApi->v1_notifiers_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Notifier ID | 
 **payload** | [**RepoNotifierUpdate**](RepoNotifierUpdate.md)| Notifier Data | 

### Return type

[**RepoNotifierOut**](RepoNotifierOut.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_notifiers_post**
> RepoNotifierOut v1_notifiers_post(payload)

Create Notifier

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.repo_notifier_create import RepoNotifierCreate
from homebox_client.models.repo_notifier_out import RepoNotifierOut
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
    api_instance = homebox_client.NotifiersApi(api_client)
    payload = homebox_client.RepoNotifierCreate() # RepoNotifierCreate | Notifier Data

    try:
        # Create Notifier
        api_response = api_instance.v1_notifiers_post(payload)
        print("The response of NotifiersApi->v1_notifiers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotifiersApi->v1_notifiers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**RepoNotifierCreate**](RepoNotifierCreate.md)| Notifier Data | 

### Return type

[**RepoNotifierOut**](RepoNotifierOut.md)

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

# **v1_notifiers_test_post**
> v1_notifiers_test_post(url)

Test Notifier

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
    api_instance = homebox_client.NotifiersApi(api_client)
    url = 'url_example' # str | URL

    try:
        # Test Notifier
        api_instance.v1_notifiers_test_post(url)
    except Exception as e:
        print("Exception when calling NotifiersApi->v1_notifiers_test_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| URL | 

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

