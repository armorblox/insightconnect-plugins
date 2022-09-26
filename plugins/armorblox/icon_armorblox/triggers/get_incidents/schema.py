# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Get a list of incidents identified by Armorblox, by default it starts polling all the incidents since last day"


class Input:
    
    INTERVAL = "interval"
    

class Output:
    
    INCIDENTS = "incidents"
    

class GetIncidentsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "interval": {
      "type": "integer",
      "title": "Fetch_Interval",
      "description": "Polling inteval in seconds",
      "default": 600,
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetIncidentsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "incidents": {
      "type": "array",
      "title": "Incidents",
      "description": "A list of 100 incidents identified by Armorblox",
      "items": {
        "$ref": "#/definitions/incident"
      },
      "order": 1
    }
  },
  "required": [
    "incidents"
  ],
  "definitions": {
    "engagement": {
      "type": "object",
      "title": "engagement",
      "properties": {
        "fwd_mail_count": {
          "type": "string",
          "title": "Mail Count",
          "description": "Mail Count",
          "order": 1
        },
        "reply_mail_count": {
          "type": "string",
          "title": "Mail Count",
          "description": "Mail Count",
          "order": 2
        }
      }
    },
    "final_detection_tag": {
      "type": "object",
      "title": "final_detection_tag",
      "properties": {
        "detection_tag_id": {
          "type": "string",
          "title": "Detection tag ID",
          "description": "Detection tag ID",
          "order": 1
        },
        "detection_tag_name": {
          "type": "string",
          "title": "Detection tag name",
          "description": "Detection tag name",
          "order": 2
        }
      }
    },
    "incident": {
      "type": "object",
      "title": "incident",
      "properties": {
        "app_name": {
          "type": "string",
          "title": "App Name",
          "description": "App Name",
          "order": 10
        },
        "date": {
          "type": "string",
          "title": "Occured Date",
          "displayType": "date",
          "format": "date-time",
          "order": 3
        },
        "engagements": {
          "$ref": "#/definitions/engagement",
          "title": "Engagements",
          "description": "Engagements",
          "order": 15
        },
        "external_senders": {
          "type": "array",
          "title": "External senders",
          "description": "List of external senders",
          "items": {
            "type": "string"
          },
          "order": 11
        },
        "external_users": {
          "type": "array",
          "title": "external users",
          "description": "List of external users",
          "items": {
            "$ref": "#/definitions/user"
          },
          "order": 18
        },
        "final_detection_tags": {
          "type": "array",
          "title": "Detection tags",
          "description": "Detection Tags",
          "items": {
            "$ref": "#/definitions/final_detection_tag"
          },
          "order": 19
        },
        "folder_categories": {
          "type": "array",
          "title": "Folder category",
          "description": "Folder category",
          "items": {
            "type": "string"
          },
          "order": 12
        },
        "id": {
          "type": "string",
          "title": "Incident ID",
          "description": "Incident ID",
          "order": 8
        },
        "incident_type": {
          "type": "string",
          "title": "Incident Type",
          "description": "Incident Type",
          "order": 14
        },
        "object_type": {
          "type": "string",
          "title": "Object Type",
          "description": "Object Type",
          "order": 7
        },
        "policy_names": {
          "type": "array",
          "title": "policy_names",
          "description": "List of policies",
          "items": {
            "type": "string"
          },
          "order": 4
        },
        "priority": {
          "type": "string",
          "title": "Priority",
          "description": "Priority of the incident",
          "order": 1
        },
        "remediation_actions": {
          "type": "array",
          "title": "Remediation Action",
          "description": "Remediation Action",
          "items": {
            "type": "string"
          },
          "order": 16
        },
        "research_status": {
          "type": "string",
          "title": "Research Status",
          "description": "Research Status",
          "order": 9
        },
        "resolution_state": {
          "type": "string",
          "title": "resolution_state",
          "description": "Resolution State",
          "order": 6
        },
        "scl_score": {
          "type": "integer",
          "title": "SCL Score",
          "order": 13
        },
        "tagged": {
          "type": "boolean",
          "title": "Is email tagged",
          "description": "Is email tagged",
          "order": 2
        },
        "title": {
          "type": "string",
          "title": "title",
          "description": "title",
          "order": 5
        },
        "users": {
          "type": "array",
          "title": "users",
          "description": "List of users",
          "items": {
            "$ref": "#/definitions/user"
          },
          "order": 17
        }
      },
      "definitions": {
        "engagement": {
          "type": "object",
          "title": "engagement",
          "properties": {
            "fwd_mail_count": {
              "type": "string",
              "title": "Mail Count",
              "description": "Mail Count",
              "order": 1
            },
            "reply_mail_count": {
              "type": "string",
              "title": "Mail Count",
              "description": "Mail Count",
              "order": 2
            }
          }
        },
        "final_detection_tag": {
          "type": "object",
          "title": "final_detection_tag",
          "properties": {
            "detection_tag_id": {
              "type": "string",
              "title": "Detection tag ID",
              "description": "Detection tag ID",
              "order": 1
            },
            "detection_tag_name": {
              "type": "string",
              "title": "Detection tag name",
              "description": "Detection tag name",
              "order": 2
            }
          }
        },
        "user": {
          "type": "object",
          "title": "user",
          "properties": {
            "email": {
              "type": "string",
              "title": "user email",
              "description": "User email",
              "order": 2
            },
            "is_vip": {
              "type": "boolean",
              "title": "Is User VIP",
              "description": "Is User VIP",
              "order": 3
            },
            "name": {
              "type": "string",
              "title": "user name",
              "description": "User name",
              "order": 1
            }
          }
        }
      }
    },
    "user": {
      "type": "object",
      "title": "user",
      "properties": {
        "email": {
          "type": "string",
          "title": "user email",
          "description": "User email",
          "order": 2
        },
        "is_vip": {
          "type": "boolean",
          "title": "Is User VIP",
          "description": "Is User VIP",
          "order": 3
        },
        "name": {
          "type": "string",
          "title": "user name",
          "description": "User name",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
