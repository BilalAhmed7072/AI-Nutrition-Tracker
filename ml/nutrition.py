import requests
from config.config import EDAMAM_APP_ID, EDAMAM_APP_KEY, NUTRITIONIX_APP_ID, NUTRITIONIX_APP_KEY
def get_nutrition_edamam(food_name: str) -> dict:
    url = "https://api.edamam.com/api/nutrition-data"
    params = {
        "app_id": EDAMAM_APP_ID,
        "app_key": EDAMAM_APP_KEY,
        "ingr": food_name
    }
    res = requests.get(url, params=params, timeout=10)
    res.raise_for_status()
    data = res.json()
    return {
        "food": food_name,
        "calories": data.get("calories", 0),
        "totalWeight": data.get("totalWeight", 0),
        "macros": data.get("totalNutrients", {})
    }

def get_nutrition(food_name: str) -> dict:
    try:
        return get_nutrition_edamam(food_name)
    except Exception:
        return {"food": food_name, "calories": 0, "error": "Nutrition lookup failed"}
