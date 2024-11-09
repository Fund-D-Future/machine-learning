
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
                    "recommendation_title_1": {
                        "type": "string",
                        "description": "first Title of the improvement suggestion"
                    },
                    "recommendation_details_1": {
                        "type": "string",
                        "description": "first Detailed suggestion for improving the campaign"
                    },
                    "recommendation_title_2": {
                        "type": "string",
                        "description": "second first Title of the improvement suggestion"
                    },
                    "recommendation_details_2": {
                        "type": "string",
                        "description": "second Detailed suggestion for improving the campaign"
                    },
                    "recommendation_title_3": {
                        "type": "string",
                        "description": "third Title of the improvement suggestion"
                    },
                    "recommendation_details_3": {
                        "type": "string",
                        "description": "third Detailed suggestion for improving the campaign"
                    },
                    "recommendation_title_4": {
                        "type": "string",
                        "description": "fourth Title of the improvement suggestion"
                    },
                    "recommendation_details_4": {
                        "type": "string",
                        "description": "fourth Detailed suggestion for improving the campaign"
                    },
                
                },
            },
            "required": ["score", "recommendation_title_1", "recommendation_details_1", "recommendation_title_2", "recommendation_details_2", "recommendation_title_3", "recommendation_details_3", "recommendation_title_4", "recommendation_details_4"]
        },
        "instructions": system_prompt
    }
]
