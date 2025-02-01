# swagger_client.AZIApi

All URIs are relative to *https://georisques.gouv.fr/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recherche_risques7**](AZIApi.md#recherche_risques7) | **GET** /v1/gaspar/azi | Lister les Atlas de Zones Inondables (AZI) recensés sur le territoire concerné

# **recherche_risques7**
> PaginatedResponseAzi recherche_risques7(rayon=rayon, latlon=latlon, code_insee=code_insee, page=page, page_size=page_size)

Lister les Atlas de Zones Inondables (AZI) recensés sur le territoire concerné

Ce service permet de lister les Atlas de Zones Inondables (AZI) recensés sur le territoire concerné, suivant une emprise spatiale définie, à  savoir un rayon de recherche pour un point défini, une ou plusieurs communes.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AZIApi()
rayon = 1000 # int | Saisir un rayon de recherche exprimé en mètres. Attention la valeur du rayon de recherche est limitée à  10 000 mètres. Par défaut le rayon de recherche est fixé à  1000 mètres. (optional) (default to 1000)
latlon = 'latlon_example' # str | Saisir un point sous la forme longitude,latitude. Le séparateur de décimales est toujours le point. La paire de coordonnées est séparée par une virgule. exemple : 2.29253,48.92572 (optional)
code_insee = 'code_insee_example' # str | Code(s) INSEE de la commune, si plusieurs codes communes, séparer les codes communes par une virgule, par exemple pour avoir les codes insee 45234 et 45100 : code_insee=45234,45100, le nombre maximum de code est 10. Ce type de recherche ne peut pas être combinée avec une recherche au rayon. (optional)
page = 1 # int | Numéro de la page (optional) (default to 1)
page_size = 10 # int | Taille des pages (optional) (default to 10)

try:
    # Lister les Atlas de Zones Inondables (AZI) recensés sur le territoire concerné
    api_response = api_instance.recherche_risques7(rayon=rayon, latlon=latlon, code_insee=code_insee, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AZIApi->recherche_risques7: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rayon** | **int**| Saisir un rayon de recherche exprimé en mètres. Attention la valeur du rayon de recherche est limitée à  10 000 mètres. Par défaut le rayon de recherche est fixé à  1000 mètres. | [optional] [default to 1000]
 **latlon** | **str**| Saisir un point sous la forme longitude,latitude. Le séparateur de décimales est toujours le point. La paire de coordonnées est séparée par une virgule. exemple : 2.29253,48.92572 | [optional] 
 **code_insee** | **str**| Code(s) INSEE de la commune, si plusieurs codes communes, séparer les codes communes par une virgule, par exemple pour avoir les codes insee 45234 et 45100 : code_insee&#x3D;45234,45100, le nombre maximum de code est 10. Ce type de recherche ne peut pas être combinée avec une recherche au rayon. | [optional] 
 **page** | **int**| Numéro de la page | [optional] [default to 1]
 **page_size** | **int**| Taille des pages | [optional] [default to 10]

### Return type

[**PaginatedResponseAzi**](PaginatedResponseAzi.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

