# coding: utf-8

# flake8: noqa
"""
    Services API Géorisques

    Description de l'API de Géorisques  # noqa: E501

    OpenAPI spec version: 1.9.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from swagger_client.models.adresse_dto import AdresseDto
from swagger_client.models.azi import Azi
from swagger_client.models.casias_dto import CasiasDto
from swagger_client.models.cat_nat import CatNat
from swagger_client.models.cavites import Cavites
from swagger_client.models.commune_dto import CommuneDto
from swagger_client.models.commune_model import CommuneModel
from swagger_client.models.coordonnees import Coordonnees
from swagger_client.models.crs import Crs
from swagger_client.models.departement import Departement
from swagger_client.models.dicrim import Dicrim
from swagger_client.models.etat_ppr import EtatPPR
from swagger_client.models.ex_basol_dto import ExBasolDto
from swagger_client.models.famille_risques import FamilleRisques
from swagger_client.models.feature import Feature
from swagger_client.models.feature_collection import FeatureCollection
from swagger_client.models.geo_json_object import GeoJsonObject
from swagger_client.models.geometry_collection import GeometryCollection
from swagger_client.models.inspection import Inspection
from swagger_client.models.installation_classee import InstallationClassee
from swagger_client.models.lex_scenario import LexScenario
from swagger_client.models.lex_type import LexType
from swagger_client.models.line_string import LineString
from swagger_client.models.lng_lat_alt import LngLatAlt
from swagger_client.models.metadata_fichier import MetadataFichier
from swagger_client.models.multi_line_string import MultiLineString
from swagger_client.models.multi_point import MultiPoint
from swagger_client.models.multi_polygon import MultiPolygon
from swagger_client.models.mvt import Mvt
from swagger_client.models.no_paginated_response_tri_zonage_dto import NoPaginatedResponseTriZonageDto
from swagger_client.models.old_model import OldModel
from swagger_client.models.one_of_casias_dto_geom import OneOfCasiasDtoGeom
from swagger_client.models.one_of_ex_basol_dto_geom import OneOfExBasolDtoGeom
from swagger_client.models.one_of_ppr_geom_perimetre import OneOfPPRGeomPerimetre
from swagger_client.models.one_of_ppr_geom_zonage import OneOfPPRGeomZonage
from swagger_client.models.one_of_sis_dto_geom import OneOfSisDtoGeom
from swagger_client.models.one_of_sup_dto_geom import OneOfSupDtoGeom
from swagger_client.models.ppr import PPR
from swagger_client.models.paginated_response_azi import PaginatedResponseAzi
from swagger_client.models.paginated_response_casias_dto import PaginatedResponseCasiasDto
from swagger_client.models.paginated_response_cat_nat import PaginatedResponseCatNat
from swagger_client.models.paginated_response_cavites import PaginatedResponseCavites
from swagger_client.models.paginated_response_dicrim import PaginatedResponseDicrim
from swagger_client.models.paginated_response_etat_ppr import PaginatedResponseEtatPPR
from swagger_client.models.paginated_response_ex_basol_dto import PaginatedResponseExBasolDto
from swagger_client.models.paginated_response_famille_risques import PaginatedResponseFamilleRisques
from swagger_client.models.paginated_response_installation_classee import PaginatedResponseInstallationClassee
from swagger_client.models.paginated_response_mvt import PaginatedResponseMvt
from swagger_client.models.paginated_response_ppr import PaginatedResponsePPR
from swagger_client.models.paginated_response_papi import PaginatedResponsePapi
from swagger_client.models.paginated_response_radon import PaginatedResponseRadon
from swagger_client.models.paginated_response_risques import PaginatedResponseRisques
from swagger_client.models.paginated_response_sis_dto import PaginatedResponseSisDto
from swagger_client.models.paginated_response_sup_dto import PaginatedResponseSupDto
from swagger_client.models.paginated_response_tim import PaginatedResponseTim
from swagger_client.models.paginated_response_tri import PaginatedResponseTri
from swagger_client.models.paginated_response_zonage_sismique import PaginatedResponseZonageSismique
from swagger_client.models.papi import Papi
from swagger_client.models.point import Point
from swagger_client.models.polygon import Polygon
from swagger_client.models.radon import Radon
from swagger_client.models.rapport_risques_json_dto import RapportRisquesJsonDto
from swagger_client.models.region import Region
from swagger_client.models.risque import Risque
from swagger_client.models.risque_dto import RisqueDto
from swagger_client.models.risque_gaspar import RisqueGaspar
from swagger_client.models.risques import Risques
from swagger_client.models.risques_naturels_dto import RisquesNaturelsDto
from swagger_client.models.risques_technologiques_dto import RisquesTechnologiquesDto
from swagger_client.models.rubrique_ic import RubriqueIC
from swagger_client.models.sis_dto import SisDto
from swagger_client.models.ssp import Ssp
from swagger_client.models.sup_dto import SupDto
from swagger_client.models.tim import Tim
from swagger_client.models.tri import Tri
from swagger_client.models.tri_zonage_dto import TriZonageDto
from swagger_client.models.zonage_argile import ZonageArgile
from swagger_client.models.zonage_sismique import ZonageSismique
