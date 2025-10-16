# homebox_client.LabelsApi

All URIs are relative to *https://demo.homebox.software/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_labels_get**](LabelsApi.md#v1_labels_get) | **GET** /v1/labels | Get All Labels
[**v1_labels_id_delete**](LabelsApi.md#v1_labels_id_delete) | **DELETE** /v1/labels/{id} | Delete Label
[**v1_labels_id_get**](LabelsApi.md#v1_labels_id_get) | **GET** /v1/labels/{id} | Get Label
[**v1_labels_id_put**](LabelsApi.md#v1_labels_id_put) | **PUT** /v1/labels/{id} | Update Label
[**v1_labels_post**](LabelsApi.md#v1_labels_post) | **POST** /v1/labels | Create Label


# **v1_labels_get**
> List[RepoLabelOut] v1_labels_get()

Get All Labels

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.repo_label_out import RepoLabelOut
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
    api_instance = homebox_client.LabelsApi(api_client)

    try:
        # Get All Labels
        api_response = api_instance.v1_labels_get()
        print("The response of LabelsApi->v1_labels_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LabelsApi->v1_labels_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[RepoLabelOut]**](RepoLabelOut.md)

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

# **v1_labels_id_delete**
> v1_labels_id_delete(id)

Delete Label

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
    api_instance = homebox_client.LabelsApi(api_client)
    id = 'id_example' # str | Label ID

    try:
        # Delete Label
        api_instance.v1_labels_id_delete(id)
    except Exception as e:
        print("Exception when calling LabelsApi->v1_labels_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Label ID | 

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

# **v1_labels_id_get**
> RepoLabelOut v1_labels_id_get(id)

Get Label

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.repo_label_out import RepoLabelOut
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
    api_instance = homebox_client.LabelsApi(api_client)
    id = 'id_example' # str | Label ID

    try:
        # Get Label
        api_response = api_instance.v1_labels_id_get(id)
        print("The response of LabelsApi->v1_labels_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LabelsApi->v1_labels_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Label ID | 

### Return type

[**RepoLabelOut**](RepoLabelOut.md)

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

# **v1_labels_id_put**
> RepoLabelOut v1_labels_id_put(id)

Update Label

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.repo_label_out import RepoLabelOut
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
    api_instance = homebox_client.LabelsApi(api_client)
    id = 'id_example' # str | Label ID

    try:
        # Update Label
        api_response = api_instance.v1_labels_id_put(id)
        print("The response of LabelsApi->v1_labels_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LabelsApi->v1_labels_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Label ID | 

### Return type

[**RepoLabelOut**](RepoLabelOut.md)

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

# **v1_labels_post**
> RepoLabelSummary v1_labels_post(payload)

Create Label

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.repo_label_create import RepoLabelCreate
from homebox_client.models.repo_label_summary import RepoLabelSummary
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
    api_instance = homebox_client.LabelsApi(api_client)
    payload = homebox_client.RepoLabelCreate() # RepoLabelCreate | Label Data

    try:
        # Create Label
        api_response = api_instance.v1_labels_post(payload)
        print("The response of LabelsApi->v1_labels_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LabelsApi->v1_labels_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**RepoLabelCreate**](RepoLabelCreate.md)| Label Data | 

### Return type

[**RepoLabelSummary**](RepoLabelSummary.md)

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

