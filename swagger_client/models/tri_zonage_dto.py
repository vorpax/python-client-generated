# coding: utf-8

"""
    Services API Géorisques

    Description de l'API de Géorisques  # noqa: E501

    OpenAPI spec version: 1.9.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TriZonageDto(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'code_national_tri': 'str',
        'identifiant_tri': 'str',
        'libelle_tri': 'str',
        'cours_deau': 'str',
        'type_inondation': 'LexType',
        'scenario': 'LexScenario',
        'date_arrete_pcb': 'date',
        'date_arrete_carte': 'date',
        'date_arrete_pcb_local': 'date',
        'date_arrete_prefet_parties_prenantes': 'date',
        'date_arrete_approbation': 'date',
        'date_arrete_national': 'date',
        'code_insee': 'str',
        'libelle_commune': 'str'
    }

    attribute_map = {
        'code_national_tri': 'code_national_tri',
        'identifiant_tri': 'identifiant_tri',
        'libelle_tri': 'libelle_tri',
        'cours_deau': 'cours_deau',
        'type_inondation': 'typeInondation',
        'scenario': 'scenario',
        'date_arrete_pcb': 'date_arrete_pcb',
        'date_arrete_carte': 'date_arrete_carte',
        'date_arrete_pcb_local': 'date_arrete_pcb_local',
        'date_arrete_prefet_parties_prenantes': 'date_arrete_prefet_parties_prenantes',
        'date_arrete_approbation': 'date_arrete_approbation',
        'date_arrete_national': 'date_arrete_national',
        'code_insee': 'code_insee',
        'libelle_commune': 'libelle_commune'
    }

    def __init__(self, code_national_tri=None, identifiant_tri=None, libelle_tri=None, cours_deau=None, type_inondation=None, scenario=None, date_arrete_pcb=None, date_arrete_carte=None, date_arrete_pcb_local=None, date_arrete_prefet_parties_prenantes=None, date_arrete_approbation=None, date_arrete_national=None, code_insee=None, libelle_commune=None):  # noqa: E501
        """TriZonageDto - a model defined in Swagger"""  # noqa: E501
        self._code_national_tri = None
        self._identifiant_tri = None
        self._libelle_tri = None
        self._cours_deau = None
        self._type_inondation = None
        self._scenario = None
        self._date_arrete_pcb = None
        self._date_arrete_carte = None
        self._date_arrete_pcb_local = None
        self._date_arrete_prefet_parties_prenantes = None
        self._date_arrete_approbation = None
        self._date_arrete_national = None
        self._code_insee = None
        self._libelle_commune = None
        self.discriminator = None
        if code_national_tri is not None:
            self.code_national_tri = code_national_tri
        if identifiant_tri is not None:
            self.identifiant_tri = identifiant_tri
        if libelle_tri is not None:
            self.libelle_tri = libelle_tri
        if cours_deau is not None:
            self.cours_deau = cours_deau
        if type_inondation is not None:
            self.type_inondation = type_inondation
        if scenario is not None:
            self.scenario = scenario
        if date_arrete_pcb is not None:
            self.date_arrete_pcb = date_arrete_pcb
        if date_arrete_carte is not None:
            self.date_arrete_carte = date_arrete_carte
        if date_arrete_pcb_local is not None:
            self.date_arrete_pcb_local = date_arrete_pcb_local
        if date_arrete_prefet_parties_prenantes is not None:
            self.date_arrete_prefet_parties_prenantes = date_arrete_prefet_parties_prenantes
        if date_arrete_approbation is not None:
            self.date_arrete_approbation = date_arrete_approbation
        if date_arrete_national is not None:
            self.date_arrete_national = date_arrete_national
        if code_insee is not None:
            self.code_insee = code_insee
        if libelle_commune is not None:
            self.libelle_commune = libelle_commune

    @property
    def code_national_tri(self):
        """Gets the code_national_tri of this TriZonageDto.  # noqa: E501


        :return: The code_national_tri of this TriZonageDto.  # noqa: E501
        :rtype: str
        """
        return self._code_national_tri

    @code_national_tri.setter
    def code_national_tri(self, code_national_tri):
        """Sets the code_national_tri of this TriZonageDto.


        :param code_national_tri: The code_national_tri of this TriZonageDto.  # noqa: E501
        :type: str
        """

        self._code_national_tri = code_national_tri

    @property
    def identifiant_tri(self):
        """Gets the identifiant_tri of this TriZonageDto.  # noqa: E501


        :return: The identifiant_tri of this TriZonageDto.  # noqa: E501
        :rtype: str
        """
        return self._identifiant_tri

    @identifiant_tri.setter
    def identifiant_tri(self, identifiant_tri):
        """Sets the identifiant_tri of this TriZonageDto.


        :param identifiant_tri: The identifiant_tri of this TriZonageDto.  # noqa: E501
        :type: str
        """

        self._identifiant_tri = identifiant_tri

    @property
    def libelle_tri(self):
        """Gets the libelle_tri of this TriZonageDto.  # noqa: E501


        :return: The libelle_tri of this TriZonageDto.  # noqa: E501
        :rtype: str
        """
        return self._libelle_tri

    @libelle_tri.setter
    def libelle_tri(self, libelle_tri):
        """Sets the libelle_tri of this TriZonageDto.


        :param libelle_tri: The libelle_tri of this TriZonageDto.  # noqa: E501
        :type: str
        """

        self._libelle_tri = libelle_tri

    @property
    def cours_deau(self):
        """Gets the cours_deau of this TriZonageDto.  # noqa: E501


        :return: The cours_deau of this TriZonageDto.  # noqa: E501
        :rtype: str
        """
        return self._cours_deau

    @cours_deau.setter
    def cours_deau(self, cours_deau):
        """Sets the cours_deau of this TriZonageDto.


        :param cours_deau: The cours_deau of this TriZonageDto.  # noqa: E501
        :type: str
        """

        self._cours_deau = cours_deau

    @property
    def type_inondation(self):
        """Gets the type_inondation of this TriZonageDto.  # noqa: E501


        :return: The type_inondation of this TriZonageDto.  # noqa: E501
        :rtype: LexType
        """
        return self._type_inondation

    @type_inondation.setter
    def type_inondation(self, type_inondation):
        """Sets the type_inondation of this TriZonageDto.


        :param type_inondation: The type_inondation of this TriZonageDto.  # noqa: E501
        :type: LexType
        """

        self._type_inondation = type_inondation

    @property
    def scenario(self):
        """Gets the scenario of this TriZonageDto.  # noqa: E501


        :return: The scenario of this TriZonageDto.  # noqa: E501
        :rtype: LexScenario
        """
        return self._scenario

    @scenario.setter
    def scenario(self, scenario):
        """Sets the scenario of this TriZonageDto.


        :param scenario: The scenario of this TriZonageDto.  # noqa: E501
        :type: LexScenario
        """

        self._scenario = scenario

    @property
    def date_arrete_pcb(self):
        """Gets the date_arrete_pcb of this TriZonageDto.  # noqa: E501


        :return: The date_arrete_pcb of this TriZonageDto.  # noqa: E501
        :rtype: date
        """
        return self._date_arrete_pcb

    @date_arrete_pcb.setter
    def date_arrete_pcb(self, date_arrete_pcb):
        """Sets the date_arrete_pcb of this TriZonageDto.


        :param date_arrete_pcb: The date_arrete_pcb of this TriZonageDto.  # noqa: E501
        :type: date
        """

        self._date_arrete_pcb = date_arrete_pcb

    @property
    def date_arrete_carte(self):
        """Gets the date_arrete_carte of this TriZonageDto.  # noqa: E501


        :return: The date_arrete_carte of this TriZonageDto.  # noqa: E501
        :rtype: date
        """
        return self._date_arrete_carte

    @date_arrete_carte.setter
    def date_arrete_carte(self, date_arrete_carte):
        """Sets the date_arrete_carte of this TriZonageDto.


        :param date_arrete_carte: The date_arrete_carte of this TriZonageDto.  # noqa: E501
        :type: date
        """

        self._date_arrete_carte = date_arrete_carte

    @property
    def date_arrete_pcb_local(self):
        """Gets the date_arrete_pcb_local of this TriZonageDto.  # noqa: E501


        :return: The date_arrete_pcb_local of this TriZonageDto.  # noqa: E501
        :rtype: date
        """
        return self._date_arrete_pcb_local

    @date_arrete_pcb_local.setter
    def date_arrete_pcb_local(self, date_arrete_pcb_local):
        """Sets the date_arrete_pcb_local of this TriZonageDto.


        :param date_arrete_pcb_local: The date_arrete_pcb_local of this TriZonageDto.  # noqa: E501
        :type: date
        """

        self._date_arrete_pcb_local = date_arrete_pcb_local

    @property
    def date_arrete_prefet_parties_prenantes(self):
        """Gets the date_arrete_prefet_parties_prenantes of this TriZonageDto.  # noqa: E501


        :return: The date_arrete_prefet_parties_prenantes of this TriZonageDto.  # noqa: E501
        :rtype: date
        """
        return self._date_arrete_prefet_parties_prenantes

    @date_arrete_prefet_parties_prenantes.setter
    def date_arrete_prefet_parties_prenantes(self, date_arrete_prefet_parties_prenantes):
        """Sets the date_arrete_prefet_parties_prenantes of this TriZonageDto.


        :param date_arrete_prefet_parties_prenantes: The date_arrete_prefet_parties_prenantes of this TriZonageDto.  # noqa: E501
        :type: date
        """

        self._date_arrete_prefet_parties_prenantes = date_arrete_prefet_parties_prenantes

    @property
    def date_arrete_approbation(self):
        """Gets the date_arrete_approbation of this TriZonageDto.  # noqa: E501


        :return: The date_arrete_approbation of this TriZonageDto.  # noqa: E501
        :rtype: date
        """
        return self._date_arrete_approbation

    @date_arrete_approbation.setter
    def date_arrete_approbation(self, date_arrete_approbation):
        """Sets the date_arrete_approbation of this TriZonageDto.


        :param date_arrete_approbation: The date_arrete_approbation of this TriZonageDto.  # noqa: E501
        :type: date
        """

        self._date_arrete_approbation = date_arrete_approbation

    @property
    def date_arrete_national(self):
        """Gets the date_arrete_national of this TriZonageDto.  # noqa: E501


        :return: The date_arrete_national of this TriZonageDto.  # noqa: E501
        :rtype: date
        """
        return self._date_arrete_national

    @date_arrete_national.setter
    def date_arrete_national(self, date_arrete_national):
        """Sets the date_arrete_national of this TriZonageDto.


        :param date_arrete_national: The date_arrete_national of this TriZonageDto.  # noqa: E501
        :type: date
        """

        self._date_arrete_national = date_arrete_national

    @property
    def code_insee(self):
        """Gets the code_insee of this TriZonageDto.  # noqa: E501


        :return: The code_insee of this TriZonageDto.  # noqa: E501
        :rtype: str
        """
        return self._code_insee

    @code_insee.setter
    def code_insee(self, code_insee):
        """Sets the code_insee of this TriZonageDto.


        :param code_insee: The code_insee of this TriZonageDto.  # noqa: E501
        :type: str
        """

        self._code_insee = code_insee

    @property
    def libelle_commune(self):
        """Gets the libelle_commune of this TriZonageDto.  # noqa: E501


        :return: The libelle_commune of this TriZonageDto.  # noqa: E501
        :rtype: str
        """
        return self._libelle_commune

    @libelle_commune.setter
    def libelle_commune(self, libelle_commune):
        """Sets the libelle_commune of this TriZonageDto.


        :param libelle_commune: The libelle_commune of this TriZonageDto.  # noqa: E501
        :type: str
        """

        self._libelle_commune = libelle_commune

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(TriZonageDto, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TriZonageDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
