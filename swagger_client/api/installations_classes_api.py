# coding: utf-8

"""
    Services API Géorisques

    Description de l'API de Géorisques  # noqa: E501

    OpenAPI spec version: 1.9.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class InstallationsClassesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def rechercher_aiots_par_geolocalisation(self, **kwargs):  # noqa: E501
        """Cette interface est conçue pour diffuser les données installations classées de Gun Env à destination de Géorisques.  # noqa: E501

        Cette interface est conçue pour diffuser les données installations classées de Gun Env à destination de Géorisques.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rechercher_aiots_par_geolocalisation(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] code_insee: Code(s) INSEE de la commune. Si plusieurs codes communes, séparer les codes communes par une virgule, par exemple pour avoir les codes insee 45234 et 45100 : code_insee=45234,45100. Le nombre maximum de codes est 10. Ce type de recherche ne peut pas être combiné avec une recherche au rayon.
        :param list[str] siret: Code(s) siret de l'installation classée.Si plusieurs codes, les séparer par une virgule, par exemple  : siret=48335930300011,35392644700130.
        :param list[str] code_aiot: Code(s) de(s) (l')installation(s) classée(s) à 10 chiffres.Si plusieurs codes, les séparer par une virgule,par exemple  : codeAIOT=0005402775,0005602790.
        :param str latlon: Saisir un point sous la forme longitude,latitude. Le séparateur de décimales est toujours un point. La paire de coordonnées est separée par une virgule. Exemple : 2.29253,48.92572
        :param float rayon: Saisir un rayon de recherche exprimé en mètres. Attention la valeur du rayon de recherche est limitée à 10 000 mètres. Par defaut le rayon de recherche est fixé a 1000 mètres.
        :param int page: Numéro de la page
        :param int page_size: Taille des pages
        :param str debut_inspection: Date d'inspection minimum à recherchée. La date est au format \"AAAA-MM-JJ\".
        :param str fin_inspection: Date d'inspection maximum à recherchée. La date est au format \"AAAA-MM-JJ\".
        :param str raison_sociale: Tout ou partie d'un nom d'établissement recherché et insensible à la casse
        :param str region: Le code de la région recherchée
        :param str departement: Le code du département recherché
        :param str activite: Le code de l'activité principale de l'établissement, tel que défini dans la nomenclature NAF v2 (ex. 01, 02, etc.) : <br>https://www.insee.fr/fr/information/2406147
        :param list[str] nomenclature: La liste des codes de nomenclatures d'installations classées. <br>La liste des valeurs est séparée par une virgule (ex. 1455, 1531, etc.) <br> <br>La liste des nomenclatures est disponible à l'adresse suivante : <br>https://aida.ineris.fr/liste_documents/1/18023/1
        :param str regime: Le code du régime de l'établissement : <br>- A : Autorisation <br>- E : Enregistrement <br>- AUTRE : Autre régime 
        :param str statut_seveso: Le code du statut SEVESO de l'établissement : <br>- 1 : Seveso seuil haut <br>- 2 : Seveso seuil bas <br>- 3 : Non Seveso
        :param bool priorite_nationale: Etablissement « priorité nationale » - true/false
        :param bool ied: Etablissement « IED-MTD » - true/false
        :param str date_maj: Date de modification des données. La date est au format \"AAAA-MM-JJ\". L'API renvoie tous les établissements dont la date de modification est supérieure ou égale à dateMaj.
        :return: PaginatedResponseInstallationClassee
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rechercher_aiots_par_geolocalisation_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.rechercher_aiots_par_geolocalisation_with_http_info(**kwargs)  # noqa: E501
            return data

    def rechercher_aiots_par_geolocalisation_with_http_info(self, **kwargs):  # noqa: E501
        """Cette interface est conçue pour diffuser les données installations classées de Gun Env à destination de Géorisques.  # noqa: E501

        Cette interface est conçue pour diffuser les données installations classées de Gun Env à destination de Géorisques.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rechercher_aiots_par_geolocalisation_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] code_insee: Code(s) INSEE de la commune. Si plusieurs codes communes, séparer les codes communes par une virgule, par exemple pour avoir les codes insee 45234 et 45100 : code_insee=45234,45100. Le nombre maximum de codes est 10. Ce type de recherche ne peut pas être combiné avec une recherche au rayon.
        :param list[str] siret: Code(s) siret de l'installation classée.Si plusieurs codes, les séparer par une virgule, par exemple  : siret=48335930300011,35392644700130.
        :param list[str] code_aiot: Code(s) de(s) (l')installation(s) classée(s) à 10 chiffres.Si plusieurs codes, les séparer par une virgule,par exemple  : codeAIOT=0005402775,0005602790.
        :param str latlon: Saisir un point sous la forme longitude,latitude. Le séparateur de décimales est toujours un point. La paire de coordonnées est separée par une virgule. Exemple : 2.29253,48.92572
        :param float rayon: Saisir un rayon de recherche exprimé en mètres. Attention la valeur du rayon de recherche est limitée à 10 000 mètres. Par defaut le rayon de recherche est fixé a 1000 mètres.
        :param int page: Numéro de la page
        :param int page_size: Taille des pages
        :param str debut_inspection: Date d'inspection minimum à recherchée. La date est au format \"AAAA-MM-JJ\".
        :param str fin_inspection: Date d'inspection maximum à recherchée. La date est au format \"AAAA-MM-JJ\".
        :param str raison_sociale: Tout ou partie d'un nom d'établissement recherché et insensible à la casse
        :param str region: Le code de la région recherchée
        :param str departement: Le code du département recherché
        :param str activite: Le code de l'activité principale de l'établissement, tel que défini dans la nomenclature NAF v2 (ex. 01, 02, etc.) : <br>https://www.insee.fr/fr/information/2406147
        :param list[str] nomenclature: La liste des codes de nomenclatures d'installations classées. <br>La liste des valeurs est séparée par une virgule (ex. 1455, 1531, etc.) <br> <br>La liste des nomenclatures est disponible à l'adresse suivante : <br>https://aida.ineris.fr/liste_documents/1/18023/1
        :param str regime: Le code du régime de l'établissement : <br>- A : Autorisation <br>- E : Enregistrement <br>- AUTRE : Autre régime 
        :param str statut_seveso: Le code du statut SEVESO de l'établissement : <br>- 1 : Seveso seuil haut <br>- 2 : Seveso seuil bas <br>- 3 : Non Seveso
        :param bool priorite_nationale: Etablissement « priorité nationale » - true/false
        :param bool ied: Etablissement « IED-MTD » - true/false
        :param str date_maj: Date de modification des données. La date est au format \"AAAA-MM-JJ\". L'API renvoie tous les établissements dont la date de modification est supérieure ou égale à dateMaj.
        :return: PaginatedResponseInstallationClassee
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['code_insee', 'siret', 'code_aiot', 'latlon', 'rayon', 'page', 'page_size', 'debut_inspection', 'fin_inspection', 'raison_sociale', 'region', 'departement', 'activite', 'nomenclature', 'regime', 'statut_seveso', 'priorite_nationale', 'ied', 'date_maj']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rechercher_aiots_par_geolocalisation" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'code_insee' in params:
            query_params.append(('code_insee', params['code_insee']))  # noqa: E501
            collection_formats['code_insee'] = 'multi'  # noqa: E501
        if 'siret' in params:
            query_params.append(('siret', params['siret']))  # noqa: E501
            collection_formats['siret'] = 'multi'  # noqa: E501
        if 'code_aiot' in params:
            query_params.append(('codeAIOT', params['code_aiot']))  # noqa: E501
            collection_formats['codeAIOT'] = 'multi'  # noqa: E501
        if 'latlon' in params:
            query_params.append(('latlon', params['latlon']))  # noqa: E501
        if 'rayon' in params:
            query_params.append(('rayon', params['rayon']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'debut_inspection' in params:
            query_params.append(('debutInspection', params['debut_inspection']))  # noqa: E501
        if 'fin_inspection' in params:
            query_params.append(('finInspection', params['fin_inspection']))  # noqa: E501
        if 'raison_sociale' in params:
            query_params.append(('raisonSociale', params['raison_sociale']))  # noqa: E501
        if 'region' in params:
            query_params.append(('region', params['region']))  # noqa: E501
        if 'departement' in params:
            query_params.append(('departement', params['departement']))  # noqa: E501
        if 'activite' in params:
            query_params.append(('activite', params['activite']))  # noqa: E501
        if 'nomenclature' in params:
            query_params.append(('nomenclature', params['nomenclature']))  # noqa: E501
            collection_formats['nomenclature'] = 'multi'  # noqa: E501
        if 'regime' in params:
            query_params.append(('regime', params['regime']))  # noqa: E501
        if 'statut_seveso' in params:
            query_params.append(('statutSeveso', params['statut_seveso']))  # noqa: E501
        if 'priorite_nationale' in params:
            query_params.append(('prioriteNationale', params['priorite_nationale']))  # noqa: E501
        if 'ied' in params:
            query_params.append(('ied', params['ied']))  # noqa: E501
        if 'date_maj' in params:
            query_params.append(('dateMaj', params['date_maj']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/installations_classees', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaginatedResponseInstallationClassee',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def rechercher_aiots_par_geolocalisation1(self, **kwargs):  # noqa: E501
        """Cette interface est conçue pour diffuser les données installations classées de Gun Env à destination de Géorisques.  # noqa: E501

        Cette interface est conçue pour diffuser les données installations classées de Gun Env à destination de Géorisques.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rechercher_aiots_par_geolocalisation1(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_size: Taille des pages
        :param int page: Numéro de la page
        :param str departement: Le code du département recherché
        :param str region: Le code de la région recherchée
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.rechercher_aiots_par_geolocalisation1_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.rechercher_aiots_par_geolocalisation1_with_http_info(**kwargs)  # noqa: E501
            return data

    def rechercher_aiots_par_geolocalisation1_with_http_info(self, **kwargs):  # noqa: E501
        """Cette interface est conçue pour diffuser les données installations classées de Gun Env à destination de Géorisques.  # noqa: E501

        Cette interface est conçue pour diffuser les données installations classées de Gun Env à destination de Géorisques.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.rechercher_aiots_par_geolocalisation1_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_size: Taille des pages
        :param int page: Numéro de la page
        :param str departement: Le code du département recherché
        :param str region: Le code de la région recherchée
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page', 'departement', 'region']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method rechercher_aiots_par_geolocalisation1" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'departement' in params:
            query_params.append(('departement', params['departement']))  # noqa: E501
        if 'region' in params:
            query_params.append(('region', params['region']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/zip'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/csv/installations_classees', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
