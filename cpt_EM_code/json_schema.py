
PROBLEM_SCHEMA = {
    "type": "json_schema",
    "json_schema": {
    "name": "soap",
    "strict": False,
    "schema":{
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            "section": {
            "type": "string"
            },
            "questions": {
            "type": "object",
            "patternProperties": {
                "^[0-9]+$": {
                "type": "object",
                "properties": {
                    "id": {
                    "type": "integer"
                    },
                    "question": {
                    "type": "string"
                    },
                    "answer": {
                    "type": "string"
                    },
                    "explanation": {
                    "type": "string"
                    }
                },
                "required": [
                    "id",
                    "question",
                    "answer",
                    "explanation"
                ],
                "additionalProperties": False
                }
            },
            "additionalProperties": False
            }
        },
        "required": ["section", "questions"],
        "additionalProperties": False
        }
    }
}

DATA_SCHEMA = {
    "type": "json_schema",
    "json_schema": {
    "name": "soap",
    "strict": False,
    "schema":{
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            "section": {
            "type": "string"
            },
            "questions": {
            "type": "object",
            "patternProperties": {
                "^[0-9]+$": {
                "type": "object",
                "properties": {
                    "id": {
                    "type": "integer"
                    },
                    "question": {
                    "type": "string"
                    },
                    "answer": {
                    "type": "string"
                    },
                    "explanation": {
                    "type": "string"
                    }
                },
                "required": ["id", "question", "answer", "explanation"],
                "additionalProperties": False
                }
            },
            "additionalProperties": False
            }
        },
        "required": ["section", "questions"],
        "additionalProperties": False
        }
    }
}



RISK_SCHEMA = {
    "type": "json_schema",
    "json_schema": {
    "name": "soap",
    "strict": False,
    "schema":{
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            "section": {
            "type": "string"
            },
            "questions": {
            "type": "object",
            "patternProperties": {
                "^[0-9]+$": {
                "type": "object",
                "properties": {
                    "id": {
                    "type": "integer"
                    },
                    "question": {
                    "type": "string"
                    },
                    "question description": {
                    "type": "string",
                    "description": "An optional field providing additional details about the question."
                    },
                    "answer": {
                    "type": "string"
                    },
                    "explanation": {
                    "type": "string"
                    }
                },
                "required": ["id", "question", "answer", "explanation"],
                "additionalProperties": False
                }
            },
            "additionalProperties": False
            }
        },
        "required": ["section", "questions"],
        "additionalProperties": False
        }
    }
}

REASON_SCHEMA = {
    "type": "json_schema",
    "json_schema": {
    "name": "soap",
    "strict": False,
    "schema":{
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            "reasoning": {
            "type": "string"
            }
        },
        "required": ["reasoning"],
        "additionalProperties": False
        }
    }
}