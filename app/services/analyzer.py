
import os
from openai import OpenAI
from dto import CampaignData
from IPython.display import Markdown
import json


client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))    

def get_function_response(data: CampaignData, function_object, tool_choice = "required", model = "gpt-4o-mini"):
  prompt = f"""
    Analyze the following crowdfunding campaign details and provide a score out of 100. 
    Additionally, suggest areas of improvement with headings and subheadings:
    Note: Only provide recommendations based on these information only.

    Campaign Name: {data.name}
    Description: {data.description}
    Target Amount: ${data.target_amount}
    Includes Visuals: {"Yes" if data.has_visuals else "No"}
    """

  try:
    response = client.chat.completions.create(
        model = model,
        messages = [{"role": "user", "content": prompt}],
        temperature = 1,
        tools = function_object,
        tool_choice = tool_choice
    )
    if(response.choices[0].message.tool_calls):
        result = response.choices[0].message.tool_calls[0].function.arguments
    else:
        result = response.choices[0].message.content

    try:
      result_json = json.loads(result)
    except json.JSONDecodeError:
        # If it's not already JSON, structure it manually
      result_json = {
                "score": None,
                "improvements": result
            }

    return result_json  
  except Exception as e:
      return f"Error occurred while analyzing: {e}"