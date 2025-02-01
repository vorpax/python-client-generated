# swagger_client.CavitesApi

All URIs are relative to *https://georisques.gouv.fr/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recherche_risques8**](CavitesApi.md#recherche_risques8) | **GET** /v1/cavites | Cette interface est conçue pour diffuser les données sur les cavités souterraines.

# **recherche_risques8**
> PaginatedResponseCavites recherche_risques8(rayon=rayon, latlon=latlon, code_insee=code_insee, page=page, page_size=page_size, region=region, departement=departement, identifiant=identifiant, type=type)

Cette interface est conçue pour diffuser les données sur les cavités souterraines.

Cette interface est conçue pour diffuser les données sur les cavités souterraines.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CavitesApi()
rayon = 1.2 # float | Saisir un rayon de recherche exprimé en mètres. Attention la valeur du rayon de recherche est limitée à 10 000 mètres. Par defaut le rayon de recherche est fixé a 1000 mètres. (optional)
latlon = 'latlon_example' # str | Saisir un point sous la forme longitude,latitude. Le séparateur de décimales est toujours un point. La paire de coordonnées est separée par une virgule. Exemple : 1.939266,47.861961 (optional)
code_insee = 'code_insee_example' # str | Code(s) INSEE de la commune. Si plusieurs codes communes, séparer les codes communes par une virgule, par exemple pour avoir les codes insee 45234 et 45100 : code_insee=45234,45100. Le nombre maximum de codes est 10. Ce type de recherche ne peut pas être combiné avec une recherche au rayon. (optional)
page = 1 # int | Numéro de la page (optional) (default to 1)
page_size = 10 # int | Taille des pages (optional) (default to 10)
region = 'region_example' # str | Le code de la région recherchée (optional)
departement = 'departement_example' # str | Le code du département recherché (optional)
identifiant = 'identifiant_example' # str | Identifiant de la cavité souterraine (optional)
type = 'type_example' # str | Type de cavité souterraine                                     <br>- Cave <br>- Naturelle <br>- Indéterminé <br>- Ouvrage civil <br>- Puits <br>- Divers <br>- Galerie <br>- Carrière <br>- Indice <br>- Ouvrage militaire <br>- Réseau galeries <br>- Souterrain (optional)

try:
    # Cette interface est conçue pour diffuser les données sur les cavités souterraines.
    api_response = api_instance.recherche_risques8(rayon=rayon, latlon=latlon, code_insee=code_insee, page=page, page_size=page_size, region=region, departement=departement, identifiant=identifiant, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CavitesApi->recherche_risques8: %s\n" % e)
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
 **identifiant** | **str**| Identifiant de la cavité souterraine | [optional] 
 **type** | **str**| Type de cavité souterraine                                     &lt;br&gt;- Cave &lt;br&gt;- Naturelle &lt;br&gt;- Indéterminé &lt;br&gt;- Ouvrage civil &lt;br&gt;- Puits &lt;br&gt;- Divers &lt;br&gt;- Galerie &lt;br&gt;- Carrière &lt;br&gt;- Indice &lt;br&gt;- Ouvrage militaire &lt;br&gt;- Réseau galeries &lt;br&gt;- Souterrain | [optional] 

### Return type

[**PaginatedResponseCavites**](PaginatedResponseCavites.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

