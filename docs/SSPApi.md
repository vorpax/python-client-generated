# swagger_client.SSPApi

All URIs are relative to *https://georisques.gouv.fr/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recherche_casias**](SSPApi.md#recherche_casias) | **GET** /v1/ssp/casias | Lister les Cartes des Anciens Sites Industriels et Activités de Services
[**recherche_ex_basol**](SSPApi.md#recherche_ex_basol) | **GET** /v1/ssp/instructions | Lister les informations de l&#x27;administration concernant une pollution suspectée ou avérée (ex-BASOL)
[**recherche_globale**](SSPApi.md#recherche_globale) | **GET** /v1/ssp | Lister les données CASIAS, ex-BASOL, SIS et SUP.
[**recherche_sis**](SSPApi.md#recherche_sis) | **GET** /v1/ssp/conclusions_sis | Lister les Secteurs d&#x27;Information sur les Sols
[**recherche_sup**](SSPApi.md#recherche_sup) | **GET** /v1/ssp/conclusions_sup | Lister les Servitudes d&#x27;Utilité Publique

# **recherche_casias**
> PaginatedResponseCasiasDto recherche_casias(rayon=rayon, latlon=latlon, code_insee=code_insee, page=page, page_size=page_size, code_region=code_region, code_departement=code_departement, date_maj=date_maj)

Lister les Cartes des Anciens Sites Industriels et Activités de Services

Ce service permet de lister les différents CASIAS, suivant une emprise spatiale définie, à savoir un rayon de recherche pour un point défini, une ou plusieurs communes, une région ou un département.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SSPApi()
rayon = 1000 # int | Saisir un rayon de recherche exprimé en mètres. Attention la valeur du rayon de recherche est limitée à  10 000 mètres. Par défaut le rayon de recherche est fixé à  1000 mètres. (optional) (default to 1000)
latlon = 'latlon_example' # str | Saisir un point sous la forme longitude,latitude. Le séparateur de décimales est toujours le point. La paire de coordonnées est séparée par une virgule. exemple : 2.29253,48.92572 (optional)
code_insee = 'code_insee_example' # str | Code(s) INSEE de la commune, si plusieurs codes communes, séparer les codes communes par une virgule, par exemple pour avoir les codes insee 45234 et 45100 : code_insee=45234,45100, le nombre maximum de code est 10. Ce type de recherche ne peut pas être combinée avec une recherche au rayon, à la région ou au département. (optional)
page = 1 # int | Numéro de la page (optional) (default to 1)
page_size = 10 # int | Taille des pages (optional) (default to 10)
code_region = 'code_region_example' # str | Le code de la région recherchée (optional)
code_departement = 'code_departement_example' # str | Le code du département recherché (optional)
date_maj = 'date_maj_example' # str | Date de mise à jour des données. La date est au format \"AAAA-MM-JJ\". L'API renvoie toutes les données dont la date de modification est supérieure ou égale à date_maj. (optional)

try:
    # Lister les Cartes des Anciens Sites Industriels et Activités de Services
    api_response = api_instance.recherche_casias(rayon=rayon, latlon=latlon, code_insee=code_insee, page=page, page_size=page_size, code_region=code_region, code_departement=code_departement, date_maj=date_maj)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SSPApi->recherche_casias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rayon** | **int**| Saisir un rayon de recherche exprimé en mètres. Attention la valeur du rayon de recherche est limitée à  10 000 mètres. Par défaut le rayon de recherche est fixé à  1000 mètres. | [optional] [default to 1000]
 **latlon** | **str**| Saisir un point sous la forme longitude,latitude. Le séparateur de décimales est toujours le point. La paire de coordonnées est séparée par une virgule. exemple : 2.29253,48.92572 | [optional] 
 **code_insee** | **str**| Code(s) INSEE de la commune, si plusieurs codes communes, séparer les codes communes par une virgule, par exemple pour avoir les codes insee 45234 et 45100 : code_insee&#x3D;45234,45100, le nombre maximum de code est 10. Ce type de recherche ne peut pas être combinée avec une recherche au rayon, à la région ou au département. | [optional] 
 **page** | **int**| Numéro de la page | [optional] [default to 1]
 **page_size** | **int**| Taille des pages | [optional] [default to 10]
 **code_region** | **str**| Le code de la région recherchée | [optional] 
 **code_departement** | **str**| Le code du département recherché | [optional] 
 **date_maj** | **str**| Date de mise à jour des données. La date est au format \&quot;AAAA-MM-JJ\&quot;. L&#x27;API renvoie toutes les données dont la date de modification est supérieure ou égale à date_maj. | [optional] 

### Return type

[**PaginatedResponseCasiasDto**](PaginatedResponseCasiasDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recherche_ex_basol**
> PaginatedResponseExBasolDto recherche_ex_basol(rayon=rayon, latlon=latlon, code_insee=code_insee, page=page, page_size=page_size, code_region=code_region, code_departement=code_departement, date_maj=date_maj)

Lister les informations de l'administration concernant une pollution suspectée ou avérée (ex-BASOL)

Ce service permet de lister les différents ex-BASOL, suivant une emprise spatiale définie, à savoir un rayon de recherche pour un point défini, une ou plusieurs communes, une région ou un département.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SSPApi()
rayon = 1000 # int | Saisir un rayon de recherche exprimé en mètres. Attention la valeur du rayon de recherche est limitée à  10 000 mètres. Par défaut le rayon de recherche est fixé à  1000 mètres. (optional) (default to 1000)
latlon = 'latlon_example' # str | Saisir un point sous la forme longitude,latitude. Le séparateur de décimales est toujours le point. La paire de coordonnées est séparée par une virgule. exemple : 2.29253,48.92572 (optional)
code_insee = 'code_insee_example' # str | Code(s) INSEE de la commune, si plusieurs codes communes, séparer les codes communes par une virgule, par exemple pour avoir les codes insee 45234 et 45100 : code_insee=45234,45100, le nombre maximum de code est 10. Ce type de recherche ne peut pas être combinée avec une recherche au rayon, à la région ou au département. (optional)
page = 1 # int | Numéro de la page (optional) (default to 1)
page_size = 10 # int | Taille des pages (optional) (default to 10)
code_region = 'code_region_example' # str | Le code de la région recherchée (optional)
code_departement = 'code_departement_example' # str | Le code du département recherché (optional)
date_maj = 'date_maj_example' # str | Date de mise à jour des données. La date est au format \"AAAA-MM-JJ\". L'API renvoie toutes les données dont la date de modification est supérieure ou égale à date_maj. (optional)

try:
    # Lister les informations de l'administration concernant une pollution suspectée ou avérée (ex-BASOL)
    api_response = api_instance.recherche_ex_basol(rayon=rayon, latlon=latlon, code_insee=code_insee, page=page, page_size=page_size, code_region=code_region, code_departement=code_departement, date_maj=date_maj)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SSPApi->recherche_ex_basol: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rayon** | **int**| Saisir un rayon de recherche exprimé en mètres. Attention la valeur du rayon de recherche est limitée à  10 000 mètres. Par défaut le rayon de recherche est fixé à  1000 mètres. | [optional] [default to 1000]
 **latlon** | **str**| Saisir un point sous la forme longitude,latitude. Le séparateur de décimales est toujours le point. La paire de coordonnées est séparée par une virgule. exemple : 2.29253,48.92572 | [optional] 
 **code_insee** | **str**| Code(s) INSEE de la commune, si plusieurs codes communes, séparer les codes communes par une virgule, par exemple pour avoir les codes insee 45234 et 45100 : code_insee&#x3D;45234,45100, le nombre maximum de code est 10. Ce type de recherche ne peut pas être combinée avec une recherche au rayon, à la région ou au département. | [optional] 
 **page** | **int**| Numéro de la page | [optional] [default to 1]
 **page_size** | **int**| Taille des pages | [optional] [default to 10]
 **code_region** | **str**| Le code de la région recherchée | [optional] 
 **code_departement** | **str**| Le code du département recherché | [optional] 
 **date_maj** | **str**| Date de mise à jour des données. La date est au format \&quot;AAAA-MM-JJ\&quot;. L&#x27;API renvoie toutes les données dont la date de modification est supérieure ou égale à date_maj. | [optional] 

### Return type

[**PaginatedResponseExBasolDto**](PaginatedResponseExBasolDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recherche_globale**
> Ssp recherche_globale(rayon=rayon, latlon=latlon, code_insee=code_insee, page=page, page_size=page_size, code_region=code_region, code_departement=code_departement, date_maj=date_maj)

Lister les données CASIAS, ex-BASOL, SIS et SUP.

Ce service permet de lister les différents CASIAS, ex-BASOL, SIS et SUP, suivant une emprise spatiale définie, à  savoir un rayon de recherche pour un point défini, une ou plusieurs communes, une région ou un département.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SSPApi()
rayon = 1000 # int | Saisir un rayon de recherche exprimé en mètres. Attention la valeur du rayon de recherche est limitée à  10 000 mètres. Par défaut le rayon de recherche est fixé à  1000 mètres. (optional) (default to 1000)
latlon = 'latlon_example' # str | Saisir un point sous la forme longitude,latitude. Le séparateur de décimales est toujours le point. La paire de coordonnées est séparée par une virgule. exemple : 2.29253,48.92572 (optional)
code_insee = 'code_insee_example' # str | Code(s) INSEE de la commune, si plusieurs codes communes, séparer les codes communes par une virgule, par exemple pour avoir les codes insee 45234 et 45100 : code_insee=45234,45100, le nombre maximum de code est 10. Ce type de recherche ne peut pas être combinée avec une recherche au rayon, à la région ou au département. (optional)
page = 1 # int | Numéro de la page (optional) (default to 1)
page_size = 10 # int | Taille des pages (optional) (default to 10)
code_region = 'code_region_example' # str | Le code de la région recherchée (optional)
code_departement = 'code_departement_example' # str | Le code du département recherché (optional)
date_maj = 'date_maj_example' # str | Date de mise à jour des données. La date est au format \"AAAA-MM-JJ\". L'API renvoie toutes les données dont la date de modification est supérieure ou égale à date_maj. (optional)

try:
    # Lister les données CASIAS, ex-BASOL, SIS et SUP.
    api_response = api_instance.recherche_globale(rayon=rayon, latlon=latlon, code_insee=code_insee, page=page, page_size=page_size, code_region=code_region, code_departement=code_departement, date_maj=date_maj)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SSPApi->recherche_globale: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rayon** | **int**| Saisir un rayon de recherche exprimé en mètres. Attention la valeur du rayon de recherche est limitée à  10 000 mètres. Par défaut le rayon de recherche est fixé à  1000 mètres. | [optional] [default to 1000]
 **latlon** | **str**| Saisir un point sous la forme longitude,latitude. Le séparateur de décimales est toujours le point. La paire de coordonnées est séparée par une virgule. exemple : 2.29253,48.92572 | [optional] 
 **code_insee** | **str**| Code(s) INSEE de la commune, si plusieurs codes communes, séparer les codes communes par une virgule, par exemple pour avoir les codes insee 45234 et 45100 : code_insee&#x3D;45234,45100, le nombre maximum de code est 10. Ce type de recherche ne peut pas être combinée avec une recherche au rayon, à la région ou au département. | [optional] 
 **page** | **int**| Numéro de la page | [optional] [default to 1]
 **page_size** | **int**| Taille des pages | [optional] [default to 10]
 **code_region** | **str**| Le code de la région recherchée | [optional] 
 **code_departement** | **str**| Le code du département recherché | [optional] 
 **date_maj** | **str**| Date de mise à jour des données. La date est au format \&quot;AAAA-MM-JJ\&quot;. L&#x27;API renvoie toutes les données dont la date de modification est supérieure ou égale à date_maj. | [optional] 

### Return type

[**Ssp**](Ssp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recherche_sis**
> PaginatedResponseSisDto recherche_sis(rayon=rayon, latlon=latlon, code_insee=code_insee, page=page, page_size=page_size, code_region=code_region, code_departement=code_departement, date_maj=date_maj)

Lister les Secteurs d'Information sur les Sols

Ce service permet de lister les différents SIS, suivant une emprise spatiale définie, à savoir un rayon de recherche pour un point défini, une ou plusieurs communes, une région ou un département.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SSPApi()
rayon = 1000 # int | Saisir un rayon de recherche exprimé en mètres. Attention la valeur du rayon de recherche est limitée à  10 000 mètres. Par défaut le rayon de recherche est fixé à  1000 mètres. (optional) (default to 1000)
latlon = 'latlon_example' # str | Saisir un point sous la forme longitude,latitude. Le séparateur de décimales est toujours le point. La paire de coordonnées est séparée par une virgule. exemple : 2.29253,48.92572 (optional)
code_insee = 'code_insee_example' # str | Code(s) INSEE de la commune, si plusieurs codes communes, séparer les codes communes par une virgule, par exemple pour avoir les codes insee 45234 et 45100 : code_insee=45234,45100, le nombre maximum de code est 10. Ce type de recherche ne peut pas être combinée avec une recherche au rayon, à la région ou au département. (optional)
page = 1 # int | Numéro de la page (optional) (default to 1)
page_size = 10 # int | Taille des pages (optional) (default to 10)
code_region = 'code_region_example' # str | Le code de la région recherchée (optional)
code_departement = 'code_departement_example' # str | Le code du département recherché (optional)
date_maj = 'date_maj_example' # str | Date de mise à jour des données. La date est au format \"AAAA-MM-JJ\". L'API renvoie toutes les données dont la date de modification est supérieure ou égale à date_maj. (optional)

try:
    # Lister les Secteurs d'Information sur les Sols
    api_response = api_instance.recherche_sis(rayon=rayon, latlon=latlon, code_insee=code_insee, page=page, page_size=page_size, code_region=code_region, code_departement=code_departement, date_maj=date_maj)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SSPApi->recherche_sis: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rayon** | **int**| Saisir un rayon de recherche exprimé en mètres. Attention la valeur du rayon de recherche est limitée à  10 000 mètres. Par défaut le rayon de recherche est fixé à  1000 mètres. | [optional] [default to 1000]
 **latlon** | **str**| Saisir un point sous la forme longitude,latitude. Le séparateur de décimales est toujours le point. La paire de coordonnées est séparée par une virgule. exemple : 2.29253,48.92572 | [optional] 
 **code_insee** | **str**| Code(s) INSEE de la commune, si plusieurs codes communes, séparer les codes communes par une virgule, par exemple pour avoir les codes insee 45234 et 45100 : code_insee&#x3D;45234,45100, le nombre maximum de code est 10. Ce type de recherche ne peut pas être combinée avec une recherche au rayon, à la région ou au département. | [optional] 
 **page** | **int**| Numéro de la page | [optional] [default to 1]
 **page_size** | **int**| Taille des pages | [optional] [default to 10]
 **code_region** | **str**| Le code de la région recherchée | [optional] 
 **code_departement** | **str**| Le code du département recherché | [optional] 
 **date_maj** | **str**| Date de mise à jour des données. La date est au format \&quot;AAAA-MM-JJ\&quot;. L&#x27;API renvoie toutes les données dont la date de modification est supérieure ou égale à date_maj. | [optional] 

### Return type

[**PaginatedResponseSisDto**](PaginatedResponseSisDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recherche_sup**
> PaginatedResponseSupDto recherche_sup(rayon=rayon, latlon=latlon, code_insee=code_insee, page=page, page_size=page_size, code_region=code_region, code_departement=code_departement, date_maj=date_maj)

Lister les Servitudes d'Utilité Publique

Ce service permet de lister les différents SUP, suivant une emprise spatiale définie, à savoir un rayon de recherche pour un point défini, une ou plusieurs communes, une région ou un département.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SSPApi()
rayon = 1000 # int | Saisir un rayon de recherche exprimé en mètres. Attention la valeur du rayon de recherche est limitée à  10 000 mètres. Par défaut le rayon de recherche est fixé à  1000 mètres. (optional) (default to 1000)
latlon = 'latlon_example' # str | Saisir un point sous la forme longitude,latitude. Le séparateur de décimales est toujours le point. La paire de coordonnées est séparée par une virgule. exemple : 2.29253,48.92572 (optional)
code_insee = 'code_insee_example' # str | Code(s) INSEE de la commune, si plusieurs codes communes, séparer les codes communes par une virgule, par exemple pour avoir les codes insee 45234 et 45100 : code_insee=45234,45100, le nombre maximum de code est 10. Ce type de recherche ne peut pas être combinée avec une recherche au rayon, à la région ou au département. (optional)
page = 1 # int | Numéro de la page (optional) (default to 1)
page_size = 10 # int | Taille des pages (optional) (default to 10)
code_region = 'code_region_example' # str | Le code de la région recherchée (optional)
code_departement = 'code_departement_example' # str | Le code du département recherché (optional)
date_maj = 'date_maj_example' # str | Date de mise à jour des données. La date est au format \"AAAA-MM-JJ\". L'API renvoie toutes les données dont la date de modification est supérieure ou égale à date_maj. (optional)

try:
    # Lister les Servitudes d'Utilité Publique
    api_response = api_instance.recherche_sup(rayon=rayon, latlon=latlon, code_insee=code_insee, page=page, page_size=page_size, code_region=code_region, code_departement=code_departement, date_maj=date_maj)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SSPApi->recherche_sup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rayon** | **int**| Saisir un rayon de recherche exprimé en mètres. Attention la valeur du rayon de recherche est limitée à  10 000 mètres. Par défaut le rayon de recherche est fixé à  1000 mètres. | [optional] [default to 1000]
 **latlon** | **str**| Saisir un point sous la forme longitude,latitude. Le séparateur de décimales est toujours le point. La paire de coordonnées est séparée par une virgule. exemple : 2.29253,48.92572 | [optional] 
 **code_insee** | **str**| Code(s) INSEE de la commune, si plusieurs codes communes, séparer les codes communes par une virgule, par exemple pour avoir les codes insee 45234 et 45100 : code_insee&#x3D;45234,45100, le nombre maximum de code est 10. Ce type de recherche ne peut pas être combinée avec une recherche au rayon, à la région ou au département. | [optional] 
 **page** | **int**| Numéro de la page | [optional] [default to 1]
 **page_size** | **int**| Taille des pages | [optional] [default to 10]
 **code_region** | **str**| Le code de la région recherchée | [optional] 
 **code_departement** | **str**| Le code du département recherché | [optional] 
 **date_maj** | **str**| Date de mise à jour des données. La date est au format \&quot;AAAA-MM-JJ\&quot;. L&#x27;API renvoie toutes les données dont la date de modification est supérieure ou égale à date_maj. | [optional] 

### Return type

[**PaginatedResponseSupDto**](PaginatedResponseSupDto.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

