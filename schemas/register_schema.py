register_success = {
  "type": "object",
  "additionalProperties": False,
  "properties": {
    "id": {
      "type": "integer"
    },
    "token": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "token"
  ]
}

register_unsuccess = {
  "type": "object",
  "properties": {
    "error": {
      "type": "string"
    }
  },
  "required": [
    "error"
  ]
}