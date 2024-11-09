
import os
from openai import OpenAI
from dto import CampaignData

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))    

def get_function_response(data: CampaignData, function_object, tool_choice = "auto", model = "gpt-4o-mini"):
  prompt = f"""
    Analyze the following crowdfunding campaign details and provide a score out of 100. 
    Additionally, suggest areas of improvement with headings and subheadings:

    Campaign Name: {data.name}
    Description: {data.description}
    Target Amount: ${data.target_amount}
    Includes Visuals: {"Yes" if data.has_visuals else "No"}
    """
  print(f'''{data.description}
    Score: {function_object}
        ''')
  print(os.environ.get("OPENAI_API_KEY"))
  print(client)
  try:
    response = client.chat.completions.create(
        model = model,
        messages = [{"role": "user", "content": prompt}],
        temperature = 1,
        tools = function_object,
        tool_choice = tool_choice
    )
    if(response.choices[0].message.tool_calls):
        print(response)
        result = response.choices[0].message.tool_calls[0].function.arguments
    else:
        result = response.choices[0].message.content

    new_result = ""
    for letter in result:
        if letter != "\\":
            new_result += letter
    return new_result
  except Exception as e:
      return f"Error occurred while analyzing: {e}"