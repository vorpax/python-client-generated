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
from swagger_client.api.radon_api import RadonApi  # noqa: E501
from swagger_client.rest import ApiException


class TestRadonApi(unittest.TestCase):
    """RadonApi unit test stubs"""

    def setUp(self):
        self.api = RadonApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_recherche_radon1(self):
        """Test case for recherche_radon1

        Rechercher les potentiels radon des communes  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
