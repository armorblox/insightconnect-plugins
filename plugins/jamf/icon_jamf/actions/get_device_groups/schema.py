# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Gets a list of all groups a device is member of"


class Input:
    ID = "ID"
    

class Output:
    DEVICE_GROUPS = "device_groups"
    

class GetDeviceGroupsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "ID": {
      "type": "integer",
      "title": "Device ID",
      "description": "Device ID",
      "order": 1
    }
  },
  "required": [
    "ID"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetDeviceGroupsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "device_groups": {
      "type": "array",
      "title": "Device Groups",
      "description": "List of device groups",
      "items": {
        "$ref": "#/definitions/device_group_detail"
      },
      "order": 1
    }
  },
  "required": [
    "device_groups"
  ],
  "definitions": {
    "device_group_detail": {
      "type": "object",
      "title": "device_group_detail",
      "properties": {
        "id": {
          "type": "integer",
          "title": "Group ID",
          "description": "Group ID",
          "order": 1
        },
        "name": {
          "type": "string",
          "title": "Group Name",
          "description": "Group name",
          "order": 2
        }
      },
      "required": [
        "id",
        "name"
      ]
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
