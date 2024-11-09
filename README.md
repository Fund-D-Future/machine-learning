# Fundd Fute Campaign Analyzer

Fundd Fute Campaign Analyzer is a FastAPI application that helps analyze the strength of a crowdfunding campaign based on provided data. It evaluates campaigns and gives a score (out of 100) for the likelihood of getting funded, along with actionable feedback on how to improve various aspects of the campaign.

## Features

- **Campaign Score Calculation**: Generates a score based on factors like the campaign name, description, target amount, and visuals.
- **Detailed Feedback**: Provides specific topics and subtopics for improvement to increase the chances of funding.
- **Modular Structure**: Organized code with separate files for DTOs, prompts, and analysis services for maintainability.

## Installation

### Prerequisites

- **Python 3.8+**
- **OpenAI API Key** (for accessing GPT-4 via LangChain)

### Step 1: Clone the Repository

git clone https://github.com/yourusername/fundd-fute-campaign-analyzer.git
cd fundd-fute-campaign-analyzer

## Step 2: Set Up a Virtual Environment
It's recommended to use a virtual environment to manage dependencies.

`python -m venv venv`
source venv/bin/activate  # On Windows: venv\Scripts\activate
