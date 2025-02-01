# swagger_client.InstallationsClassesApi

All URIs are relative to *https://georisques.gouv.fr/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rechercher_aiots_par_geolocalisation**](InstallationsClassesApi.md#rechercher_aiots_par_geolocalisation) | **GET** /v1/installations_classees | Cette interface est conçue pour diffuser les données installations classées de Gun Env à destination de Géorisques.
[**rechercher_aiots_par_geolocalisation1**](InstallationsClassesApi.md#rechercher_aiots_par_geolocalisation1) | **GET** /v1/csv/installations_classees | Cette interface est conçue pour diffuser les données installations classées de Gun Env à destination de Géorisques.

# **rechercher_aiots_par_geolocalisation**
> PaginatedResponseInstallationClassee rechercher_aiots_par_geolocalisation(code_insee=code_insee, siret=siret, code_aiot=code_aiot, latlon=latlon, rayon=rayon, page=page, page_size=page_size, debut_inspection=debut_inspection, fin_inspection=fin_inspection, raison_sociale=raison_sociale, region=region, departement=departement, activite=activite, nomenclature=nomenclature, regime=regime, statut_seveso=statut_seveso, priorite_nationale=priorite_nationale, ied=ied, date_maj=date_maj)

Cette interface est conçue pour diffuser les données installations classées de Gun Env à destination de Géorisques.

Cette interface est conçue pour diffuser les données installations classées de Gun Env à destination de Géorisques.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InstallationsClassesApi()
code_insee = ['code_insee_example'] # list[str] | Code(s) INSEE de la commune. Si plusieurs codes communes, séparer les codes communes par une virgule, par exemple pour avoir les codes insee 45234 et 45100 : code_insee=45234,45100. Le nombre maximum de codes est 10. Ce type de recherche ne peut pas être combiné avec une recherche au rayon. (optional)
siret = ['siret_example'] # list[str] | Code(s) siret de l'installation classée.Si plusieurs codes, les séparer par une virgule, par exemple  : siret=48335930300011,35392644700130. (optional)
code_aiot = ['code_aiot_example'] # list[str] | Code(s) de(s) (l')installation(s) classée(s) à 10 chiffres.Si plusieurs codes, les séparer par une virgule,par exemple  : codeAIOT=0005402775,0005602790. (optional)
latlon = 'latlon_example' # str | Saisir un point sous la forme longitude,latitude. Le séparateur de décimales est toujours un point. La paire de coordonnées est separée par une virgule. Exemple : 2.29253,48.92572 (optional)
rayon = 1.2 # float | Saisir un rayon de recherche exprimé en mètres. Attention la valeur du rayon de recherche est limitée à 10 000 mètres. Par defaut le rayon de recherche est fixé a 1000 mètres. (optional)
page = 1 # int | Numéro de la page (optional) (default to 1)
page_size = 10 # int | Taille des pages (optional) (default to 10)
debut_inspection = 'debut_inspection_example' # str | Date d'inspection minimum à recherchée. La date est au format \"AAAA-MM-JJ\". (optional)
fin_inspection = 'fin_inspection_example' # str | Date d'inspection maximum à recherchée. La date est au format \"AAAA-MM-JJ\". (optional)
raison_sociale = 'raison_sociale_example' # str | Tout ou partie d'un nom d'établissement recherché et insensible à la casse (optional)
region = 'region_example' # str | Le code de la région recherchée (optional)
departement = 'departement_example' # str | Le code du département recherché (optional)
activite = 'activite_example' # str | Le code de l'activité principale de l'établissement, tel que défini dans la nomenclature NAF v2 (ex. 01, 02, etc.) : <br>https://www.insee.fr/fr/information/2406147 (optional)
nomenclature = ['nomenclature_example'] # list[str] | La liste des codes de nomenclatures d'installations classées. <br>La liste des valeurs est séparée par une virgule (ex. 1455, 1531, etc.) <br> <br>La liste des nomenclatures est disponible à l'adresse suivante : <br>https://aida.ineris.fr/liste_documents/1/18023/1 (optional)
regime = 'regime_example' # str | Le code du régime de l'établissement : <br>- A : Autorisation <br>- E : Enregistrement <br>- AUTRE : Autre régime  (optional)
statut_seveso = 'statut_seveso_example' # str | Le code du statut SEVESO de l'établissement : <br>- 1 : Seveso seuil haut <br>- 2 : Seveso seuil bas <br>- 3 : Non Seveso (optional)
priorite_nationale = true # bool | Etablissement « priorité nationale » - true/false (optional)
ied = true # bool | Etablissement « IED-MTD » - true/false (optional)
date_maj = 'date_maj_example' # str | Date de modification des données. La date est au format \"AAAA-MM-JJ\". L'API renvoie tous les établissements dont la date de modification est supérieure ou égale à dateMaj. (optional)

try:
    # Cette interface est conçue pour diffuser les données installations classées de Gun Env à destination de Géorisques.
    api_response = api_instance.rechercher_aiots_par_geolocalisation(code_insee=code_insee, siret=siret, code_aiot=code_aiot, latlon=latlon, rayon=rayon, page=page, page_size=page_size, debut_inspection=debut_inspection, fin_inspection=fin_inspection, raison_sociale=raison_sociale, region=region, departement=departement, activite=activite, nomenclature=nomenclature, regime=regime, statut_seveso=statut_seveso, priorite_nationale=priorite_nationale, ied=ied, date_maj=date_maj)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstallationsClassesApi->rechercher_aiots_par_geolocalisation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_insee** | [**list[str]**](str.md)| Code(s) INSEE de la commune. Si plusieurs codes communes, séparer les codes communes par une virgule, par exemple pour avoir les codes insee 45234 et 45100 : code_insee&#x3D;45234,45100. Le nombre maximum de codes est 10. Ce type de recherche ne peut pas être combiné avec une recherche au rayon. | [optional] 
 **siret** | [**list[str]**](str.md)| Code(s) siret de l&#x27;installation classée.Si plusieurs codes, les séparer par une virgule, par exemple  : siret&#x3D;48335930300011,35392644700130. | [optional] 
 **code_aiot** | [**list[str]**](str.md)| Code(s) de(s) (l&#x27;)installation(s) classée(s) à 10 chiffres.Si plusieurs codes, les séparer par une virgule,par exemple  : codeAIOT&#x3D;0005402775,0005602790. | [optional] 
 **latlon** | **str**| Saisir un point sous la forme longitude,latitude. Le séparateur de décimales est toujours un point. La paire de coordonnées est separée par une virgule. Exemple : 2.29253,48.92572 | [optional] 
 **rayon** | **float**| Saisir un rayon de recherche exprimé en mètres. Attention la valeur du rayon de recherche est limitée à 10 000 mètres. Par defaut le rayon de recherche est fixé a 1000 mètres. | [optional] 
 **page** | **int**| Numéro de la page | [optional] [default to 1]
 **page_size** | **int**| Taille des pages | [optional] [default to 10]
 **debut_inspection** | **str**| Date d&#x27;inspection minimum à recherchée. La date est au format \&quot;AAAA-MM-JJ\&quot;. | [optional] 
 **fin_inspection** | **str**| Date d&#x27;inspection maximum à recherchée. La date est au format \&quot;AAAA-MM-JJ\&quot;. | [optional] 
 **raison_sociale** | **str**| Tout ou partie d&#x27;un nom d&#x27;établissement recherché et insensible à la casse | [optional] 
 **region** | **str**| Le code de la région recherchée | [optional] 
 **departement** | **str**| Le code du département recherché | [optional] 
 **activite** | **str**| Le code de l&#x27;activité principale de l&#x27;établissement, tel que défini dans la nomenclature NAF v2 (ex. 01, 02, etc.) : &lt;br&gt;https://www.insee.fr/fr/information/2406147 | [optional] 
 **nomenclature** | [**list[str]**](str.md)| La liste des codes de nomenclatures d&#x27;installations classées. &lt;br&gt;La liste des valeurs est séparée par une virgule (ex. 1455, 1531, etc.) &lt;br&gt; &lt;br&gt;La liste des nomenclatures est disponible à l&#x27;adresse suivante : &lt;br&gt;https://aida.ineris.fr/liste_documents/1/18023/1 | [optional] 
 **regime** | **str**| Le code du régime de l&#x27;établissement : &lt;br&gt;- A : Autorisation &lt;br&gt;- E : Enregistrement &lt;br&gt;- AUTRE : Autre régime  | [optional] 
 **statut_seveso** | **str**| Le code du statut SEVESO de l&#x27;établissement : &lt;br&gt;- 1 : Seveso seuil haut &lt;br&gt;- 2 : Seveso seuil bas &lt;br&gt;- 3 : Non Seveso | [optional] 
 **priorite_nationale** | **bool**| Etablissement « priorité nationale » - true/false | [optional] 
 **ied** | **bool**| Etablissement « IED-MTD » - true/false | [optional] 
 **date_maj** | **str**| Date de modification des données. La date est au format \&quot;AAAA-MM-JJ\&quot;. L&#x27;API renvoie tous les établissements dont la date de modification est supérieure ou égale à dateMaj. | [optional] 

### Return type

[**PaginatedResponseInstallationClassee**](PaginatedResponseInstallationClassee.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rechercher_aiots_par_geolocalisation1**
> list[str] rechercher_aiots_par_geolocalisation1(page_size=page_size, page=page, departement=departement, region=region)

Cette interface est conçue pour diffuser les données installations classées de Gun Env à destination de Géorisques.

Cette interface est conçue pour diffuser les données installations classées de Gun Env à destination de Géorisques.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InstallationsClassesApi()
page_size = 6000 # int | Taille des pages (optional) (default to 6000)
page = 1 # int | Numéro de la page (optional) (default to 1)
departement = 'departement_example' # str | Le code du département recherché (optional)
region = 'region_example' # str | Le code de la région recherchée (optional)

try:
    # Cette interface est conçue pour diffuser les données installations classées de Gun Env à destination de Géorisques.
    api_response = api_instance.rechercher_aiots_par_geolocalisation1(page_size=page_size, page=page, departement=departement, region=region)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstallationsClassesApi->rechercher_aiots_par_geolocalisation1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Taille des pages | [optional] [default to 6000]
 **page** | **int**| Numéro de la page | [optional] [default to 1]
 **departement** | **str**| Le code du département recherché | [optional] 
 **region** | **str**| Le code de la région recherchée | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

