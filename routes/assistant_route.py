from flask import Blueprint, request, jsonify
from ml.rag import get_rag_response
from ml.diet_gen import generate_personalized_diet, estimate_target_calories
from google.generativeai import GenerativeModel
import os

assistant_bp = Blueprint("assistant", __name__)

def detect_intent(query):
    """
    Uses Gemini model to classify the user's query into an intent.
    Possible intents:
      - diet_plan
      - nutrition_info
      - health_advice
      - general_query
    """
    model = GenerativeModel("gemini-1.5-flash")
    prompt = f"""
    You are an intent classification model for a nutrition and health assistant.
    Classify the following query into ONE of these intents:
    - diet_plan (for meal, diet, calories, nutrition plans, etc.)
    - nutrition_info (for asking about nutrients, food items, or ingredient values)
    - health_advice (for fitness, exercise, disease, or general well-being questions)
    - general_query (for small talk or non-health related queries)

    Query: "{query}"

    Respond with only one intent name, nothing else.
    """
    try:
        resp = model.generate_content(prompt)
        intent = resp.text.strip().lower()
        return intent
    except Exception as e:
        print("Intent detection failed:", e)
        return "general_query"


@assistant_bp.route("/assistant", methods=["POST"])
def assistant():
    data = request.get_json() or {}
    query = data.get("query", "")
    profile = data.get("profile", {})
    eaten = data.get("eaten", [])

    if not query:
        return jsonify({"error": "Query is required"}), 400

    intent = detect_intent(query)
    print(f"[Intent Detected] {intent}")

    if intent == "diet_plan":
        target_calories = data.get("target_calories") or estimate_target_calories(profile)
        answer = generate_personalized_diet(profile, eaten, target_calories)
        return jsonify({"answer": answer})

    elif intent in ["nutrition_info", "health_advice"]:
        try:
            answer = get_rag_response(query, k=4)
        except Exception as e:
            print("RAG failed:", e)
            answer = "Sorry, I couldn’t retrieve health information right now."
        return jsonify({"answer": answer})

    else:  
        try:
            model = GenerativeModel("gemini-1.5-flash")
            fallback_prompt = f"You are a friendly AI health assistant.\nUser: {query}"
            resp = model.generate_content(fallback_prompt)
            answer = resp.text
        except Exception as e:
            answer = "I'm having trouble generating a response right now."

        return jsonify({"answer": answer})
