# swagger_client.PPRApi

All URIs are relative to *https://georisques.gouv.fr/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recherche_ppr**](PPRApi.md#recherche_ppr) | **GET** /v1/ppr | Lister les documents PPR (OBSOLETE)

# **recherche_ppr**
> PaginatedResponsePPR recherche_ppr(rayon=rayon, latlon=latlon, code_insee=code_insee, code_etat=code_etat, code_risque=code_risque, page=page, page_size=page_size)

Lister les documents PPR (OBSOLETE)

Ce service permet de lister les différents documents PPR, suivant une emprise spatiale définie, à  savoir un rayon de recherche pour un point défini, une ou plusieurs communes.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PPRApi()
rayon = 1000 # int | Saisir un rayon de recherche exprimé en mètres. Attention la valeur du rayon de recherche est limitée à  10 000 mètres. Par défaut le rayon de recherche est fixé à  1000 mètres. (optional) (default to 1000)
latlon = 'latlon_example' # str | Saisir un point sous la forme longitude,latitude. Le séparateur de décimales est toujours le point. La paire de coordonnées est séparée par une virgule. exemple : 2.29253,48.92572 (optional)
code_insee = 'code_insee_example' # str | Code(s) INSEE de la commune, si plusieurs codes communes, séparer les codes communes par une virgule, par exemple pour avoir les codes insee 45234 et 45100 : code_insee=45234,45100, le nombre maximum de code est 10. Ce type de recherche ne peut pas être combinée avec une recherche au rayon. (optional)
code_etat = 'code_etat_example' # str | Ce paramètre est optionnel. Code de l'état du document PPR, qui prend pour valeur 01 (Prescrit), 02 (Approuvé), 03 (Abrogé), 04 (Appliqué par anticipation). Si plusieurs états, séparer les codes par une virgule. exemple : 01,02,03,04 (optional)
code_risque = 'code_risque_example' # str | Ce paramètre est optionnel. Code du type de risque du document PPR, qui prend pour valeur pour les principaux :11 (Inondation), 12 (Mouvements de terrain), 13 (Séisme), 14 (Avalanche), 16 (Feu de forêt), 17 (Phénomènes météorologiques), 21 (Risque industriel). Si plusieurs types de risque, séparer les codes par une virgule. exemple : 11,12,13 (optional)
page = 1 # int | Numéro de la page (optional) (default to 1)
page_size = 10 # int | Taille des pages (optional) (default to 10)

try:
    # Lister les documents PPR (OBSOLETE)
    api_response = api_instance.recherche_ppr(rayon=rayon, latlon=latlon, code_insee=code_insee, code_etat=code_etat, code_risque=code_risque, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PPRApi->recherche_ppr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rayon** | **int**| Saisir un rayon de recherche exprimé en mètres. Attention la valeur du rayon de recherche est limitée à  10 000 mètres. Par défaut le rayon de recherche est fixé à  1000 mètres. | [optional] [default to 1000]
 **latlon** | **str**| Saisir un point sous la forme longitude,latitude. Le séparateur de décimales est toujours le point. La paire de coordonnées est séparée par une virgule. exemple : 2.29253,48.92572 | [optional] 
 **code_insee** | **str**| Code(s) INSEE de la commune, si plusieurs codes communes, séparer les codes communes par une virgule, par exemple pour avoir les codes insee 45234 et 45100 : code_insee&#x3D;45234,45100, le nombre maximum de code est 10. Ce type de recherche ne peut pas être combinée avec une recherche au rayon. | [optional] 
 **code_etat** | **str**| Ce paramètre est optionnel. Code de l&#x27;état du document PPR, qui prend pour valeur 01 (Prescrit), 02 (Approuvé), 03 (Abrogé), 04 (Appliqué par anticipation). Si plusieurs états, séparer les codes par une virgule. exemple : 01,02,03,04 | [optional] 
 **code_risque** | **str**| Ce paramètre est optionnel. Code du type de risque du document PPR, qui prend pour valeur pour les principaux :11 (Inondation), 12 (Mouvements de terrain), 13 (Séisme), 14 (Avalanche), 16 (Feu de forêt), 17 (Phénomènes météorologiques), 21 (Risque industriel). Si plusieurs types de risque, séparer les codes par une virgule. exemple : 11,12,13 | [optional] 
 **page** | **int**| Numéro de la page | [optional] [default to 1]
 **page_size** | **int**| Taille des pages | [optional] [default to 10]

### Return type

[**PaginatedResponsePPR**](PaginatedResponsePPR.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

