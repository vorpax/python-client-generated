# swagger_client.RetraitGonflementDesArgilesApi

All URIs are relative to *https://georisques.gouv.fr/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rechercher_zonage_retrait_gonflement**](RetraitGonflementDesArgilesApi.md#rechercher_zonage_retrait_gonflement) | **GET** /v1/rga | Cette interface est conçue pour diffuser les données sur le retrait / gonflement des sols argileux.

# **rechercher_zonage_retrait_gonflement**
> ZonageArgile rechercher_zonage_retrait_gonflement(latlon=latlon)

Cette interface est conçue pour diffuser les données sur le retrait / gonflement des sols argileux.

Cette interface est conçue pour diffuser les données sur le retrait / gonflement des sols argileux.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RetraitGonflementDesArgilesApi()
latlon = 'latlon_example' # str | Saisir un point sous la forme longitude,latitude. Le séparateur de décimales est toujours un point. La paire de coordonnées est separée par une virgule. Exemple : 0.345234,46.576964 (optional)

try:
    # Cette interface est conçue pour diffuser les données sur le retrait / gonflement des sols argileux.
    api_response = api_instance.rechercher_zonage_retrait_gonflement(latlon=latlon)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RetraitGonflementDesArgilesApi->rechercher_zonage_retrait_gonflement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **latlon** | **str**| Saisir un point sous la forme longitude,latitude. Le séparateur de décimales est toujours un point. La paire de coordonnées est separée par une virgule. Exemple : 0.345234,46.576964 | [optional] 

### Return type

[**ZonageArgile**](ZonageArgile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

