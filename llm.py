import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

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
    - Provide a detailed day-by-day itinerary.
    - Format output clearly using headings:
      Day 1:
      Morning:
      Afternoon:
      Evening:
    - Keep response clean and structured.

    """
    try:
      response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a professional travel planner."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=800
       )

      return response.choices[0].message.content
    
    except Exception as e:
      return f"Error generating travel plan: {str(e)}"