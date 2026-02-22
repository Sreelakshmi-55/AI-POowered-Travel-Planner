import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_plan(destination, days, weather, context, budget, mood):

    prompt = f"""
    You are an expert AI travel planner.

    Destination: {destination}
    Number of Days: {days}
    Budget Level: {budget}
    Travel Mood: {mood}

    Current Weather:
    {weather}

    Travel Knowledge:
    {context}

    Instructions:
    - Adjust activities based on weather.
    - Suggest hotels and restaurants based on budget.
    - Align activities with travel mood.
    - Provide detailed day-by-day itinerary.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content