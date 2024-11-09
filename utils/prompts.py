from dto import CampaignData

def generate_analysis_prompt(data: CampaignData) -> str:
    return f"""
    Analyze the following crowdfunding campaign based on its components. Provide a score out of 100 for the likelihood of getting funded, and offer specific feedback on improvement areas.

    Campaign Name: {data.name}
    Description: {data.description}
    Target Amount: ${data.target_amount}
    Has Visuals: {"Yes" if data.has_visuals else "No"}

    Provide a score and detailed feedback, with topics and subtopics for improvement.
    """
