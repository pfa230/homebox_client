# homebox_client.UserApi

All URIs are relative to *https://demo.homebox.software/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_users_change_password_put**](UserApi.md#v1_users_change_password_put) | **PUT** /v1/users/change-password | Change Password
[**v1_users_register_post**](UserApi.md#v1_users_register_post) | **POST** /v1/users/register | Register New User
[**v1_users_self_delete**](UserApi.md#v1_users_self_delete) | **DELETE** /v1/users/self | Delete Account
[**v1_users_self_get**](UserApi.md#v1_users_self_get) | **GET** /v1/users/self | Get User Self
[**v1_users_self_put**](UserApi.md#v1_users_self_put) | **PUT** /v1/users/self | Update Account


# **v1_users_change_password_put**
> v1_users_change_password_put(payload)

Change Password

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.v1_change_password import V1ChangePassword
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
    api_instance = homebox_client.UserApi(api_client)
    payload = homebox_client.V1ChangePassword() # V1ChangePassword | Password Payload

    try:
        # Change Password
        api_instance.v1_users_change_password_put(payload)
    except Exception as e:
        print("Exception when calling UserApi->v1_users_change_password_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**V1ChangePassword**](V1ChangePassword.md)| Password Payload | 

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

# **v1_users_register_post**
> v1_users_register_post(payload)

Register New User

### Example


```python
import homebox_client
from homebox_client.models.services_user_registration import ServicesUserRegistration
from homebox_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demo.homebox.software/api
# See configuration.py for a list of all supported configuration parameters.
configuration = homebox_client.Configuration(
    host = "https://demo.homebox.software/api"
)


# Enter a context with an instance of the API client
with homebox_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = homebox_client.UserApi(api_client)
    payload = homebox_client.ServicesUserRegistration() # ServicesUserRegistration | User Data

    try:
        # Register New User
        api_instance.v1_users_register_post(payload)
    except Exception as e:
        print("Exception when calling UserApi->v1_users_register_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**ServicesUserRegistration**](ServicesUserRegistration.md)| User Data | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_users_self_delete**
> v1_users_self_delete()

Delete Account

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
    api_instance = homebox_client.UserApi(api_client)

    try:
        # Delete Account
        api_instance.v1_users_self_delete()
    except Exception as e:
        print("Exception when calling UserApi->v1_users_self_delete: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **v1_users_self_get**
> V1UsersSelfGet200Response v1_users_self_get()

Get User Self

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.v1_users_self_get200_response import V1UsersSelfGet200Response
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
    api_instance = homebox_client.UserApi(api_client)

    try:
        # Get User Self
        api_response = api_instance.v1_users_self_get()
        print("The response of UserApi->v1_users_self_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->v1_users_self_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1UsersSelfGet200Response**](V1UsersSelfGet200Response.md)

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

# **v1_users_self_put**
> V1UsersSelfPut200Response v1_users_self_put(payload)

Update Account

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.repo_user_update import RepoUserUpdate
from homebox_client.models.v1_users_self_put200_response import V1UsersSelfPut200Response
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
    api_instance = homebox_client.UserApi(api_client)
    payload = homebox_client.RepoUserUpdate() # RepoUserUpdate | User Data

    try:
        # Update Account
        api_response = api_instance.v1_users_self_put(payload)
        print("The response of UserApi->v1_users_self_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->v1_users_self_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**RepoUserUpdate**](RepoUserUpdate.md)| User Data | 

### Return type

[**V1UsersSelfPut200Response**](V1UsersSelfPut200Response.md)

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

