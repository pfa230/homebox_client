# homebox_client.GroupApi

All URIs are relative to *https://demo.homebox.software/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_groups_get**](GroupApi.md#v1_groups_get) | **GET** /v1/groups | Get Group
[**v1_groups_invitations_post**](GroupApi.md#v1_groups_invitations_post) | **POST** /v1/groups/invitations | Create Group Invitation
[**v1_groups_put**](GroupApi.md#v1_groups_put) | **PUT** /v1/groups | Update Group


# **v1_groups_get**
> RepoGroup v1_groups_get()

Get Group

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.repo_group import RepoGroup
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
    api_instance = homebox_client.GroupApi(api_client)

    try:
        # Get Group
        api_response = api_instance.v1_groups_get()
        print("The response of GroupApi->v1_groups_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->v1_groups_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RepoGroup**](RepoGroup.md)

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

# **v1_groups_invitations_post**
> V1GroupInvitation v1_groups_invitations_post(payload)

Create Group Invitation

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.v1_group_invitation import V1GroupInvitation
from homebox_client.models.v1_group_invitation_create import V1GroupInvitationCreate
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
    api_instance = homebox_client.GroupApi(api_client)
    payload = homebox_client.V1GroupInvitationCreate() # V1GroupInvitationCreate | User Data

    try:
        # Create Group Invitation
        api_response = api_instance.v1_groups_invitations_post(payload)
        print("The response of GroupApi->v1_groups_invitations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->v1_groups_invitations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**V1GroupInvitationCreate**](V1GroupInvitationCreate.md)| User Data | 

### Return type

[**V1GroupInvitation**](V1GroupInvitation.md)

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

# **v1_groups_put**
> RepoGroup v1_groups_put(payload)

Update Group

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.repo_group import RepoGroup
from homebox_client.models.repo_group_update import RepoGroupUpdate
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
    api_instance = homebox_client.GroupApi(api_client)
    payload = homebox_client.RepoGroupUpdate() # RepoGroupUpdate | User Data

    try:
        # Update Group
        api_response = api_instance.v1_groups_put(payload)
        print("The response of GroupApi->v1_groups_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupApi->v1_groups_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payload** | [**RepoGroupUpdate**](RepoGroupUpdate.md)| User Data | 

### Return type

[**RepoGroup**](RepoGroup.md)

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

