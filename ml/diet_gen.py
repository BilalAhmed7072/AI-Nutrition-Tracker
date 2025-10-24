import os
import google.generativeai as genai
from config.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY or os.getenv("GEMINI_API_KEY"))

def calculate_bmr(gender, weight, height, age):
    if gender and gender.lower().startswith("m"):
        return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        return 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

activity_factors = {
    "sedentary": 1.2,
    "light": 1.375,
    "moderate": 1.55,
    "active": 1.725,
    "very_active": 1.9
}

def estimate_target_calories(profile: dict):
    try:
        weight = profile.get("weight_kg") or profile.get("weight") or 70
        height = profile.get("height_cm") or profile.get("height") or 170
        age = profile.get("age") or 30
        gender = profile.get("gender") or "male"
        bmr = calculate_bmr(gender, weight, height, age)
        activity = activity_factors.get(profile.get("activity_level", "moderate"), 1.55)
        maintenance = bmr * activity
        goal = profile.get("goal", "maintenance")
        if goal == "weight_loss":
            return max(1200, int(maintenance - 500))
        elif goal == "weight_gain":
            return int(maintenance + 500)
        else:
            return int(maintenance)
    except Exception:
        return 2000

def generate_personalized_diet(profile: dict, eaten_today: list, target_calories: int = None) -> str:
    if target_calories is None:
        target_calories = estimate_target_calories(profile)

    prompt = f"""
You are a certified nutritionist. Create a concise one-day meal plan for the user below.

User profile:
{profile}

Target daily calories: {int(target_calories)} kcal
Already eaten today: {eaten_today}

Provide:
- Breakfast, lunch, dinner, and 1-2 snacks
- Approx calories per meal and macronutrient grams (protein/carbs/fat)
- Quick swap options for preferences/allergies

Be concise and actionable.
"""

    model = genai.GenerativeModel("gemini-1.5-flash")
    resp = model.generate_content(prompt)
    return resp.text
