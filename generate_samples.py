"""
Universal Sample Leaf, Fruit & Tree Generator for Instant Demos
Creates realistic specimens across Vegetables, Fruits, Trees, and Cash Crops:
1. Tomato Early Blight (தக்காளி கருகல்)
2. Paddy Blast (நெல் குலை நோய்)
3. Paddy Bacterial Blight (நெல் பாக்டீரியா கருகல்)
4. Banana Sigatoka Leaf Spot (வாழை சிகடோகா இலைப்புள்ளி)
5. Mango Anthracnose Spot (மாமரம் ஆந்த்ராக்னோஸ்)
6. Citrus Lemon Canker (எலுமிச்சை கேங்கர் சொறி நோய்)
7. Brinjal Fruit/Shoot Borer (கத்தரிக்காய் காய் புழு)
8. Coconut Leaf Rot (தென்னை ஓலை அழுகல்)
9. Healthy Specimen (ஆரோக்கியமான இலை)
"""

import os
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

def create_botanical_sample(width=400, height=400, specimen_type="tomato", condition="early_blight"):
    img = Image.new("RGB", (width, height), (245, 245, 240))
    draw = ImageDraw.Draw(img)
    cx, cy = width // 2, height // 2

    if specimen_type == "banana":
        # Broad elongated tropical banana leaf
        points = []
        for y in range(30, height - 30):
            t = (y - 30) / (height - 60)
            w = 80 * math.sin(t * math.pi)
            points.append((cx - w, y))
        for y in range(height - 31, 29, -1):
            t = (y - 30) / (height - 60)
            w = 80 * math.sin(t * math.pi)
            points.append((cx + w, y))
        draw.polygon(points, fill=(65, 145, 45))
        # Midrib
        draw.line([(cx, 30), (cx, height - 30)], fill=(130, 200, 95), width=8)
        # Parallel lateral veins
        for y in range(50, height - 50, 20):
            draw.line([(cx, y), (cx - 75, y + 10)], fill=(80, 160, 60), width=2)
            draw.line([(cx, y), (cx + 75, y + 10)], fill=(80, 160, 60), width=2)
        # Sigatoka spindle spots
        for sy in [cy - 80, cy - 20, cy + 50, cy + 90]:
            # Elliptical brown lesions with yellow halo
            draw.ellipse([cx - 55, sy - 12, cx - 20, sy + 12], fill=(195, 175, 40))
            draw.ellipse([cx - 50, sy - 8, cx - 25, sy + 8], fill=(90, 45, 15))
            draw.ellipse([cx - 42, sy - 4, cx - 32, sy + 4], fill=(180, 180, 170)) # Grey center
            # Right side spots
            draw.ellipse([cx + 25, sy + 10, cx + 60, sy + 34], fill=(195, 175, 40))
            draw.ellipse([cx + 30, sy + 14, cx + 55, sy + 30], fill=(90, 45, 15))

    elif specimen_type == "citrus":
        # Lemon fruit with Canker crusty lesions
        # Draw Lemon shape (Yellow ovate with small tip)
        draw.ellipse([cx - 95, cy - 120, cx + 95, cy + 120], fill=(245, 215, 40))
        # Small lemon mammilla / tip
        draw.polygon([(cx, cy - 135), (cx - 15, cy - 118), (cx + 15, cy - 118)], fill=(230, 200, 35))
        draw.polygon([(cx, cy + 135), (cx - 15, cy + 118), (cx + 15, cy + 118)], fill=(230, 200, 35))
        # Citrus Canker lesions (raised corky crater-like dark brown scabs with oily yellow halos)
        spots = [(cx - 35, cy - 40, 18), (cx + 40, cy - 10, 22), (cx - 15, cy + 45, 16), (cx + 30, cy + 60, 14)]
        for sx, sy, r in spots:
            draw.ellipse([sx - r - 6, sy - r - 6, sx + r + 6, sy + r + 6], fill=(210, 180, 20)) # Halo
            draw.ellipse([sx - r, sy - r, sx + r, sy + r], fill=(95, 55, 20)) # Outer scab
            draw.ellipse([sx - r + 4, sy - r + 4, sx + r - 4, sy + r - 4], fill=(60, 30, 10)) # Crater

    elif specimen_type == "mango":
        # Mango leaf with Anthracnose
        points = []
        for y in range(35, height - 35):
            t = (y - 35) / (height - 70)
            w = 55 * math.sin(t * math.pi)
            points.append((cx - w, y))
        for y in range(height - 36, 34, -1):
            t = (y - 35) / (height - 70)
            w = 55 * math.sin(t * math.pi)
            points.append((cx + w, y))
        draw.polygon(points, fill=(50, 115, 40))
        # Midrib
        draw.line([(cx, 35), (cx, height - 35)], fill=(110, 175, 80), width=5)
        # Anthracnose black tar-spots and necrotic leaf edges
        for sy in [cy - 90, cy - 30, cy + 40]:
            draw.ellipse([cx - 40, sy, cx - 10, sy + 25], fill=(40, 25, 15))
            draw.ellipse([cx + 10, sy + 20, cx + 38, sy + 45], fill=(35, 20, 10))
        # Edge burn
        draw.polygon([(cx - 48, cy), (cx - 52, cy + 60), (cx - 38, cy + 40)], fill=(70, 35, 15))

    elif specimen_type == "coconut":
        # Coconut frond spear leaflet
        draw.polygon([(cx - 20, 30), (cx + 20, 30), (cx + 35, height - 40), (cx - 35, height - 40)], fill=(60, 130, 40))
        draw.line([(cx, 30), (cx, height - 40)], fill=(120, 180, 70), width=6)
        # Leaf rot distal shrivelling
        draw.polygon([(cx - 22, 30), (cx + 22, 30), (cx + 28, 130), (cx - 28, 130)], fill=(45, 25, 15))
        draw.line([(cx - 30, 130), (cx + 30, 130)], fill=(180, 140, 40), width=3)

    elif specimen_type == "rice":
        points = []
        for y in range(40, height - 40):
            t = (y - 40) / (height - 80)
            w = 32 * math.sin(t * math.pi)
            points.append((cx - w, y))
        for y in range(height - 41, 39, -1):
            t = (y - 40) / (height - 80)
            w = 32 * math.sin(t * math.pi)
            points.append((cx + w, y))
        draw.polygon(points, fill=(68, 142, 52))
        draw.line([(cx, 40), (cx, height - 40)], fill=(110, 185, 90), width=3)
        if condition == "blast":
            spots = [(cx, cy - 60), (cx - 5, cy + 10), (cx + 3, cy + 80)]
            for sx, sy in spots:
                draw.polygon([(sx, sy - 22), (sx + 10, sy), (sx, sy + 22), (sx - 10, sy)], fill=(110, 45, 15))
                draw.polygon([(sx, sy - 14), (sx + 6, sy), (sx, sy + 14), (sx - 6, sy)], fill=(190, 185, 175))
        elif condition == "bacterial_blight":
            for y in range(cy - 80, cy + 100, 8):
                draw.ellipse([cx - 25, y, cx - 10, y + 14], fill=(185, 150, 40))
                draw.ellipse([cx + 10, y + 10, cx + 25, y + 24], fill=(150, 100, 30))

    else:  # Tomato / General foliage
        leaf_color = (55, 135, 45) if condition != "healthy" else (50, 155, 40)
        draw.ellipse([cx - 95, cy - 140, cx + 95, cy + 110], fill=leaf_color)
        draw.line([(cx, cy + 100), (cx, height - 25)], fill=(40, 100, 30), width=6)
        draw.line([(cx, cy + 100), (cx, cy - 130)], fill=(85, 175, 75), width=4)
        for dy in range(-100, 80, 35):
            draw.line([(cx, cy + dy), (cx - 70, cy + dy - 25)], fill=(75, 160, 65), width=2)
            draw.line([(cx, cy + dy), (cx + 70, cy + dy - 25)], fill=(75, 160, 65), width=2)

        if condition == "early_blight":
            spots = [(cx - 35, cy - 40, 26), (cx + 40, cy + 20, 32), (cx - 20, cy + 50, 20)]
            for sx, sy, r in spots:
                draw.ellipse([sx - r - 8, sy - r - 8, sx + r + 8, sy + r + 8], fill=(195, 180, 45))
                draw.ellipse([sx - r, sy - r, sx + r, sy + r], fill=(85, 45, 20))
                draw.ellipse([sx - r + 6, sy - r + 6, sx + r - 6, sy + r - 6], fill=(120, 65, 30))

    img = img.filter(ImageFilter.SMOOTH_MORE)
    return img

def generate_all_samples():
    output_dir = os.path.join(os.path.dirname(__file__), "sample_data")
    os.makedirs(output_dir, exist_ok=True)

    samples = [
        ("tomato_early_blight.png", "tomato", "early_blight"),
        ("banana_sigatoka.png", "banana", "sigatoka"),
        ("citrus_lemon_canker.png", "citrus", "canker"),
        ("mango_anthracnose.png", "mango", "anthracnose"),
        ("coconut_leaf_rot.png", "coconut", "leaf_rot"),
        ("paddy_blast.png", "rice", "blast"),
        ("paddy_bacterial_blight.png", "rice", "bacterial_blight"),
        ("general_healthy.png", "tomato", "healthy")
    ]

    for filename, s_type, cond in samples:
        path = os.path.join(output_dir, filename)
        img = create_botanical_sample(400, 400, s_type, cond)
        img.save(path, "PNG")
        print(f"Generated: {path}")

if __name__ == "__main__":
    import sys
    if sys.platform.startswith("win"):
        sys.stdout.reconfigure(encoding='utf-8')
    generate_all_samples()
