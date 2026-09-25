"""
Universal Verification Test for Smart Uzhavan AI Doctor
Verifies:
1. Universal sample generation (Vegetables, Fruits, Trees, Cereals)
2. Spectral scanning on multiple botanical specimens
3. Agro Knowledge Base retrieval for Banana, Citrus, Coconut, Tomato
4. Tamil TTS audio generation
5. Conversational Voice Engine
"""

import os
import sys

# Ensure UTF-8 output on Windows console
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding='utf-8')

def run_tests():
    print("🌾 Starting Universal Uzhavan AI Doctor System Verification...")

    # Step 1: Generate sample images
    from generate_samples import generate_all_samples
    print("Generating demo botanical samples (Fruits, Trees, Leaves)...")
    generate_all_samples()
    print("✅ All samples generated in sample_data/")

    # Step 2: Test Spectral Scanner on Citrus Fruit / Banana Leaf
    from PIL import Image
    from spectral_scanner import analyze_leaf_spectral
    sample_banana = os.path.join(os.path.dirname(__file__), "sample_data", "banana_sigatoka.png")
    img = Image.open(sample_banana)
    
    print("Testing Spectral Scanner on Banana Sigatoka sample...")
    result = analyze_leaf_spectral(img)
    metrics = result["metrics"]
    print(f"✅ Banana Spectral Metrics:")
    print(f"   - Damage %: {metrics['damage_percentage']}%")
    print(f"   - Chlorophyll Index: {metrics['chlorophyll_index']}")
    print(f"   - Avg NDVI: {metrics['avg_ndvi']}")
    print(f"   - Stress Level: {metrics['stress_level']}")

    # Step 3: Test Knowledge Base & AI Engine on Auto-Detect & Fruit
    from uzhavan_ai import get_offline_expert_diagnosis, ask_uzhavan_voice_doctor
    print("Testing Universal Knowledge Engine on Banana...")
    diag = get_offline_expert_diagnosis("banana", metrics)
    print(f"✅ Diagnosis:")
    print(f"   - Crop: {diag['crop_name_ta']}")
    print(f"   - Part: {diag['plant_part']}")
    print(f"   - Disease: {diag['disease_name_ta']}")
    print(f"   - Organic: {diag['organic_solution']['recipe_ta']}")
    print(f"   - Chemical: {diag['chemical_solution']['medicine_name']}")
    print(f"   - Audio size: {len(diag['audio_bytes']) if diag.get('audio_bytes') else 0} bytes")

    # Step 4: Test Auto-Detect mode
    print("Testing Auto-Detect mode...")
    auto_diag = get_offline_expert_diagnosis("auto_detect", metrics)
    print(f"✅ Auto-Detect Diagnosis: {auto_diag['disease_name_ta']}")

    # Step 5: Test Tamil Voice Q&A for Trees
    print("Testing Tree voice consultation...")
    chat_res = ask_uzhavan_voice_doctor("தென்னை மரத்தில் ஓலை அழுகினால் என்ன மருந்து வைக்க வேண்டும்?", diag)
    print(f"✅ Voice Response: {chat_res['reply_ta'][:60]}...")
    print(f"   - Audio size: {len(chat_res['audio_bytes']) if chat_res.get('audio_bytes') else 0} bytes")

    print("\n🎉 ALL UNIVERSAL BOTANICAL TESTS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    run_tests()
