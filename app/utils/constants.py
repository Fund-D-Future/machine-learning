
system_prompt = "Analyze crowdfunding campaign details and return a score and suggestions for improvement, Analyzes the campaign details and returns a structured response with a score out of 100 and improvement recommendations. include as much recommendation title and recommentdation details as you see. make sure the suggestions are up to 3 or 4. If you do not have any information, let the user know and let them input it before they continue. dont make one up"
# Define the function schema

function_object = [
    {
        "type": "function",
        "function": {
            "name": "campaign_scoring_details",
            "parameters": {
                "type": "object",
                "properties": {
                    "score": {
                        "type": "integer",
                        "description": "Score of the campaign on a scale of 0 to 100"
                    },
                    "recommendations": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "title": {
                                    "type": "string",
                                    "description": "Title of the improvement suggestion"
                                },
                                "suggestion": {
                                    "type": "string",
                                    "description": "Detailed suggestion for improving the campaign"
                                }
                            },
                            "required": ["title", "suggestion"]
                        },
                        "description": "List of improvement suggestions for the campaign"
                    }
                },
                "required": ["score", "recommendations"]
            }
        },
        "instructions": system_prompt
    }
]
