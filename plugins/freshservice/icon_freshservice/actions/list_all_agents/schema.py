# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "View information about all agents in the account. Use filters to view only specific agents (those who match the criteria that you choose)"


class Input:
    ACTIVE = "active"
    EMAIL = "email"
    MOBILEPHONENUMBER = "mobilePhoneNumber"
    STATE = "state"
    WORKPHONENUMBER = "workPhoneNumber"
    

class Output:
    AGENTS = "agents"
    

class ListAllAgentsInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "active": {
      "type": "string",
      "title": "Active",
      "description": "Return active, deactivated or all agents",
      "default": "all",
      "enum": [
        "true",
        "false",
        "all"
      ],
      "order": 5
    },
    "email": {
      "type": "string",
      "title": "Email",
      "description": "Email address of the agent based on which the results will be filtered",
      "order": 1
    },
    "mobilePhoneNumber": {
      "type": "string",
      "title": "Mobile Phone Number",
      "description": "Mobile phone number of the agent based on which the results will be filtered",
      "order": 2
    },
    "state": {
      "type": "string",
      "title": "State",
      "description": "Return fulltime, occasional or all agents",
      "default": "all",
      "enum": [
        "fulltime",
        "occasional",
        "all"
      ],
      "order": 4
    },
    "workPhoneNumber": {
      "type": "string",
      "title": "Work Phone Number",
      "description": "Work phone number of the agent based on which the results will be filtered",
      "order": 3
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListAllAgentsOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "agents": {
      "type": "array",
      "title": "Agents",
      "description": "Information about agents in the account",
      "items": {
        "$ref": "#/definitions/agent"
      },
      "order": 1
    }
  },
  "definitions": {
    "agent": {
      "type": "object",
      "title": "agent",
      "properties": {
        "active": {
          "type": "boolean",
          "title": "Active",
          "description": "True if the agent is active, false if the agent has been deactivated",
          "order": 30
        },
        "address": {
          "type": "string",
          "title": "Address",
          "description": "Address of the agent",
          "order": 12
        },
        "backgroundInformation": {
          "type": "string",
          "title": "Background Information",
          "description": "Background information of the agent",
          "order": 17
        },
        "canSeeAllTicketsFromAssociatedDepartments": {
          "type": "boolean",
          "title": "Can See All Tickets from Associated Departments",
          "description": "Set to true if the agent must be allowed to view tickets filed by other members of the department, and false otherwise",
          "order": 10
        },
        "createdAt": {
          "type": "string",
          "title": "Created At",
          "description": "Date and time when the agent was created",
          "order": 31
        },
        "customFields": {
          "type": "object",
          "title": "Custom Fields",
          "description": "Key-value pair containing the names and values of the (custom) agent fields",
          "order": 28
        },
        "departmentIds": {
          "type": "array",
          "title": "Department IDs",
          "description": "Unique IDs of the departments associated with the agent",
          "items": {
            "type": "string"
          },
          "order": 9
        },
        "email": {
          "type": "string",
          "title": "Email",
          "description": "Email address of the agent",
          "order": 6
        },
        "firstName": {
          "type": "string",
          "title": "First Name",
          "description": "First name of the agent",
          "order": 2
        },
        "hasLoggedIn": {
          "type": "boolean",
          "title": "Has Logged In",
          "description": "Set to true if the user has logged in to FreshService at least once, and false otherwise",
          "order": 29
        },
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "User ID of the agent",
          "order": 1
        },
        "jobTitle": {
          "type": "string",
          "title": "Job Title",
          "description": "Job title of the agent",
          "order": 5
        },
        "language": {
          "type": "string",
          "title": "Language",
          "description": "Language used by the agent",
          "order": 15
        },
        "lastActiveAt": {
          "type": "string",
          "title": "Last Active At",
          "description": "Timestamp of the agent's recent activity",
          "order": 27
        },
        "lastLoginAt": {
          "type": "string",
          "title": "Last Login At",
          "description": "Timestamp of the agent's last successful login",
          "order": 26
        },
        "lastName": {
          "type": "string",
          "title": "Last Name",
          "description": "Last name of the agent",
          "order": 3
        },
        "locationId": {
          "type": "integer",
          "title": "Location ID",
          "description": "Unique ID of the location associated with the agent",
          "order": 16
        },
        "memberOf": {
          "type": "array",
          "title": "Member Of",
          "description": "Unique IDs of the groups that the agent is a member of",
          "items": {
            "type": "integer"
          },
          "order": 20
        },
        "memberOfPendingApproval": {
          "type": "array",
          "title": "Member Of Pending Approval",
          "description": "Unique IDs of the restricted groups to which the agent's addition as a member is pending approval",
          "items": {
            "type": "integer"
          },
          "order": 22
        },
        "mobilePhoneNumber": {
          "type": "string",
          "title": "Mobile Phone Number",
          "description": "Mobile phone number of the agent",
          "order": 8
        },
        "observerOf": {
          "type": "array",
          "title": "Observer Of",
          "description": "Unique IDs of the groups that the agent is an observer of",
          "items": {
            "type": "integer"
          },
          "order": 21
        },
        "observerOfPendingApproval": {
          "type": "array",
          "title": "Observer Of Pending Approval",
          "description": "Unique IDs of the restricted groups to which the agent's addition as an observer is pending approval",
          "items": {
            "type": "integer"
          },
          "order": 23
        },
        "occasional": {
          "type": "boolean",
          "title": "Occasional",
          "description": "True if the agent is an occasional agent, and false if full-time agent",
          "order": 4
        },
        "reportingManagerId": {
          "type": "integer",
          "title": "Reporting Manager ID",
          "description": "User ID of the agent's reporting manager",
          "order": 11
        },
        "roles": {
          "type": "array",
          "title": "Roles",
          "description": "Roles that are granted to the agent",
          "items": {
            "$ref": "#/definitions/role"
          },
          "order": 24
        },
        "scopes": {
          "$ref": "#/definitions/scope",
          "title": "Scopes",
          "description": "Scopes of the agent",
          "order": 25
        },
        "scoreboardLevelId": {
          "type": "integer",
          "title": "Scoreboard Level ID",
          "description": "Unique ID of the level of the agent in the Arcade",
          "order": 18
        },
        "ticketScope": {
          "type": "string",
          "title": "Ticket Scope",
          "description": "Ticket scope of the agent",
          "order": 19
        },
        "timeFormat": {
          "type": "string",
          "title": "Time Format",
          "description": "Time format for the agent",
          "order": 14
        },
        "timeZone": {
          "type": "string",
          "title": "Time Zone",
          "description": "Time zone of the agent",
          "order": 13
        },
        "updatedAt": {
          "type": "string",
          "title": "Updated At",
          "description": "Date and time when the agent was last updated",
          "order": 32
        },
        "workPhoneNumber": {
          "type": "string",
          "title": "Work Phone Number",
          "description": "Work phone number of the agent",
          "order": 7
        }
      },
      "definitions": {
        "role": {
          "type": "object",
          "title": "role",
          "properties": {
            "assigmentScope": {
              "type": "string",
              "title": "Assignment Scope",
              "description": "The scope in which the agent can use the permissions granted by this role",
              "order": 2
            },
            "groups": {
              "type": "array",
              "title": "Groups",
              "description": "Unique IDs of Groups in which the permissions granted by the role applies",
              "items": {
                "type": "integer"
              },
              "order": 3
            },
            "roleId": {
              "type": "integer",
              "title": "Role ID",
              "description": "Unique ID of the role assigned",
              "order": 1
            }
          }
        },
        "scope": {
          "type": "object",
          "title": "scope",
          "properties": {
            "asset": {
              "type": "string",
              "title": "Asset",
              "description": "Asset scope of the agent",
              "order": 5
            },
            "change": {
              "type": "string",
              "title": "Change",
              "description": "Change scope of the agent",
              "order": 3
            },
            "contract": {
              "type": "string",
              "title": "Contract",
              "description": "Contract scope of the agent",
              "order": 7
            },
            "problem": {
              "type": "string",
              "title": "Problem",
              "description": "Problem scope of the agent",
              "order": 2
            },
            "release": {
              "type": "string",
              "title": "Release",
              "description": "Release scope of the agent",
              "order": 4
            },
            "solution": {
              "type": "string",
              "title": "Solution",
              "description": "Solution scope of the agent",
              "order": 6
            },
            "ticket": {
              "type": "string",
              "title": "Ticket",
              "description": "Ticket scope of the agent",
              "order": 1
            }
          }
        }
      }
    },
    "role": {
      "type": "object",
      "title": "role",
      "properties": {
        "assigmentScope": {
          "type": "string",
          "title": "Assignment Scope",
          "description": "The scope in which the agent can use the permissions granted by this role",
          "order": 2
        },
        "groups": {
          "type": "array",
          "title": "Groups",
          "description": "Unique IDs of Groups in which the permissions granted by the role applies",
          "items": {
            "type": "integer"
          },
          "order": 3
        },
        "roleId": {
          "type": "integer",
          "title": "Role ID",
          "description": "Unique ID of the role assigned",
          "order": 1
        }
      }
    },
    "scope": {
      "type": "object",
      "title": "scope",
      "properties": {
        "asset": {
          "type": "string",
          "title": "Asset",
          "description": "Asset scope of the agent",
          "order": 5
        },
        "change": {
          "type": "string",
          "title": "Change",
          "description": "Change scope of the agent",
          "order": 3
        },
        "contract": {
          "type": "string",
          "title": "Contract",
          "description": "Contract scope of the agent",
          "order": 7
        },
        "problem": {
          "type": "string",
          "title": "Problem",
          "description": "Problem scope of the agent",
          "order": 2
        },
        "release": {
          "type": "string",
          "title": "Release",
          "description": "Release scope of the agent",
          "order": 4
        },
        "solution": {
          "type": "string",
          "title": "Solution",
          "description": "Solution scope of the agent",
          "order": 6
        },
        "ticket": {
          "type": "string",
          "title": "Ticket",
          "description": "Ticket scope of the agent",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
