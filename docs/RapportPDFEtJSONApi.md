# swagger_client.RapportPDFEtJSONApi

All URIs are relative to *https://georisques.gouv.fr/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_rapport_risque**](RapportPDFEtJSONApi.md#generate_rapport_risque) | **GET** /v1/rapport_pdf | Cette interface est conçue pour generer un rapport de risque : adresse ou latlon génèrent un rapport à l&#x27;adresse. code_insee génère un rapport à la commune.
[**generate_rapport_risque_json**](RapportPDFEtJSONApi.md#generate_rapport_risque_json) | **GET** /v1/resultats_rapport_risque | Résultats du rapport des risques près de chez moi

# **generate_rapport_risque**
> list[str] generate_rapport_risque(code_insee=code_insee, latlon=latlon, adresse=adresse)

Cette interface est conçue pour generer un rapport de risque : adresse ou latlon génèrent un rapport à l'adresse. code_insee génère un rapport à la commune.

Cette interface est conçue pour génerer un rapport de risque

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RapportPDFEtJSONApi()
code_insee = 'code_insee_example' # str | Identifiant unique INSEE de la commune (optional)
latlon = 'latlon_example' # str | Saisir un point sous la forme longitude,latitude. Le séparateur de décimales est toujours le point. La paire de coordonnées est séparée par une virgule. exemple : 2.29253,48.92572 (optional)
adresse = 'adresse_example' # str | Adresse postale (optional)

try:
    # Cette interface est conçue pour generer un rapport de risque : adresse ou latlon génèrent un rapport à l'adresse. code_insee génère un rapport à la commune.
    api_response = api_instance.generate_rapport_risque(code_insee=code_insee, latlon=latlon, adresse=adresse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RapportPDFEtJSONApi->generate_rapport_risque: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_insee** | **str**| Identifiant unique INSEE de la commune | [optional] 
 **latlon** | **str**| Saisir un point sous la forme longitude,latitude. Le séparateur de décimales est toujours le point. La paire de coordonnées est séparée par une virgule. exemple : 2.29253,48.92572 | [optional] 
 **adresse** | **str**| Adresse postale | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_rapport_risque_json**
> RapportRisquesJsonDto generate_rapport_risque_json(code_insee=code_insee, latlon=latlon, adresse=adresse)

Résultats du rapport des risques près de chez moi

Cette interface est conçue pour fournir les résultats des rapports des risques près de chez moi.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RapportPDFEtJSONApi()
code_insee = 'code_insee_example' # str | Identifiant unique INSEE de la commune (optional)
latlon = 'latlon_example' # str | Saisir un point sous la forme longitude,latitude. Le séparateur de décimales est toujours le point. La paire de coordonnées est séparée par une virgule. exemple : 2.29253,48.92572 (optional)
adresse = 'adresse_example' # str | Adresse postale (optional)

try:
    # Résultats du rapport des risques près de chez moi
    api_response = api_instance.generate_rapport_risque_json(code_insee=code_insee, latlon=latlon, adresse=adresse)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RapportPDFEtJSONApi->generate_rapport_risque_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_insee** | **str**| Identifiant unique INSEE de la commune | [optional] 
 **latlon** | **str**| Saisir un point sous la forme longitude,latitude. Le séparateur de décimales est toujours le point. La paire de coordonnées est séparée par une virgule. exemple : 2.29253,48.92572 | [optional] 
 **adresse** | **str**| Adresse postale | [optional] 

### Return type

[**RapportRisquesJsonDto**](RapportRisquesJsonDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

