# coding: utf-8

"""
    Services API Géorisques

    Description de l'API de Géorisques  # noqa: E501

    OpenAPI spec version: 1.9.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.tri___zonage_rglementaire_api import TRIZonageRglementaireApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTRIZonageRglementaireApi(unittest.TestCase):
    """TRIZonageRglementaireApi unit test stubs"""

    def setUp(self):
        self.api = TRIZonageRglementaireApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_recherche_tri_zonage(self):
        """Test case for recherche_tri_zonage

        Lister les Territoires à  Risques importants d'Inondation (TRI) recensés sur l'adresse concernée  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
