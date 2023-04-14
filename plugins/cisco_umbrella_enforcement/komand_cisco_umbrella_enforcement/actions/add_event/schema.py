# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Posts a malware event for processing and optionally adds it to the customer's domain list"


class Input:
    ALERTTIME = "alertTime"
    DEVICEID = "deviceId"
    DEVICEVERSION = "deviceVersion"
    DISABLEDSTSAFEGUARDS = "disableDstSafeguards"
    DSTDOMAIN = "dstDomain"
    DSTIP = "dstIP"
    DSTURL = "dstUrl"
    EVENTDESCRIPTION = "eventDescription"
    EVENTHASH = "eventHash"
    EVENTSEVERITY = "eventSeverity"
    EVENTTIME = "eventTime"
    EVENTTYPE = "eventType"
    EXTERNALURL = "externalURL"
    FILEHASH = "fileHash"
    FILENAME = "fileName"
    PROTOCOLVERSION = "protocolVersion"
    PROVIDERNAME = "providerName"
    SRC = "src"
    

class Output:
    ID = "ID"
    

class AddEventInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "alertTime": {
      "type": "string",
      "title": "Alert Time",
      "description": "The time the event was sent to Umbrella",
      "order": 1
    },
    "deviceId": {
      "type": "string",
      "title": "Device ID",
      "description": "The ID of the device sending the event",
      "order": 2
    },
    "deviceVersion": {
      "type": "string",
      "title": "Device Version",
      "description": "The version of the device sending the event",
      "order": 3
    },
    "disableDstSafeguards": {
      "type": "boolean",
      "title": "Disable Destination Safeguards",
      "description": "True bypasses validations normally performed against submitted events",
      "default": false,
      "order": 18
    },
    "dstDomain": {
      "type": "string",
      "title": "Destination Domain",
      "description": "The destination domain specified (follow RFC 3986 encoding guidelines)",
      "order": 4
    },
    "dstIP": {
      "type": "string",
      "title": "Destination IP",
      "description": "The destination UP of the domain, specified in IPv4 dotted-decimal notation",
      "order": 5
    },
    "dstUrl": {
      "type": "string",
      "title": "Destination URL",
      "description": "The destination URL specified (follow RFC 3986 encoding guidelines)",
      "order": 6
    },
    "eventDescription": {
      "type": "string",
      "title": "Event Description",
      "description": "Variant or other descriptor of event type",
      "order": 7
    },
    "eventHash": {
      "type": "string",
      "title": "Event Hash",
      "description": "A unique hash of the event",
      "order": 8
    },
    "eventSeverity": {
      "type": "string",
      "title": "Event Severity",
      "description": "The partner threat level or rating",
      "order": 9
    },
    "eventTime": {
      "type": "string",
      "title": "Event Time",
      "description": "The time the event was detected",
      "order": 10
    },
    "eventType": {
      "type": "string",
      "title": "Event Type",
      "description": "Common name or classification of threat",
      "order": 11
    },
    "externalURL": {
      "type": "string",
      "title": "External URL",
      "description": "External page containing additional information about event",
      "order": 12
    },
    "fileHash": {
      "type": "string",
      "title": "File Hash",
      "description": "SHA-1 of file reported by appliance",
      "order": 13
    },
    "fileName": {
      "type": "string",
      "title": "File Name",
      "description": "Path to file exhibiting malicious behaviour",
      "order": 14
    },
    "protocolVersion": {
      "type": "string",
      "title": "Protocol Version",
      "description": "The version of the protocol for the API",
      "default": "1.0a",
      "order": 15
    },
    "providerName": {
      "type": "string",
      "title": "Provider Name",
      "description": "The provider name for the API",
      "default": "Security Platform",
      "order": 16
    },
    "src": {
      "type": "string",
      "title": "Src",
      "description": "The first IP or hostname associated with the infected device",
      "order": 17
    }
  },
  "required": [
    "alertTime",
    "deviceId",
    "deviceVersion",
    "dstDomain",
    "dstUrl",
    "eventTime",
    "protocolVersion",
    "providerName"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddEventOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "ID": {
      "type": "object",
      "title": "ID List",
      "description": "Object containing added IDs",
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
