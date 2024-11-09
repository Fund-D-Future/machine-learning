from pydantic import BaseModel
from typing import List, Dict

class CampaignData(BaseModel):
    name: str
    description: str
    target_amount: float
    has_visuals: bool

class CampaignAnalysisResponse(BaseModel):
    score: int
    feedback: Dict[str, List[str]]
