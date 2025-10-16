# homebox_client.ReportingApi

All URIs are relative to *https://demo.homebox.software/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_reporting_bill_of_materials_get**](ReportingApi.md#v1_reporting_bill_of_materials_get) | **GET** /v1/reporting/bill-of-materials | Export Bill of Materials


# **v1_reporting_bill_of_materials_get**
> str v1_reporting_bill_of_materials_get()

Export Bill of Materials

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
    api_instance = homebox_client.ReportingApi(api_client)

    try:
        # Export Bill of Materials
        api_response = api_instance.v1_reporting_bill_of_materials_get()
        print("The response of ReportingApi->v1_reporting_bill_of_materials_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportingApi->v1_reporting_bill_of_materials_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | text/csv |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

