# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Find an Automox device by IP address"


class Input:
    IP_ADDRESS = "ip_address"
    ORG_ID = "org_id"
    

class Output:
    DEVICE = "device"
    

class GetDeviceByIpInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "ip_address": {
      "type": "string",
      "title": "IP Address",
      "description": "IP address of device",
      "order": 2
    },
    "org_id": {
      "type": "integer",
      "title": "Organization ID",
      "description": "Identifier of organization to restrict results",
      "order": 1
    }
  },
  "required": [
    "ip_address"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetDeviceByIpOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "device": {
      "$ref": "#/definitions/device",
      "title": "Device",
      "description": "The matched Automox device",
      "order": 1
    }
  },
  "definitions": {
    "device": {
      "type": "object",
      "title": "device",
      "properties": {
        "agent_version": {
          "type": "string",
          "title": "Agent Version",
          "description": "The agent version of a device",
          "order": 18
        },
        "compliant": {
          "type": "boolean",
          "title": "Compliant",
          "description": "Whether a device is compliant",
          "order": 23
        },
        "connected": {
          "type": "boolean",
          "title": "Connected",
          "description": "Whether a device is currently connected to the Automox platform",
          "order": 26
        },
        "create_time": {
          "type": "string",
          "title": "Create Time",
          "description": "The time a device was created in the Automox platform",
          "order": 10
        },
        "custom_name": {
          "type": "string",
          "title": "Custom Name",
          "description": "The custom name of a device",
          "order": 19
        },
        "deleted": {
          "type": "boolean",
          "title": "Deleted",
          "description": "Whether a device is deleted",
          "order": 9
        },
        "detail": {
          "type": "object",
          "title": "Detail",
          "description": "Additional details of a device",
          "order": 17
        },
        "display_name": {
          "type": "string",
          "title": "Display Name",
          "description": "The display name of a device",
          "order": 24
        },
        "id": {
          "type": "integer",
          "title": "Device ID",
          "description": "The device ID",
          "order": 1
        },
        "ip_addrs": {
          "type": "array",
          "title": "IP Addresses",
          "description": "List of IP addresses for a device",
          "items": {
            "type": "string"
          },
          "order": 14
        },
        "ip_addrs_private": {
          "type": "array",
          "title": "Private IP Addresses",
          "description": "List of private IP addresses for a device",
          "items": {
            "type": "string"
          },
          "order": 15
        },
        "is_compatible": {
          "type": "boolean",
          "title": "Is Compatible",
          "description": "Whether a device is compatible with the Automox platform",
          "order": 20
        },
        "is_delayed_by_notification": {
          "type": "boolean",
          "title": "Is Delayed by Notification",
          "description": "Whether patching is delayed by a device notificiation",
          "order": 28
        },
        "is_delayed_by_user": {
          "type": "boolean",
          "title": "Is Delayed By User",
          "description": "Whether patching is delayed by a user",
          "order": 30
        },
        "last_disconnect_time": {
          "type": "string",
          "title": "Last Disconnect Time",
          "description": "The last time a device disconnected from the Automox platform",
          "order": 32
        },
        "last_logged_in_user": {
          "type": "string",
          "title": "Last Logged In User",
          "description": "The last logged in user of a device",
          "order": 36
        },
        "last_refresh_time": {
          "type": "string",
          "title": "Last Refresh Time",
          "description": "The last time a device was refreshed",
          "order": 6
        },
        "last_scan_failed": {
          "type": "boolean",
          "title": "Last Scan Failed",
          "description": "Whether the last scan failed on a device",
          "order": 21
        },
        "last_update_time": {
          "type": "string",
          "title": "Last Update Time",
          "description": "The last time a device was updated in the Automox platform",
          "order": 5
        },
        "name": {
          "type": "string",
          "title": "Device Name",
          "description": "The device name",
          "order": 4
        },
        "needs_attention": {
          "type": "boolean",
          "title": "Needs Attention",
          "description": "Whether a device currently needs attention",
          "order": 33
        },
        "needs_reboot": {
          "type": "boolean",
          "title": "Needs Reboot",
          "description": "Whether a device needs rebooted",
          "order": 7
        },
        "next_patch_time": {
          "type": "string",
          "title": "Next Patch Time",
          "description": "The time for the next device patch",
          "order": 27
        },
        "organization_id": {
          "type": "integer",
          "title": "Organization ID",
          "description": "The organization identifier of a device",
          "order": 3
        },
        "os_family": {
          "type": "string",
          "title": "Operating System Family",
          "description": "The operating system family of a device",
          "order": 13
        },
        "os_name": {
          "type": "string",
          "title": "Operating System",
          "description": "The name of the operating system of a device",
          "order": 12
        },
        "os_version": {
          "type": "string",
          "title": "Operating System Version",
          "description": "The operating system version of a device",
          "order": 11
        },
        "patches": {
          "type": "integer",
          "title": "Patches",
          "description": "The number of patches currently identified for a device",
          "order": 16
        },
        "pending": {
          "type": "boolean",
          "title": "Pending",
          "description": "Whether work is pending on a device",
          "order": 22
        },
        "pending_patches": {
          "type": "integer",
          "title": "Pending Patches",
          "description": "The number of pending patches for a device",
          "order": 25
        },
        "reboot_is_delayed_by_notification": {
          "type": "boolean",
          "title": "Reboot Is Delayed By Notification",
          "description": "Whether rebooting is delayed by a device notification",
          "order": 29
        },
        "reboot_is_delayed_by_user": {
          "type": "boolean",
          "title": "Reboot Is Delayed By User",
          "description": "Whether rebooting is delayed by a user",
          "order": 31
        },
        "serial_number": {
          "type": "string",
          "title": "Serial Number",
          "description": "The serial number of a device",
          "order": 34
        },
        "server_group_id": {
          "type": "integer",
          "title": "Server Group ID",
          "description": "The server group identifier of a device",
          "order": 2
        },
        "status": {
          "$ref": "#/definitions/device_status_details",
          "title": "Status",
          "description": "The device status details",
          "order": 35
        },
        "tags": {
          "type": "array",
          "title": "Tags",
          "description": "List of tags",
          "items": {
            "type": "string"
          },
          "order": 8
        }
      },
      "definitions": {
        "device_policy_status": {
          "type": "object",
          "title": "device_policy_status",
          "properties": {
            "compliant": {
              "type": "boolean",
              "title": "Compliant",
              "description": "Whether a device is compliant to given status",
              "order": 2
            },
            "id": {
              "type": "integer",
              "title": "Policy ID",
              "description": "The identifier of the policy",
              "order": 1
            }
          }
        },
        "device_status_details": {
          "type": "object",
          "title": "device_status_details",
          "properties": {
            "agent_status": {
              "type": "string",
              "title": "Agent Status",
              "description": "The status of a device agent",
              "order": 2
            },
            "device_status": {
              "type": "string",
              "title": "Device Status",
              "description": "The status of a device",
              "order": 1
            },
            "policy_status": {
              "type": "string",
              "title": "Policy Status",
              "description": "The overall status of all policies assigned to a device",
              "order": 3
            },
            "policy_statuses": {
              "type": "array",
              "title": "Policy Statuses",
              "description": "A list of policy statuses with compliant details",
              "items": {
                "$ref": "#/definitions/device_policy_status"
              },
              "order": 4
            }
          },
          "definitions": {
            "device_policy_status": {
              "type": "object",
              "title": "device_policy_status",
              "properties": {
                "compliant": {
                  "type": "boolean",
                  "title": "Compliant",
                  "description": "Whether a device is compliant to given status",
                  "order": 2
                },
                "id": {
                  "type": "integer",
                  "title": "Policy ID",
                  "description": "The identifier of the policy",
                  "order": 1
                }
              }
            }
          }
        }
      }
    },
    "device_policy_status": {
      "type": "object",
      "title": "device_policy_status",
      "properties": {
        "compliant": {
          "type": "boolean",
          "title": "Compliant",
          "description": "Whether a device is compliant to given status",
          "order": 2
        },
        "id": {
          "type": "integer",
          "title": "Policy ID",
          "description": "The identifier of the policy",
          "order": 1
        }
      }
    },
    "device_status_details": {
      "type": "object",
      "title": "device_status_details",
      "properties": {
        "agent_status": {
          "type": "string",
          "title": "Agent Status",
          "description": "The status of a device agent",
          "order": 2
        },
        "device_status": {
          "type": "string",
          "title": "Device Status",
          "description": "The status of a device",
          "order": 1
        },
        "policy_status": {
          "type": "string",
          "title": "Policy Status",
          "description": "The overall status of all policies assigned to a device",
          "order": 3
        },
        "policy_statuses": {
          "type": "array",
          "title": "Policy Statuses",
          "description": "A list of policy statuses with compliant details",
          "items": {
            "$ref": "#/definitions/device_policy_status"
          },
          "order": 4
        }
      },
      "definitions": {
        "device_policy_status": {
          "type": "object",
          "title": "device_policy_status",
          "properties": {
            "compliant": {
              "type": "boolean",
              "title": "Compliant",
              "description": "Whether a device is compliant to given status",
              "order": 2
            },
            "id": {
              "type": "integer",
              "title": "Policy ID",
              "description": "The identifier of the policy",
              "order": 1
            }
          }
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
