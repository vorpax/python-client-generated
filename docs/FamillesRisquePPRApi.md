# swagger_client.FamillesRisquePPRApi

All URIs are relative to *https://georisques.gouv.fr/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recherche_risque**](FamillesRisquePPRApi.md#recherche_risque) | **GET** /v1/ppr/famille_risques | Lister les familles de risques

# **recherche_risque**
> PaginatedResponseFamilleRisques recherche_risque()

Lister les familles de risques

Lexique des familles de risques de la base de données GASPAR (codification issue du standard PPRN / PPRT de la Commission de validation des données pour l'information spatialisée (COVADIS))

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FamillesRisquePPRApi()

try:
    # Lister les familles de risques
    api_response = api_instance.recherche_risque()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FamillesRisquePPRApi->recherche_risque: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PaginatedResponseFamilleRisques**](PaginatedResponseFamilleRisques.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

