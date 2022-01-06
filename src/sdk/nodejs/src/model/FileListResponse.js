/*
 * self-managed-osdu
 * Rest API Documentation for Self Managed OSDU
 *
 * OpenAPI spec version: 0.11.0
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 2.4.22
 *
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD. Register as an anonymous module.
    define(['ApiClient', 'model/FileLocation'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    module.exports = factory(require('../ApiClient'), require('./FileLocation'));
  } else {
    // Browser globals (root is window)
    if (!root.SelfManagedOsdu) {
      root.SelfManagedOsdu = {};
    }
    root.SelfManagedOsdu.FileListResponse = factory(root.SelfManagedOsdu.ApiClient, root.SelfManagedOsdu.FileLocation);
  }
}(this, function(ApiClient, FileLocation) {
  'use strict';

  /**
   * The FileListResponse model module.
   * @module model/FileListResponse
   * @version 0.11.0
   */

  /**
   * Constructs a new <code>FileListResponse</code>.
   * @alias module:model/FileListResponse
   * @class
   */
  var exports = function() {
  };

  /**
   * Constructs a <code>FileListResponse</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:model/FileListResponse} obj Optional instance to populate.
   * @return {module:model/FileListResponse} The populated <code>FileListResponse</code> instance.
   */
  exports.constructFromObject = function(data, obj) {
    if (data) {
      obj = obj || new exports();
      if (data.hasOwnProperty('content'))
        obj.content = ApiClient.convertToType(data['content'], [FileLocation]);
      if (data.hasOwnProperty('number'))
        obj._number = ApiClient.convertToType(data['number'], 'Number');
      if (data.hasOwnProperty('numberOfElements'))
        obj.numberOfElements = ApiClient.convertToType(data['numberOfElements'], 'Number');
      if (data.hasOwnProperty('size'))
        obj.size = ApiClient.convertToType(data['size'], 'Number');
    }
    return obj;
  }

  /**
   * @member {Array.<module:model/FileLocation>} content
   */
  exports.prototype.content = undefined;

  /**
   * @member {Number} _number
   */
  exports.prototype._number = undefined;

  /**
   * @member {Number} numberOfElements
   */
  exports.prototype.numberOfElements = undefined;

  /**
   * @member {Number} size
   */
  exports.prototype.size = undefined;


  return exports;

}));
