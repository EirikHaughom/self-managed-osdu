/*
 * self-managed-osdu
 * Rest API Documentation for Self Managed OSDU
 *
 * OpenAPI spec version: 0.11.0
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */


package io.swagger.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;

/**
 * Group properties
 */
@ApiModel(description = "Group properties")
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2021-12-21T22:06:14.852Z")
public class EntitlementGroupProperties {
  @SerializedName("name")
  private String name = null;

  @SerializedName("description")
  private String description = null;

  @SerializedName("email")
  private String email = null;

  public EntitlementGroupProperties name(String name) {
    this.name = name;
    return this;
  }

   /**
   * The name of an entitlement or group.
   * @return name
  **/
  @ApiModelProperty(example = "service.entitlements.user", required = true, value = "The name of an entitlement or group.")
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public EntitlementGroupProperties description(String description) {
    this.description = description;
    return this;
  }

   /**
   * The description of an entitlement or group.
   * @return description
  **/
  @ApiModelProperty(example = "A service entitlement", required = true, value = "The description of an entitlement or group.")
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }

  public EntitlementGroupProperties email(String email) {
    this.email = email;
    return this;
  }

   /**
   * The fully qualified group name.
   * @return email
  **/
  @ApiModelProperty(example = "service.entitlements.user@partition.contoso.com", required = true, value = "The fully qualified group name.")
  public String getEmail() {
    return email;
  }

  public void setEmail(String email) {
    this.email = email;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    EntitlementGroupProperties entitlementGroupProperties = (EntitlementGroupProperties) o;
    return Objects.equals(this.name, entitlementGroupProperties.name) &&
        Objects.equals(this.description, entitlementGroupProperties.description) &&
        Objects.equals(this.email, entitlementGroupProperties.email);
  }

  @Override
  public int hashCode() {
    return Objects.hash(name, description, email);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class EntitlementGroupProperties {\n");
    
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("    email: ").append(toIndentedString(email)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}

