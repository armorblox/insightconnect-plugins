# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Adds Label to an Issue"


class Input:
    ISSUE_NUMBER = "issue_number"
    LABEL = "label"
    ORGANIZATION = "organization"
    REPOSITORY = "repository"
    

class Output:
    URL = "url"
    

class AddIssueLabelInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "issue_number": {
      "type": "number",
      "title": "Issue Number",
      "description": "issue number",
      "order": 3
    },
    "label": {
      "type": "string",
      "title": "Label",
      "description": "issue label",
      "order": 4
    },
    "organization": {
      "type": "string",
      "title": "Organization",
      "description": "Organizational owner of repository",
      "order": 2
    },
    "repository": {
      "type": "string",
      "title": "Repository",
      "description": "Repository to post issue",
      "order": 1
    }
  },
  "required": [
    "issue_number",
    "label",
    "repository"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AddIssueLabelOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "url": {
      "type": "string",
      "title": "URL",
      "description": "URL",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
