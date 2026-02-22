import streamlit as st
from rag import setup_rag, retrieve_context
from weather import get_weather
from llm import generate_plan

st.set_page_config(page_title="AI Travel Planner", page_icon="🌍")

st.title("🌍 AI Adaptive Travel Planner")

@st.cache_resource
def load_vectorstore():
    return setup_rag()

vectorstore = load_vectorstore()

destination = st.text_input("Enter Destination")

days = st.number_input("Number of Days", min_value=1, max_value=14, value=3)

budget = st.selectbox(
    "Select Budget Level",
    ["Low", "Medium", "High"]
)

mood = st.selectbox(
    "Select Travel Mood",
    ["Relaxing", "Adventure", "Romantic", "Family", "Solo"]
)

if st.button("Generate Travel Plan"):

    if not destination:
        st.warning("Please enter a destination.")
    else:

        with st.spinner("Planning your trip..."):

            weather = get_weather(destination)

            context = retrieve_context(vectorstore, destination)

            plan = generate_plan(
                destination,
                days,
                weather,
                context,
                budget,
                mood
            )

        st.subheader("Your Travel Itinerary")
        st.write(plan)

        budget_costs = {
            "Low": 60,
            "Medium": 150,
            "High": 350
        }

        estimated_cost = budget_costs[budget] * days

        st.subheader("Estimated Budget")
        st.success(f"Approximate Total Cost: ${estimated_cost}")

        st.subheader("Weather Info")
        st.info(weather)