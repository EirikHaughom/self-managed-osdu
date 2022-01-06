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


class FileLocationResponse(object):
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
        'driver': 'FileDriver',
        'location': 'str'
    }

    attribute_map = {
        'driver': 'Driver',
        'location': 'Location'
    }

    def __init__(self, driver=None, location=None, _configuration=None):  # noqa: E501
        """FileLocationResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._driver = None
        self._location = None
        self.discriminator = None

        if driver is not None:
            self.driver = driver
        if location is not None:
            self.location = location

    @property
    def driver(self):
        """Gets the driver of this FileLocationResponse.  # noqa: E501


        :return: The driver of this FileLocationResponse.  # noqa: E501
        :rtype: FileDriver
        """
        return self._driver

    @driver.setter
    def driver(self, driver):
        """Sets the driver of this FileLocationResponse.


        :param driver: The driver of this FileLocationResponse.  # noqa: E501
        :type: FileDriver
        """

        self._driver = driver

    @property
    def location(self):
        """Gets the location of this FileLocationResponse.  # noqa: E501


        :return: The location of this FileLocationResponse.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this FileLocationResponse.


        :param location: The location of this FileLocationResponse.  # noqa: E501
        :type: str
        """

        self._location = location

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
        if issubclass(FileLocationResponse, dict):
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
        if not isinstance(other, FileLocationResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileLocationResponse):
            return True

        return self.to_dict() != other.to_dict()
