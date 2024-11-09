from pydantic import BaseModel

class CampaignData(BaseModel):
    name: str
    description: str
    target_amount: float
    has_visuals: bool

