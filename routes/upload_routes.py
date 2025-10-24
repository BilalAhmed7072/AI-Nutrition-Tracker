from flask import Blueprint, request, jsonify
from ml.recognition import predict_food
from ml.nutrition import get_nutrition
import os

upload_bp = Blueprint("upload", __name__)

@upload_bp.route("/upload", methods=["POST"])
def upload_food():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    image = request.files["image"]
    tmp_path = "temp_upload.jpg"
    image.save(tmp_path)

    try:
        food = predict_food(tmp_path)
    except Exception as e:
        return jsonify({"error": f"Food recognition failed: {str(e)}"}), 500

    try:
        nutrition = get_nutrition(food)
    except Exception as e:
        nutrition = {"error": "Nutrition lookup failed", "details": str(e)}

    try:
        os.remove(tmp_path)
    except Exception:
        pass

    return jsonify({"food": food, "nutrition": nutrition})
