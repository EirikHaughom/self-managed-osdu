# coding: utf-8

"""
    self-managed-osdu

    Rest API Documentation for Self Managed OSDU  # noqa: E501

    OpenAPI spec version: 0.11.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class FileToOneRelationship(object):
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
        'confidence': 'float',
        'id': 'str',
        'name': 'str',
        'version': 'float'
    }

    attribute_map = {
        'confidence': 'confidence',
        'id': 'id',
        'name': 'name',
        'version': 'version'
    }

    def __init__(self, confidence=None, id=None, name=None, version=None, _configuration=None):  # noqa: E501
        """FileToOneRelationship - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._confidence = None
        self._id = None
        self._name = None
        self._version = None
        self.discriminator = None

        if confidence is not None:
            self.confidence = confidence
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version

    @property
    def confidence(self):
        """Gets the confidence of this FileToOneRelationship.  # noqa: E501

        The confidence of the relationship. If the property is absent a well-known relation is implied.  # noqa: E501

        :return: The confidence of this FileToOneRelationship.  # noqa: E501
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this FileToOneRelationship.

        The confidence of the relationship. If the property is absent a well-known relation is implied.  # noqa: E501

        :param confidence: The confidence of this FileToOneRelationship.  # noqa: E501
        :type: float
        """

        self._confidence = confidence

    @property
    def id(self):
        """Gets the id of this FileToOneRelationship.  # noqa: E501

        The id of the related object in the Data Ecosystem. If set, the id has priority over the natural key in the name property.  # noqa: E501

        :return: The id of this FileToOneRelationship.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FileToOneRelationship.

        The id of the related object in the Data Ecosystem. If set, the id has priority over the natural key in the name property.  # noqa: E501

        :param id: The id of this FileToOneRelationship.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this FileToOneRelationship.  # noqa: E501

        The name or natural key of the related object. This property is required if the target object id could not (yet) be identified.  # noqa: E501

        :return: The name of this FileToOneRelationship.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FileToOneRelationship.

        The name or natural key of the related object. This property is required if the target object id could not (yet) be identified.  # noqa: E501

        :param name: The name of this FileToOneRelationship.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def version(self):
        """Gets the version of this FileToOneRelationship.  # noqa: E501

        The version number of the related entity. If no version number is specified, the last version is implied.  # noqa: E501

        :return: The version of this FileToOneRelationship.  # noqa: E501
        :rtype: float
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this FileToOneRelationship.

        The version number of the related entity. If no version number is specified, the last version is implied.  # noqa: E501

        :param version: The version of this FileToOneRelationship.  # noqa: E501
        :type: float
        """

        self._version = version

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
        if issubclass(FileToOneRelationship, dict):
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
        if not isinstance(other, FileToOneRelationship):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileToOneRelationship):
            return True

        return self.to_dict() != other.to_dict()
