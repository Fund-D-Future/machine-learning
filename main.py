from fastapi import FastAPI
from dto import CampaignData, CampaignAnalysisResponse
from services.analyzer import analyze_campaign

app = FastAPI()

@app.post("/analyze_campaign", response_model=CampaignAnalysisResponse)
async def analyze_campaign_endpoint(data: CampaignData):
    result = await analyze_campaign(data)
    return result
