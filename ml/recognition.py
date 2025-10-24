from PIL import Image
from transformers import ViTFeatureExtractor, ViTForImageClassification
import torch
MODEL_NAME = "nateraw/food"

feature_extractor = ViTFeatureExtractor.from_pretrained(MODEL_NAME)
model = ViTForImageClassification.from_pretrained(MODEL_NAME)

def predict_food(image_path: str) -> str:
    image = Image.open(image_path).convert("RGB")
    inputs = feature_extractor(images=image, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
    idx = int(probs.argmax().item())
    label = model.config.id2label[idx]
    return label
