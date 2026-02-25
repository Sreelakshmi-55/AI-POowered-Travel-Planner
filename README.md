# AI-Powered-Travel-Planner
The AI-Powered Travel Planner is an intelligent travel assistant that generates personalized, structured travel itineraries based on user inputs such as destination, duration, budget, and interests.

This project leverages:
* Large Language Models (LLMs) for itinerary generation
* Retrieval-Augmented Generation (RAG) for context-aware responses
* Real-time weather data
* Streamlit for user interaction

The goal is to build a smart system that produces reliable, personalized, and data-grounded travel plans instead of generic recommendations.
The system combines Retrieval-Augmented Generation (RAG) with Large Language Models (LLMs) to produce structured, accurate, and context-aware travel plans.
Instead of relying only on generative AI, the system retrieves relevant travel information from a structured knowledge base and uses it to generate grounded and personalized itineraries.

## Aim

To design and implement an intelligent travel planning system that integrates semantic search with large language models to generate reliable and customized travel itineraries.

## Objectives

* Generate personalized travel itineraries
* Incorporate weather-aware recommendations
* Suggest attractions, accommodations, and cuisines
* Provide budget-based cost estimation
* Reduce hallucination through Retrieval-Augmented Generation
* Provide structured, day-wise travel planning
* Optimize token usage for multi-day plans

## Problem Statement

Traditional travel platforms often:
* Provide generic recommendations
* Lack structured day-wise planning
* Require users to browse multiple websites
* Do not adapt well to user preferences

Additionally, standalone LLM-based systems may hallucinate travel details such as hotels or pricing.

This project addresses these issues by integrating:
* Structured retrieval (RAG)
* Real-time weather data
* Controlled prompt engineering
* Cost estimation logic

## Technologies Used

Programming Language: Python

Frontend: Streamlit

LLM: LLaMA 3.1 (via Groq API)

Retrieval System:

* Structured text knowledge base (cities.txt)

* Semantic retrieval logic

External API: Weather API (real-time weather data)

AI Technique: Retrieval-Augmented Generation (RAG)

## Conclusion

The AI-Powered Travel Planner demonstrates how Retrieval-Augmented Generation can enhance large language models to build reliable, personalized, and structured travel planning systems.

This project showcases the integration of AI, NLP, and vector databases to develop a practical, real-world intelligent assistant.
