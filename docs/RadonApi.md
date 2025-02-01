# swagger_client.RadonApi

All URIs are relative to *https://georisques.gouv.fr/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recherche_radon1**](RadonApi.md#recherche_radon1) | **GET** /v1/radon | Rechercher les potentiels radon des communes

# **recherche_radon1**
> PaginatedResponseRadon recherche_radon1(code_insee, page=page, page_size=page_size)

Rechercher les potentiels radon des communes

Ce service permet de recherche le potentiel radon d'une ou plusieurs communes. Attention pour les communes de Paris, Lyon et Marseille, seules les informations à  l'arrondissement sont disponibles.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RadonApi()
code_insee = 'code_insee_example' # str | Code(s) INSEE de la commune, si plusieurs codes communes, séparer les codes communes par une virgule, par exemple pour avoir les codes insee 45234 et 45100 : code_insee=45234,45100, le nombre maximum de code est 10
page = 1 # int | Numéro de la page (optional) (default to 1)
page_size = 10 # int | Taille des pages (optional) (default to 10)

try:
    # Rechercher les potentiels radon des communes
    api_response = api_instance.recherche_radon1(code_insee, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RadonApi->recherche_radon1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_insee** | **str**| Code(s) INSEE de la commune, si plusieurs codes communes, séparer les codes communes par une virgule, par exemple pour avoir les codes insee 45234 et 45100 : code_insee&#x3D;45234,45100, le nombre maximum de code est 10 | 
 **page** | **int**| Numéro de la page | [optional] [default to 1]
 **page_size** | **int**| Taille des pages | [optional] [default to 10]

### Return type

[**PaginatedResponseRadon**](PaginatedResponseRadon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

