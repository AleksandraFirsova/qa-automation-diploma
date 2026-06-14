auth_success_schema = {
    "type": "object",
    "properties": {
        "token": {
            "type": "string"
        }
    },
    "required": ["token"],
    "additionalProperties": False
}

auth_error_schema = {
    "type": "object",
    "properties": {
        "reason": {
            "type": "string"
        }
    },
    "required": ["reason"],
    "additionalProperties": False
}
