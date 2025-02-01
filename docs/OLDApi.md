# swagger_client.OLDApi

All URIs are relative to *https://georisques.gouv.fr/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recherche_risques**](OLDApi.md#recherche_risques) | **GET** /v1/old | Liste des Obligations Légales de Débroussaillement

# **recherche_risques**
> list[OldModel] recherche_risques(latlon=latlon, code_insee=code_insee)

Liste des Obligations Légales de Débroussaillement

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OLDApi()
latlon = 'latlon_example' # str | Saisir un point sous la forme longitude,latitude. Le séparateur de décimales est toujours un point. La paire de coordonnées est separée par une virgule. Exemple : 4.254,43.8 (optional)
code_insee = 'code_insee_example' # str | Code INSEE de la commune (optional)

try:
    # Liste des Obligations Légales de Débroussaillement
    api_response = api_instance.recherche_risques(latlon=latlon, code_insee=code_insee)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OLDApi->recherche_risques: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **latlon** | **str**| Saisir un point sous la forme longitude,latitude. Le séparateur de décimales est toujours un point. La paire de coordonnées est separée par une virgule. Exemple : 4.254,43.8 | [optional] 
 **code_insee** | **str**| Code INSEE de la commune | [optional] 

### Return type

[**list[OldModel]**](OldModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

