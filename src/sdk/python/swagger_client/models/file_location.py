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


class FileLocation(object):
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
        'file_id': 'FileID',
        'driver': 'FileDriver',
        'location': 'str',
        'created_at': 'datetime',
        'created_by': 'str'
    }

    attribute_map = {
        'file_id': 'FileID',
        'driver': 'Driver',
        'location': 'Location',
        'created_at': 'CreatedAt',
        'created_by': 'CreatedBy'
    }

    def __init__(self, file_id=None, driver=None, location=None, created_at=None, created_by=None, _configuration=None):  # noqa: E501
        """FileLocation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._file_id = None
        self._driver = None
        self._location = None
        self._created_at = None
        self._created_by = None
        self.discriminator = None

        if file_id is not None:
            self.file_id = file_id
        if driver is not None:
            self.driver = driver
        if location is not None:
            self.location = location
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by

    @property
    def file_id(self):
        """Gets the file_id of this FileLocation.  # noqa: E501


        :return: The file_id of this FileLocation.  # noqa: E501
        :rtype: FileID
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this FileLocation.


        :param file_id: The file_id of this FileLocation.  # noqa: E501
        :type: FileID
        """

        self._file_id = file_id

    @property
    def driver(self):
        """Gets the driver of this FileLocation.  # noqa: E501


        :return: The driver of this FileLocation.  # noqa: E501
        :rtype: FileDriver
        """
        return self._driver

    @driver.setter
    def driver(self, driver):
        """Sets the driver of this FileLocation.


        :param driver: The driver of this FileLocation.  # noqa: E501
        :type: FileDriver
        """

        self._driver = driver

    @property
    def location(self):
        """Gets the location of this FileLocation.  # noqa: E501


        :return: The location of this FileLocation.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this FileLocation.


        :param location: The location of this FileLocation.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def created_at(self):
        """Gets the created_at of this FileLocation.  # noqa: E501


        :return: The created_at of this FileLocation.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this FileLocation.


        :param created_at: The created_at of this FileLocation.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this FileLocation.  # noqa: E501


        :return: The created_by of this FileLocation.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this FileLocation.


        :param created_by: The created_by of this FileLocation.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

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
        if issubclass(FileLocation, dict):
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
        if not isinstance(other, FileLocation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileLocation):
            return True

        return self.to_dict() != other.to_dict()
