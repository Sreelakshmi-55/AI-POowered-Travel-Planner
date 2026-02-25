import streamlit as st
from rag import setup_rag, retrieve_context
from weather import get_weather
from llm import generate_plan

st.set_page_config(page_title="AI Travel Planner", page_icon="🌍",layout="wide")

st.markdown("""
<div style='text-align: center; padding: 20px 0;'>
    <h1>🌍 AI Adaptive Travel Planner</h1>
    <p style='font-size:18px;'>Plan your perfect trip with real-time weather insights and AI-generated itineraries.</p>
</div>
""", unsafe_allow_html=True)
st.markdown("""
<style>
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        padding: 10px 24px;
    }
            
</style>
""", unsafe_allow_html=True)

st.markdown("---")


@st.cache_resource
def load_vectorstore():
    return setup_rag()

vectorstore = load_vectorstore()

st.markdown("## ✈️ Plan Your Trip")

col1, col2 = st.columns(2)

with col1:
    destination = st.text_input("📍 Enter Destination")
    days = st.number_input("📅 Number of Days", min_value=1, max_value=14, value=3)

with col2:
    budget = st.selectbox(
        "💰 Select Budget Level",
        ["Low", "Medium", "High"]
    )

    mood = st.selectbox(
        "🎯 Select Travel Mood",
        ["Relaxing", "Adventure", "Romantic", "Family", "Solo"]
    )

st.markdown("###")
generate = st.button("✨ Generate Travel Plan")

if generate:

    if not destination:
        st.warning("Please enter a destination.")
    else:

        with st.spinner("Planning your trip..."):
          try:
            weather = get_weather(destination)
          except Exception:
            weather = "Weather information unavailable."
          try:
            context = retrieve_context(vectorstore, destination)
          except Exception:
            context = "No additional travel context available."
          try:
            plan = generate_plan(
                destination,
                days,
                weather,
                context,
                budget,
                mood
            )
          except Exception:
             plan = "Unable to generate travel plan at the moment."
             
        st.markdown("---")
        st.markdown("## 🗺️ Your Travel Plan")
        colA, colB = st.columns([2, 1])
        with colA:
            st.markdown("### 📖 Itinerary")
            st.markdown(plan)
        with colB:
            st.markdown("### 💰 Estimated Budget")
            budget_costs = {
             "Low": 60,
             "Medium": 150,
             "High": 350
             }
            estimated_cost = budget_costs[budget] * days
            st.success(f"Approximate Total Cost: ${estimated_cost}")
            st.markdown("### 🌤️ Weather Info")
            st.info(weather)







