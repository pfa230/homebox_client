# homebox_client.AuthenticationApi

All URIs are relative to *https://demo.homebox.software/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_users_login_post**](AuthenticationApi.md#v1_users_login_post) | **POST** /v1/users/login | User Login
[**v1_users_logout_post**](AuthenticationApi.md#v1_users_logout_post) | **POST** /v1/users/logout | User Logout
[**v1_users_refresh_get**](AuthenticationApi.md#v1_users_refresh_get) | **GET** /v1/users/refresh | User Token Refresh


# **v1_users_login_post**
> V1TokenResponse v1_users_login_post(provider=provider, password=password, stay_logged_in=stay_logged_in, username=username)

User Login

### Example


```python
import homebox_client
from homebox_client.models.v1_token_response import V1TokenResponse
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
    api_instance = homebox_client.AuthenticationApi(api_client)
    provider = 'provider_example' # str | auth provider (optional)
    password = 'password_example' # str |  (optional)
    stay_logged_in = True # bool |  (optional)
    username = 'username_example' # str |  (optional)

    try:
        # User Login
        api_response = api_instance.v1_users_login_post(provider=provider, password=password, stay_logged_in=stay_logged_in, username=username)
        print("The response of AuthenticationApi->v1_users_login_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->v1_users_login_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| auth provider | [optional] 
 **password** | **str**|  | [optional] 
 **stay_logged_in** | **bool**|  | [optional] 
 **username** | **str**|  | [optional] 

### Return type

[**V1TokenResponse**](V1TokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_users_logout_post**
> v1_users_logout_post()

User Logout

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
    api_instance = homebox_client.AuthenticationApi(api_client)

    try:
        # User Logout
        api_instance.v1_users_logout_post()
    except Exception as e:
        print("Exception when calling AuthenticationApi->v1_users_logout_post: %s\n" % e)
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

# **v1_users_refresh_get**
> v1_users_refresh_get()

User Token Refresh

handleAuthRefresh returns a handler that will issue a new token from an existing token.
This does not validate that the user still exists within the database.

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
    api_instance = homebox_client.AuthenticationApi(api_client)

    try:
        # User Token Refresh
        api_instance.v1_users_refresh_get()
    except Exception as e:
        print("Exception when calling AuthenticationApi->v1_users_refresh_get: %s\n" % e)
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

