## Input for minknow/minknow-core script dev_tools/generate_eeprom_code.py
<%def name="grpc_type(field)"><%
    type_ = field["type"]
    if type_ == "string":
        return 'string'
    elif type_ == "unsigned_int":
        if field["size"] > 4:
            return "uint64"
        else:
            return "uint32"
    elif type_ == "signed_int":
        if field["size"] > 4:
            return "sint64"
        else:
            return "sint32"
    elif type_ == "float":
        if field["size"] > 4:
            return "double"
        else:
            return "float"
    raise ValueError("Unknown type {}".format(type_))
%></%def>\
<%def name="grpc_wrapper_type(field)"><%
    type_map = {
        "string": "google.protobuf.StringValue",
        "uint64": "google.protobuf.UInt64Value",
        "uint32": "google.protobuf.UInt32Value",
        "int64": "google.protobuf.Int64Value",
        "int32": "google.protobuf.Int32Value",
        "sint64": "google.protobuf.Int64Value",
        "sint32": "google.protobuf.Int32Value",
        "double": "google.protobuf.DoubleValue",
        "float": "google.protobuf.FloatValue",
    }
    return type_map[grpc_type(field)]
%></%def>\
<%def name="non_default_null(field)"><%
    return "null_value" in field and field["null_value"] not in ["", 0]
%></%def>\
syntax="proto3";

package minknow_api.production;

option java_package = "com.nanoporetech.minknow_api";
option objc_class_prefix = "MKAPI";

##import "google/protobuf/wrappers.proto";

// Methods used in production.
//
// These might modify the device or flowcell permanently. They are not available
// in non-production contexts.
service ProductionService {
    // Writes data to the EEPROM on the attached flowcell.
    //
    // This call will fail with FAILED_PRECONDITION if there is no device connected or no flowcell
    // attached.
    //
    // Very little checking of the provided values is done, and no attempt is made to preserve
    // existing data. Use the other methods on this service for that.
    rpc write_flowcell_data(WriteFlowcellDataRequest) returns (WriteFlowcellDataResponse) {}

    // Write the flowcell ID to the flowcell EEPROM.
    //
    // Flowcell IDs over 8 characters or containing unprintable characters will be rejected with
    // INVALID_ARGUMENT. An empty string effectively clears the flowcell ID.
    //
    // If nothing is currently written on the flowcell EEPROM, it will write the data in a suitable
    // format. If the EEPROM contains a data version that supports this field, it will be updated,
    // and all other fields will be preserved. If the EEPROM contains a data version that doesn't
    // support this field, this call will fail with FAILED_PRECONDITION and the EEPROM will not be
    // changed.
    //
    // This call will fail with FAILED_PRECONDITION if there is no device connected or no flowcell
    // attached, or if the flowcell's EEPROM is corrupt or has data in an unknown version.
    rpc write_flowcell_id(WriteFlowcellIdRequest) returns (WriteFlowcellIdResponse) {}

    // Write the number of wells to the flowcell EEPROM.
    //
    // Well counts greater than the number supported by the hardware will be rejected. Passing zero
    // will effectively set it to the default for this device.
    //
    // If nothing is currently written on the flowcell EEPROM, it will write the data in a suitable
    // format. If the EEPROM contains a data version that supports this field, it will be updated,
    // and all other fields will be preserved. If the EEPROM contains a data version that doesn't
    // support this field, this call will fail with FAILED_PRECONDITION and the EEPROM will not be
    // changed.
    //
    // This call will fail with FAILED_PRECONDITION if there is no device connected or no flowcell
    // attached, or if the flowcell's EEPROM is corrupt or has data in an unknown version.
    rpc write_wells_per_channel(WriteWellsPerChannelRequest) returns (WriteWellsPerChannelResponse) {}

    // Write the product code to the flowcell EEPROM.
    //
    // This is the code presented to customers in the shop, eg: "FLO-MIN106".
    //
    // Produce codes over 10 characters or containing unprintable characters will be rejected with
    // INVALID_ARGUMENT. An empty string effectively clears the product code.
    //
    // If nothing is currently written on the flowcell EEPROM, it will write the data in a suitable
    // format. If the EEPROM contains a data version that supports this field, it will be updated,
    // and all other fields will be preserved. If the EEPROM contains a data version that doesn't
    // support this field, this call will fail with FAILED_PRECONDITION and the EEPROM will not be
    // changed.
    //
    // This call will fail with FAILED_PRECONDITION if there is no device connected or no flowcell
    // attached, or if the flowcell's EEPROM is corrupt or has data in an unknown version.
    rpc write_product_code(WriteProductCodeRequest) returns (WriteProductCodeResponse) {}

    // Write the temperature offset to the flowcell EEPROM.
    //
    // The temperature offset is specified in hundreths of a degree Celsius, and can range from
    // -327.67 degrees Celsius to 327.67 degrees Celsius. The value -32767 will be accepted, but
    // will cause the temperature offset to cleared, just as though no value had been provided at
    // all.
    //
    // If nothing is currently written on the flowcell EEPROM, it will write the data in a suitable
    // format. If the EEPROM contains a data version that supports this field, it will be updated,
    // and all other fields will be preserved. If the EEPROM contains a data version that doesn't
    // support this field, this call will fail with FAILED_PRECONDITION and the EEPROM will not be
    // changed.
    //
    // This call will fail with FAILED_PRECONDITION if there is no device connected or no flowcell
    // attached, or if the flowcell's EEPROM is corrupt or has data in an unknown version.
    rpc write_temperature_offset(WriteTemperatureOffsetRequest) returns (WriteTemperatureOffsetResponse) {}
}

message WriteFlowcellDataRequest {
    message Empty {}
    % for version, fields in sorted(versions.items()):
    message Version${version} {
        % for i, field in enumerate(sorted(fields, key=lambda x: x["addr_start"])):
        % if non_default_null(field):
        // Used to make the field nullable, since the null value is not protobuf's default.
        oneof ${field["name"]}_nullable {
        % endif
        // ${field["description"]}
        ${grpc_type(field)} ${field["name"]} = ${i + 1};
        % if non_default_null(field):
        }
        % endif
        % endfor
    }
    % endfor

    oneof data {
        // Clears any existing data from the EEPROM.
        Empty empty = 1;
        % for version in sorted(versions.keys()):
        // Writes version ${version} data to the EEPROM.
        Version${version} v${version} = ${int(version) + 1};
        % endfor
    };
}
message WriteFlowcellDataResponse {}

message WriteFlowcellIdRequest {
    string flowcell_id = 1;
}
message WriteFlowcellIdResponse {}

message WriteWellsPerChannelRequest {
    uint32 wells_per_channel = 1;
}
message WriteWellsPerChannelResponse {}

message WriteProductCodeRequest {
    string product_code = 1;
}
message WriteProductCodeResponse {}

message WriteTemperatureOffsetRequest {
    oneof offset_nullable {
        int32 offset = 1;
    }
}
message WriteTemperatureOffsetResponse {}
