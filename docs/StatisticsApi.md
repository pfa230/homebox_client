# homebox_client.StatisticsApi

All URIs are relative to *https://demo.homebox.software/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_groups_statistics_get**](StatisticsApi.md#v1_groups_statistics_get) | **GET** /v1/groups/statistics | Get Group Statistics
[**v1_groups_statistics_labels_get**](StatisticsApi.md#v1_groups_statistics_labels_get) | **GET** /v1/groups/statistics/labels | Get Label Statistics
[**v1_groups_statistics_locations_get**](StatisticsApi.md#v1_groups_statistics_locations_get) | **GET** /v1/groups/statistics/locations | Get Location Statistics
[**v1_groups_statistics_purchase_price_get**](StatisticsApi.md#v1_groups_statistics_purchase_price_get) | **GET** /v1/groups/statistics/purchase-price | Get Purchase Price Statistics


# **v1_groups_statistics_get**
> RepoGroupStatistics v1_groups_statistics_get()

Get Group Statistics

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.repo_group_statistics import RepoGroupStatistics
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
    api_instance = homebox_client.StatisticsApi(api_client)

    try:
        # Get Group Statistics
        api_response = api_instance.v1_groups_statistics_get()
        print("The response of StatisticsApi->v1_groups_statistics_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatisticsApi->v1_groups_statistics_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RepoGroupStatistics**](RepoGroupStatistics.md)

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

# **v1_groups_statistics_labels_get**
> List[RepoTotalsByOrganizer] v1_groups_statistics_labels_get()

Get Label Statistics

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.repo_totals_by_organizer import RepoTotalsByOrganizer
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
    api_instance = homebox_client.StatisticsApi(api_client)

    try:
        # Get Label Statistics
        api_response = api_instance.v1_groups_statistics_labels_get()
        print("The response of StatisticsApi->v1_groups_statistics_labels_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatisticsApi->v1_groups_statistics_labels_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[RepoTotalsByOrganizer]**](RepoTotalsByOrganizer.md)

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

# **v1_groups_statistics_locations_get**
> List[RepoTotalsByOrganizer] v1_groups_statistics_locations_get()

Get Location Statistics

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.repo_totals_by_organizer import RepoTotalsByOrganizer
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
    api_instance = homebox_client.StatisticsApi(api_client)

    try:
        # Get Location Statistics
        api_response = api_instance.v1_groups_statistics_locations_get()
        print("The response of StatisticsApi->v1_groups_statistics_locations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatisticsApi->v1_groups_statistics_locations_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[RepoTotalsByOrganizer]**](RepoTotalsByOrganizer.md)

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

# **v1_groups_statistics_purchase_price_get**
> RepoValueOverTime v1_groups_statistics_purchase_price_get(start=start, end=end)

Get Purchase Price Statistics

### Example

* Api Key Authentication (Bearer):

```python
import homebox_client
from homebox_client.models.repo_value_over_time import RepoValueOverTime
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
    api_instance = homebox_client.StatisticsApi(api_client)
    start = 'start_example' # str | start date (optional)
    end = 'end_example' # str | end date (optional)

    try:
        # Get Purchase Price Statistics
        api_response = api_instance.v1_groups_statistics_purchase_price_get(start=start, end=end)
        print("The response of StatisticsApi->v1_groups_statistics_purchase_price_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatisticsApi->v1_groups_statistics_purchase_price_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **str**| start date | [optional] 
 **end** | **str**| end date | [optional] 

### Return type

[**RepoValueOverTime**](RepoValueOverTime.md)

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

