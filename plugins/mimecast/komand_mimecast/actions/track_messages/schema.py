# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Search for messages processing, and current state using specific message information. Either one of `Send From`, `Send To`, `Subject`, `Sender IP` fields, or `Message ID` must not be empty"


class Input:
    END_DATE = "end_date"
    MESSAGE_ID = "message_id"
    ROUTES = "routes"
    SEARCH_REASON = "search_reason"
    SEND_FROM = "send_from"
    SEND_TO = "send_to"
    SENDER_IP = "sender_ip"
    START_DATE = "start_date"
    SUBJECT = "subject"
    

class Output:
    TRACKED_EMAILS = "tracked_emails"
    

class TrackMessagesInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "end_date": {
      "type": "string",
      "title": "End Date",
      "displayType": "date",
      "description": "The date and time of the latest message to track",
      "format": "date-time",
      "order": 3
    },
    "message_id": {
      "type": "string",
      "title": "Message ID",
      "description": "The internet message id of the message to track",
      "order": 4
    },
    "routes": {
      "type": "array",
      "title": "Routes",
      "description": "An array of routes to filter by. Possible values are internal, outbound and inbound",
      "items": {
        "type": "string"
      },
      "order": 5
    },
    "search_reason": {
      "type": "string",
      "title": "Search Reason",
      "description": "Reason for Tracking a email, used for activity tracking purposes",
      "order": 1
    },
    "send_from": {
      "type": "string",
      "title": "Send From",
      "description": "The sending email address or domain of the messages to track",
      "order": 6
    },
    "send_to": {
      "type": "string",
      "title": "Send To",
      "description": "The recipient email address or domain of the messages to track",
      "order": 7
    },
    "sender_ip": {
      "type": "string",
      "title": "Sender IP",
      "description": "The source IP address of messages to track",
      "order": 9
    },
    "start_date": {
      "type": "string",
      "title": "Start Date",
      "displayType": "date",
      "description": "The date and time of the earliest message to track",
      "format": "date-time",
      "order": 2
    },
    "subject": {
      "type": "string",
      "title": "Subject",
      "description": "The subject of the messages to track",
      "order": 8
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class TrackMessagesOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "tracked_emails": {
      "type": "array",
      "title": "Tracked Emails",
      "description": "An array of found tracked emails",
      "items": {
        "$ref": "#/definitions/tracked_emails"
      },
      "order": 1
    }
  },
  "required": [
    "tracked_emails"
  ],
  "definitions": {
    "recipient": {
      "type": "object",
      "title": "recipient",
      "properties": {
        "displayableName": {
          "type": "string",
          "title": "Display Name",
          "description": "The display name of the recipient",
          "order": 2
        },
        "emailAddress": {
          "type": "string",
          "title": "Email Address",
          "description": "The email address of the recipient",
          "order": 1
        }
      }
    },
    "sender": {
      "type": "object",
      "title": "sender",
      "properties": {
        "displayableName": {
          "type": "string",
          "title": "Display Name",
          "description": "The display name of the sender",
          "order": 2
        },
        "emailAddress": {
          "type": "string",
          "title": "Email Address",
          "description": "The email address of the sender",
          "order": 1
        }
      }
    },
    "tracked_emails": {
      "type": "object",
      "title": "tracked_emails",
      "properties": {
        "attachments": {
          "type": "boolean",
          "title": "Attachments",
          "description": "Indicates whether the message has attachments or not",
          "order": 4
        },
        "detectionLevel": {
          "type": "string",
          "title": "Detection Level",
          "description": "The spam scanning level applied to the message",
          "order": 1
        },
        "fromEnv": {
          "$ref": "#/definitions/sender",
          "title": "Envelope From",
          "description": "An object describing the envelope from address of the message",
          "order": 8
        },
        "fromHdr": {
          "$ref": "#/definitions/sender",
          "title": "Header From",
          "description": "An object describing the header from address information of the message",
          "order": 7
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "The Mimecast ID of the message",
          "order": 10
        },
        "received": {
          "type": "string",
          "title": "Received",
          "displayType": "date",
          "description": "The date and time the message was received by Mimecast",
          "format": "date-time",
          "order": 3
        },
        "route": {
          "type": "string",
          "title": "Route",
          "description": "The route of the message",
          "order": 5
        },
        "senderIP": {
          "type": "string",
          "title": "Sender IP Address",
          "description": "The source IP address of the message",
          "order": 9
        },
        "sent": {
          "type": "string",
          "title": "Sent",
          "displayType": "date",
          "description": "The date and time that the message was sent / processed by Mimecast",
          "format": "date-time",
          "order": 11
        },
        "spamScore": {
          "type": "integer",
          "title": "Spam Score",
          "description": "The spam score of the received message",
          "order": 13
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "The status of the message",
          "order": 2
        },
        "subject": {
          "type": "string",
          "title": "Subject",
          "description": "The subject of the message",
          "order": 12
        },
        "to": {
          "type": "array",
          "title": "To",
          "description": "An array of recipients",
          "items": {
            "$ref": "#/definitions/recipient"
          },
          "order": 6
        }
      },
      "definitions": {
        "recipient": {
          "type": "object",
          "title": "recipient",
          "properties": {
            "displayableName": {
              "type": "string",
              "title": "Display Name",
              "description": "The display name of the recipient",
              "order": 2
            },
            "emailAddress": {
              "type": "string",
              "title": "Email Address",
              "description": "The email address of the recipient",
              "order": 1
            }
          }
        },
        "sender": {
          "type": "object",
          "title": "sender",
          "properties": {
            "displayableName": {
              "type": "string",
              "title": "Display Name",
              "description": "The display name of the sender",
              "order": 2
            },
            "emailAddress": {
              "type": "string",
              "title": "Email Address",
              "description": "The email address of the sender",
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
