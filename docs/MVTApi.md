# swagger_client.MVTApi

All URIs are relative to *https://georisques.gouv.fr/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recherche_risques1**](MVTApi.md#recherche_risques1) | **GET** /v1/mvt | Cette interface est conçue pour diffuser les données sur le mouvement de terrain.

# **recherche_risques1**
> PaginatedResponseMvt recherche_risques1(rayon=rayon, latlon=latlon, code_insee=code_insee, page=page, page_size=page_size, region=region, departement=departement, identifiant=identifiant, type=type, fiabilite=fiabilite)

Cette interface est conçue pour diffuser les données sur le mouvement de terrain.

Cette interface est conçue pour diffuser les données sur le mouvement de terrain.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MVTApi()
rayon = 1.2 # float | Saisir un rayon de recherche exprimé en mètres. Attention la valeur du rayon de recherche est limitée à 10 000 mètres. Par defaut le rayon de recherche est fixé a 1000 mètres. (optional)
latlon = 'latlon_example' # str | Saisir un point sous la forme longitude,latitude. Le séparateur de décimales est toujours un point. La paire de coordonnées est separée par une virgule. Exemple : 1.939266,47.861961 (optional)
code_insee = 'code_insee_example' # str | Code(s) INSEE de la commune. Si plusieurs codes communes, séparer les codes communes par une virgule, par exemple pour avoir les codes insee 45234 et 45100 : code_insee=45234,45100. Le nombre maximum de codes est 10. Ce type de recherche ne peut pas être combiné avec une recherche au rayon. (optional)
page = 1 # int | Numéro de la page (optional) (default to 1)
page_size = 10 # int | Taille des pages (optional) (default to 10)
region = 'region_example' # str | Le code de la région recherchée (optional)
departement = 'departement_example' # str | Le code du département recherché (optional)
identifiant = 'identifiant_example' # str | Identifiant du mouvement (optional)
type = 'type_example' # str | Type de mouvement de terrain                   <br>- Effondrement / Affaissement <br>- Coulée <br>- Glissement <br>- Erosion de berges <br>- Chute de blocs / Eboulement (optional)
fiabilite = 'fiabilite_example' # str | Type de fiabilité                                    <br>- Faible <br>- Moyen <br>- Fort (optional)

try:
    # Cette interface est conçue pour diffuser les données sur le mouvement de terrain.
    api_response = api_instance.recherche_risques1(rayon=rayon, latlon=latlon, code_insee=code_insee, page=page, page_size=page_size, region=region, departement=departement, identifiant=identifiant, type=type, fiabilite=fiabilite)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MVTApi->recherche_risques1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rayon** | **float**| Saisir un rayon de recherche exprimé en mètres. Attention la valeur du rayon de recherche est limitée à 10 000 mètres. Par defaut le rayon de recherche est fixé a 1000 mètres. | [optional] 
 **latlon** | **str**| Saisir un point sous la forme longitude,latitude. Le séparateur de décimales est toujours un point. La paire de coordonnées est separée par une virgule. Exemple : 1.939266,47.861961 | [optional] 
 **code_insee** | **str**| Code(s) INSEE de la commune. Si plusieurs codes communes, séparer les codes communes par une virgule, par exemple pour avoir les codes insee 45234 et 45100 : code_insee&#x3D;45234,45100. Le nombre maximum de codes est 10. Ce type de recherche ne peut pas être combiné avec une recherche au rayon. | [optional] 
 **page** | **int**| Numéro de la page | [optional] [default to 1]
 **page_size** | **int**| Taille des pages | [optional] [default to 10]
 **region** | **str**| Le code de la région recherchée | [optional] 
 **departement** | **str**| Le code du département recherché | [optional] 
 **identifiant** | **str**| Identifiant du mouvement | [optional] 
 **type** | **str**| Type de mouvement de terrain                   &lt;br&gt;- Effondrement / Affaissement &lt;br&gt;- Coulée &lt;br&gt;- Glissement &lt;br&gt;- Erosion de berges &lt;br&gt;- Chute de blocs / Eboulement | [optional] 
 **fiabilite** | **str**| Type de fiabilité                                    &lt;br&gt;- Faible &lt;br&gt;- Moyen &lt;br&gt;- Fort | [optional] 

### Return type

[**PaginatedResponseMvt**](PaginatedResponseMvt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

