# homebox_client.ItemsAttachmentsApi

All URIs are relative to *https://demo.homebox.software/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_items_id_attachments_attachment_id_delete**](ItemsAttachmentsApi.md#v1_items_id_attachments_attachment_id_delete) | **DELETE** /v1/items/{id}/attachments/{attachment_id} | Delete Item Attachment
[**v1_items_id_attachments_attachment_id_get**](ItemsAttachmentsApi.md#v1_items_id_attachments_attachment_id_get) | **GET** /v1/items/{id}/attachments/{attachment_id} | Get Item Attachment
[**v1_items_id_attachments_attachment_id_put**](ItemsAttachmentsApi.md#v1_items_id_attachments_attachment_id_put) | **PUT** /v1/items/{id}/attachments/{attachment_id} | Update Item Attachment
[**v1_items_id_attachments_post**](ItemsAttachmentsApi.md#v1_items_id_attachments_post) | **POST** /v1/items/{id}/attachments | Create Item Attachment


# **v1_items_id_attachments_attachment_id_delete**
> v1_items_id_attachments_attachment_id_delete(id, attachment_id)

Delete Item Attachment

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
    api_instance = homebox_client.ItemsAttachmentsApi(api_client)
    id = 'id_example' # str | Item ID
    attachment_id = 'attachment_id_example' # str | Attachment ID

    try:
        # Delete Item Attachment
        api_instance.v1_items_id_attachments_attachment_id_delete(id, attachment_id)
    except Exception as e:
        print("Exception when calling ItemsAttachmentsApi->v1_items_id_attachments_attachment_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item ID | 
 **attachment_id** | **str**| Attachment ID | 

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

# **v1_items_id_attachments_attachment_id_get**
> V1ItemAttachmentToken v1_items_id_attachments_attachment_id_get(id, attachment_id)

Get Item Attachment

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.v1_item_attachment_token import V1ItemAttachmentToken
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
    api_instance = homebox_client.ItemsAttachmentsApi(api_client)
    id = 'id_example' # str | Item ID
    attachment_id = 'attachment_id_example' # str | Attachment ID

    try:
        # Get Item Attachment
        api_response = api_instance.v1_items_id_attachments_attachment_id_get(id, attachment_id)
        print("The response of ItemsAttachmentsApi->v1_items_id_attachments_attachment_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsAttachmentsApi->v1_items_id_attachments_attachment_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item ID | 
 **attachment_id** | **str**| Attachment ID | 

### Return type

[**V1ItemAttachmentToken**](V1ItemAttachmentToken.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_items_id_attachments_attachment_id_put**
> RepoItemOut v1_items_id_attachments_attachment_id_put(id, attachment_id, payload)

Update Item Attachment

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.repo_item_attachment_update import RepoItemAttachmentUpdate
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
    api_instance = homebox_client.ItemsAttachmentsApi(api_client)
    id = 'id_example' # str | Item ID
    attachment_id = 'attachment_id_example' # str | Attachment ID
    payload = homebox_client.RepoItemAttachmentUpdate() # RepoItemAttachmentUpdate | Attachment Update

    try:
        # Update Item Attachment
        api_response = api_instance.v1_items_id_attachments_attachment_id_put(id, attachment_id, payload)
        print("The response of ItemsAttachmentsApi->v1_items_id_attachments_attachment_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsAttachmentsApi->v1_items_id_attachments_attachment_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item ID | 
 **attachment_id** | **str**| Attachment ID | 
 **payload** | [**RepoItemAttachmentUpdate**](RepoItemAttachmentUpdate.md)| Attachment Update | 

### Return type

[**RepoItemOut**](RepoItemOut.md)

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

# **v1_items_id_attachments_post**
> RepoItemOut v1_items_id_attachments_post(id, file, name, type=type, primary=primary)

Create Item Attachment

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
    api_instance = homebox_client.ItemsAttachmentsApi(api_client)
    id = 'id_example' # str | Item ID
    file = None # bytearray | File attachment
    name = 'name_example' # str | name of the file including extension
    type = 'type_example' # str | Type of file (optional)
    primary = True # bool | Is this the primary attachment (optional)

    try:
        # Create Item Attachment
        api_response = api_instance.v1_items_id_attachments_post(id, file, name, type=type, primary=primary)
        print("The response of ItemsAttachmentsApi->v1_items_id_attachments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ItemsAttachmentsApi->v1_items_id_attachments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Item ID | 
 **file** | **bytearray**| File attachment | 
 **name** | **str**| name of the file including extension | 
 **type** | **str**| Type of file | [optional] 
 **primary** | **bool**| Is this the primary attachment | [optional] 

### Return type

[**RepoItemOut**](RepoItemOut.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

