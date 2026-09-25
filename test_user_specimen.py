import sys
import os
from PIL import Image
from botanical_classifier import classify_plant_and_disease_offline

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding='utf-8')

img_path = os.path.join(os.path.dirname(__file__), "sample_data", "user_banana_specimen.png")
if os.path.exists(img_path):
    res = classify_plant_and_disease_offline(Image.open(img_path))
    print("🎯 RESULTS ON USER SPECIMEN:")
    print(f"Predicted Plant: {res['plant']}")
    print(f"Predicted Disease: {res['disease']}")
    print(f"Confidence: {res['confidence']*100:.1f}%")
    print(f"Justification: {res['justification']}")
else:
    print("Sample not found:", img_path)
