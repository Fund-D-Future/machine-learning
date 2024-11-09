from dto import CampaignData, CampaignAnalysisResponse
from utils.prompts import generate_analysis_prompt
from langchain.llms import OpenAI
import os

# Initialize the OpenAI API (you'll need to replace "YOUR_OPENAI_API_KEY")
llm = OpenAI(api_key="YOUR_OPENAI_API_KEY")

async def analyze_campaign(data: CampaignData) -> CampaignAnalysisResponse:
    # Generate the prompt based on the campaign data
    prompt = generate_analysis_prompt(data)
    
    # Call the LLM to analyze the prompt
    response = llm(prompt)
    
    # Example of parsing response - customize as needed based on OpenAI's actual response structure
    # Assuming response contains 'score' and 'feedback' as fields
    score = int(response.get("score", 0))  # Extracted score from the response
    feedback = response.get("feedback", {})

    return CampaignAnalysisResponse(score=score, feedback=feedback)
