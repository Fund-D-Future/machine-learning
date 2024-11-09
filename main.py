# main.py
from fastapi import FastAPI
from dto import CampaignData
from services.analyzer import get_function_response
from utils.constants import function_object


app = FastAPI(
    title="Fund The Future Campaign Analyzer",
    description="API to analyze crowdfunding campaigns and provide feedback.",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Fund The Future Campaign Analyzer API!",
        "documentation": "<a href='http://127.0.0.1:8000/docs'>API Documentation</a>"
    }

# Endpoint for analyzing campaigns
@app.post("/analyze_campaign")
async def analyze_campaign(data:CampaignData):
    try:
        return get_function_response(data, function_object)
    except Exception as e:
        return {str(e)}