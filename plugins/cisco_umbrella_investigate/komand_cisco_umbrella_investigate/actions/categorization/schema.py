# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Return if domain has been flagged as malicious by the Cisco Security Labs team"


class Input:
    DOMAINS = "domains"
    

class Output:
    CATEGORIES = "categories"
    

class CategorizationInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "domains": {
      "type": "array",
      "title": "Domains",
      "description": "Domain names",
      "items": {
        "type": "string"
      },
      "order": 1
    }
  },
  "required": [
    "domains"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CategorizationOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "categories": {
      "type": "array",
      "title": "Categories",
      "description": "Information about content categories and security categories",
      "items": {
        "$ref": "#/definitions/category"
      },
      "order": 1
    }
  },
  "required": [
    "categories"
  ],
  "definitions": {
    "category": {
      "type": "object",
      "title": "category",
      "properties": {
        "content_categories": {
          "type": "array",
          "title": "Content Categories",
          "description": "The Umbrella content category or categories that match this domain. If none match, the return will be blank",
          "order": 4
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Domain name",
          "order": 1
        },
        "security_categories": {
          "type": "array",
          "title": "Security Categories",
          "description": "The Umbrella security category, or categories, that match this domain or that this domain is associated with. If none match, the return will be blank",
          "order": 3
        },
        "status": {
          "type": "integer",
          "title": "Status",
          "description": "The status will be '-1' if the domain is believed to be malicious, '1' if the domain is believed to be benign, '0' if it hasn't been classified yet",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
