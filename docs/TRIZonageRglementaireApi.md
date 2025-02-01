# swagger_client.TRIZonageRglementaireApi

All URIs are relative to *https://georisques.gouv.fr/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recherche_tri_zonage**](TRIZonageRglementaireApi.md#recherche_tri_zonage) | **GET** /v1/tri_zonage | Lister les Territoires à  Risques importants d&#x27;Inondation (TRI) recensés sur l&#x27;adresse concernée

# **recherche_tri_zonage**
> NoPaginatedResponseTriZonageDto recherche_tri_zonage(latlon, code=code)

Lister les Territoires à  Risques importants d'Inondation (TRI) recensés sur l'adresse concernée

Ce service permet de lister les Territoires à  Risques importants d'Inondation (TRI) recensés sur l'adresse concernée, suivant une latitude et une longitude.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TRIZonageRglementaireApi()
latlon = 'latlon_example' # str | Saisir un point sous la forme longitude,latitude. Le séparateur de décimales est toujours le point. La paire de coordonnées est séparée par une virgule. exemple : 2.29253,48.92572
code = 'code_example' # str | Code risque TRI - possibilité de mettre une liste entre virgules (optional)

try:
    # Lister les Territoires à  Risques importants d'Inondation (TRI) recensés sur l'adresse concernée
    api_response = api_instance.recherche_tri_zonage(latlon, code=code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TRIZonageRglementaireApi->recherche_tri_zonage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **latlon** | **str**| Saisir un point sous la forme longitude,latitude. Le séparateur de décimales est toujours le point. La paire de coordonnées est séparée par une virgule. exemple : 2.29253,48.92572 | 
 **code** | **str**| Code risque TRI - possibilité de mettre une liste entre virgules | [optional] 

### Return type

[**NoPaginatedResponseTriZonageDto**](NoPaginatedResponseTriZonageDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

