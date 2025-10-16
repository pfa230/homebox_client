# homebox_client.BaseApi

All URIs are relative to *https://demo.homebox.software/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_currency_get**](BaseApi.md#v1_currency_get) | **GET** /v1/currency | Currency
[**v1_status_get**](BaseApi.md#v1_status_get) | **GET** /v1/status | Application Info


# **v1_currency_get**
> CurrenciesCurrency v1_currency_get()

Currency

### Example


```python
import homebox_client
from homebox_client.models.currencies_currency import CurrenciesCurrency
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
    api_instance = homebox_client.BaseApi(api_client)

    try:
        # Currency
        api_response = api_instance.v1_currency_get()
        print("The response of BaseApi->v1_currency_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BaseApi->v1_currency_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CurrenciesCurrency**](CurrenciesCurrency.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_status_get**
> V1APISummary v1_status_get()

Application Info

### Example


```python
import homebox_client
from homebox_client.models.v1_api_summary import V1APISummary
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
    api_instance = homebox_client.BaseApi(api_client)

    try:
        # Application Info
        api_response = api_instance.v1_status_get()
        print("The response of BaseApi->v1_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BaseApi->v1_status_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**V1APISummary**](V1APISummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

