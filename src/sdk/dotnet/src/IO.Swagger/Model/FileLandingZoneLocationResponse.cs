/* 
 * self-managed-osdu
 *
 * Rest API Documentation for Self Managed OSDU
 *
 * OpenAPI spec version: 0.11.0
 * 
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 */

using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using SwaggerDateConverter = IO.Swagger.Client.SwaggerDateConverter;

namespace IO.Swagger.Model
{
    /// <summary>
    /// FileLandingZoneLocationResponse
    /// </summary>
    [DataContract]
    public partial class FileLandingZoneLocationResponse :  IEquatable<FileLandingZoneLocationResponse>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="FileLandingZoneLocationResponse" /> class.
        /// </summary>
        /// <param name="fileID">fileID.</param>
        /// <param name="location">location.</param>
        public FileLandingZoneLocationResponse(string fileID = default(string), Dictionary<string, string> location = default(Dictionary<string, string>))
        {
            this.FileID = fileID;
            this.Location = location;
        }
        
        /// <summary>
        /// Gets or Sets FileID
        /// </summary>
        [DataMember(Name="FileID", EmitDefaultValue=false)]
        public string FileID { get; set; }

        /// <summary>
        /// Gets or Sets Location
        /// </summary>
        [DataMember(Name="Location", EmitDefaultValue=false)]
        public Dictionary<string, string> Location { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class FileLandingZoneLocationResponse {\n");
            sb.Append("  FileID: ").Append(FileID).Append("\n");
            sb.Append("  Location: ").Append(Location).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as FileLandingZoneLocationResponse);
        }

        /// <summary>
        /// Returns true if FileLandingZoneLocationResponse instances are equal
        /// </summary>
        /// <param name="input">Instance of FileLandingZoneLocationResponse to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(FileLandingZoneLocationResponse input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.FileID == input.FileID ||
                    (this.FileID != null &&
                    this.FileID.Equals(input.FileID))
                ) && 
                (
                    this.Location == input.Location ||
                    this.Location != null &&
                    this.Location.SequenceEqual(input.Location)
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.FileID != null)
                    hashCode = hashCode * 59 + this.FileID.GetHashCode();
                if (this.Location != null)
                    hashCode = hashCode * 59 + this.Location.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

}
