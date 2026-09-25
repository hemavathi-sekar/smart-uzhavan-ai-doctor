import sys
import os
from PIL import Image
from uzhavan_ai import analyze_crop_with_gemini

if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding='utf-8')

img_path = os.path.join(os.path.dirname(__file__), "sample_data", "user_banana_specimen.png")
img = Image.open(img_path)

# Test with crop_hint="auto_detect" and no API key (offline)
res = analyze_crop_with_gemini(img, crop_hint="auto_detect", api_key=None)

print("🎯 DIAGNOSIS RESULTS:")
print(f"Detected Plant: {res['crop_name_ta']}")
print(f"Detected Disease: {res['disease_name_ta']}")
print(f"Confidence: {res['confidence_score']}")
print(f"Audio Script: {res['audio_script_ta'][:100]}...")
print(f"Audio Bytes Size: {len(res['audio_bytes'])} bytes")
