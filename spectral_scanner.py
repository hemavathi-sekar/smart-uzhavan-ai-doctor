"""
Leaf Spectral Scanner & Computer Vision Engine
Simulates Multi-spectral imaging, NDVI vegetation index, Chlorophyll stress mapping,
and Necrosis spot detection for AgriTech diagnostics.
"""

import cv2
import numpy as np
from PIL import Image

def analyze_leaf_spectral(image_input):
    """
    Takes a PIL Image or numpy array of a leaf.
    Performs:
    1. Leaf segmentation (HSV mask to isolate leaf from background)
    2. Simulated NIR (Near-Infrared) & Red-Edge channel estimation
    3. NDVI (Normalized Difference Vegetation Index) stress heatmap
    4. Chlorophyll Absorption Index (CI_green) map
    5. Necrosis & Disease spot contour detection and damage percentage
    Returns:
    - dict of processed images (RGB, NDVI heatmap, Chlorophyll map, Lesion overlay)
    - quantitative metrics (% damage, chlorophyll score, health status)
    """
    if isinstance(image_input, Image.Image):
        img_rgb = np.array(image_input.convert("RGB"))
    else:
        img_rgb = image_input.copy()

    # Resize for consistent processing if very large
    h, w, _ = img_rgb.shape
    max_dim = 800
    if max(h, w) > max_dim:
        scale = max_dim / max(h, w)
        img_rgb = cv2.resize(img_rgb, (int(w * scale), int(h * scale)), interpolation=cv2.INTER_AREA)
        h, w, _ = img_rgb.shape

    img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

    # 1. Leaf Segmentation (Isolate leaf from non-plant background)
    hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
    # Range covering healthy green to diseased yellow/brown/dry tones
    lower_plant = np.array([15, 30, 30])
    upper_plant = np.array([90, 255, 255])
    plant_mask = cv2.inRange(hsv, lower_plant, upper_plant)

    # Clean mask morphology
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    plant_mask = cv2.morphologyEx(plant_mask, cv2.MORPH_OPEN, kernel, iterations=2)
    plant_mask = cv2.morphologyEx(plant_mask, cv2.MORPH_CLOSE, kernel, iterations=2)

    total_leaf_pixels = np.count_nonzero(plant_mask)
    if total_leaf_pixels < 500:
        # Fallback if leaf mask didn't catch (e.g. background non-standard), use full image
        plant_mask = np.ones((h, w), dtype=np.uint8) * 255
        total_leaf_pixels = h * w

    # 2. Simulated Spectral Decomposition (Red, Green, Blue, and Simulated NIR)
    # In vegetation science:
    # Chlorophyll absorbs strongly in Red (650-670nm) and Blue (450nm), reflects Green (550nm).
    # Healthy mesophyll cell structure strongly reflects NIR (750-900nm).
    # Diseased tissue collapses cell structures, reducing NIR and reducing green while increasing red reflection.
    r = img_rgb[:, :, 0].astype(np.float32)
    g = img_rgb[:, :, 1].astype(np.float32)
    b = img_rgb[:, :, 2].astype(np.float32)

    # Simulated NIR: combination of high green reflectance and luminance where chlorophyll is active
    # Healthy leaf has high Green and moderate Blue/Red.
    simulated_nir = np.clip(1.3 * g - 0.3 * r + 0.2 * b, 0, 255).astype(np.float32)

    # 3. NDVI Calculation: (NIR - Red) / (NIR + Red + epsilon)
    denominator = simulated_nir + r + 1e-6
    ndvi = (simulated_nir - r) / denominator
    ndvi = np.clip(ndvi, -1.0, 1.0)

    # Normalized NDVI to 0 - 255 for color mapping
    # Healthy tissue > 0.3, stressed 0.1 - 0.3, dead / necrotic < 0.1
    ndvi_scaled = ((ndvi + 1.0) / 2.0 * 255).astype(np.uint8)
    ndvi_masked = cv2.bitwise_and(ndvi_scaled, ndvi_scaled, mask=plant_mask)
    ndvi_colormap = cv2.applyColorMap(ndvi_masked, cv2.COLORMAP_JET)
    ndvi_colormap[plant_mask == 0] = [20, 20, 20] # Background dark

    # 4. Chlorophyll Stress Map (Green Chlorophyll Index)
    # CI_green = (NIR / Green) - 1
    ci_green = (simulated_nir / (g + 1e-6)) - 1.0
    ci_scaled = np.clip((ci_green + 0.5) / 2.0 * 255, 0, 255).astype(np.uint8)
    ci_colormap = cv2.applyColorMap(ci_scaled, cv2.COLORMAP_VIRIDIS)
    ci_colormap[plant_mask == 0] = [20, 20, 20]

    # 5. Lesion & Necrosis Spot Detection
    # Spots typically appear as dark brown, yellow halos, or grey necrosis
    # In HSV: Hue < 25 (yellow/orange/brown/red), or Saturation high & Value lower
    lesion_mask_1 = cv2.inRange(hsv, np.array([0, 40, 20]), np.array([28, 255, 200])) # Brown/yellow
    lesion_mask_2 = cv2.inRange(hsv, np.array([28, 50, 20]), np.array([45, 255, 180])) # Pale chlorotic yellow
    lesion_raw = cv2.bitwise_or(lesion_mask_1, lesion_mask_2)
    lesion_in_leaf = cv2.bitwise_and(lesion_raw, lesion_raw, mask=plant_mask)

    # Refine lesions with morphology
    lesion_cleaned = cv2.morphologyEx(lesion_in_leaf, cv2.MORPH_OPEN, kernel)
    lesion_pixels = np.count_nonzero(lesion_cleaned)

    # Damage Percentage
    damage_pct = (lesion_pixels / max(total_leaf_pixels, 1)) * 100.0
    damage_pct = round(min(damage_pct, 100.0), 1)

    # 6. Create Visual Inspection Overlay (Bounding boxes and contours on original leaf)
    overlay_img = img_rgb.copy()
    contours, _ = cv2.findContours(lesion_cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    spot_count = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 40: # Filter tiny pixel noise
            spot_count += 1
            # Draw contour in vibrant red/yellow
            cv2.drawContours(overlay_img, [cnt], -1, (255, 30, 30), 2)
            # Draw bounding box
            x, y, bw, bh = cv2.boundingRect(cnt)
            cv2.rectangle(overlay_img, (x, y), (x + bw, y + bh), (255, 215, 0), 1)

    # Average NDVI in valid leaf area
    leaf_ndvi_vals = ndvi[plant_mask > 0]
    avg_ndvi = float(np.mean(leaf_ndvi_vals)) if len(leaf_ndvi_vals) > 0 else 0.5
    chlorophyll_score = round(max(0.0, min(100.0, (avg_ndvi + 0.2) * 100.0)), 1)

    # Classify Health Stress Level
    if damage_pct < 4.0 and chlorophyll_score > 65.0:
        health_status = "Healthy (ஆரோக்கியமான இலை)"
        stress_level = "Low / Normal"
        badge_color = "green"
    elif damage_pct < 18.0:
        health_status = "Moderate Stress (இடைநிலை பூஞ்சாண தாக்குதல்)"
        stress_level = "Moderate"
        badge_color = "orange"
    else:
        health_status = "Severe Infestation (தீவிர பயிர் நோய் தாக்குதல்)"
        stress_level = "Critical"
        badge_color = "red"

    return {
        "images": {
            "original_rgb": Image.fromarray(img_rgb),
            "spectral_overlay": Image.fromarray(overlay_img),
            "ndvi_heatmap": Image.fromarray(cv2.cvtColor(ndvi_colormap, cv2.COLOR_BGR2RGB)),
            "chlorophyll_map": Image.fromarray(cv2.cvtColor(ci_colormap, cv2.COLOR_BGR2RGB))
        },
        "metrics": {
            "damage_percentage": damage_pct,
            "chlorophyll_index": chlorophyll_score,
            "avg_ndvi": round(avg_ndvi, 3),
            "spot_count": spot_count,
            "health_status": health_status,
            "stress_level": stress_level,
            "badge_color": badge_color
        }
    }
