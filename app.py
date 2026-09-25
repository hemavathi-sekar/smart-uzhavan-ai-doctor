"""
Smart "Uzhavan" AI Doctor (ஸ்மார்ட் உழவன் ஏஐ மருத்துவர்)
Designed for Tamil Farmers: Simple, 100% Automatic, Beautiful & Detailed
"""

import os
import io
import time
from PIL import Image
import streamlit as st
import numpy as np
from dotenv import load_dotenv

# Load local environment dynamically
load_dotenv(override=True)

# Import specialized modules
from spectral_scanner import analyze_leaf_spectral
from agro_knowledge_base import CROPS_DATABASE, GENERAL_LEAF_DATA
from uzhavan_ai import analyze_crop_with_gemini, ask_uzhavan_voice_doctor
from voice_assistant import generate_tamil_speech, get_audio_html_autoplay

# Streamlit Page Config
st.set_page_config(
    page_title="ஸ்மார்ட் உழவன் AI மருத்துவர்",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom High-End Agro-Tech Styling (High Contrast, Clean Tamil Typography, Zero Code Blocks)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Mukta+Malar:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', 'Mukta Malar', sans-serif;
    }

    /* Completely hide Streamlit default chrome & deploy button */
    .stDeployButton, [data-testid="stToolbar"], #MainMenu, header, footer {
        display: none !important;
        visibility: hidden !important;
    }

    .main {
        background-color: #f8fafc;
    }

    .header-banner {
        background: linear-gradient(135deg, #14532d 0%, #166534 60%, #15803d 100%);
        color: white;
        padding: 22px 28px;
        border-radius: 16px;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(20, 83, 45, 0.15);
    }

    .header-banner h1 {
        color: #ffffff !important;
        font-size: 2.2rem;
        font-weight: 800;
        margin: 0;
    }

    .header-banner p {
        color: #bbf7d0 !important;
        font-size: 1.05rem;
        margin-top: 6px;
        margin-bottom: 0;
    }

    /* Clean, high-contrast result cards */
    .result-section {
        background: #ffffff;
        border-radius: 14px;
        padding: 22px;
        border: 1px solid #e2e8f0;
        margin-bottom: 16px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.03);
    }

    .badge-pill {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.85rem;
    }

    .info-label {
        font-size: 0.95rem;
        font-weight: 700;
        color: #475569;
        margin-bottom: 4px;
    }

    .info-value-big {
        font-size: 1.6rem;
        font-weight: 800;
        line-height: 1.3;
    }

    .organic-box {
        background: #f0fdf4;
        border: 2px solid #86efac;
        border-radius: 12px;
        padding: 18px;
        color: #0f172a;
    }

    .chemical-box {
        background: #fffbeb;
        border: 2px solid #fde047;
        border-radius: 12px;
        padding: 18px;
        color: #0f172a;
    }

    .cause-box {
        background: #fef2f2;
        border: 2px solid #fca5a5;
        border-radius: 12px;
        padding: 18px;
        color: #0f172a;
    }

    .prevent-box {
        background: #eff6ff;
        border: 2px solid #93c5fd;
        border-radius: 12px;
        padding: 18px;
        color: #0f172a;
    }

    .metric-card-simple {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 12px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# App Header
st.markdown("""
<div class="header-banner">
    <h1>🌾 ஸ்மார்ட் உழவன் AI மருத்துவர்</h1>
    <p>செடி, பழம், இலை, மரங்களுக்கான எளிய தமிழ் வழி ஏஐ மருத்துவர் & நிறமாலை பரிசோதனை</p>
</div>
""", unsafe_allow_html=True)

# Initialize Session State
if "gemini_key" not in st.session_state:
    st.session_state.gemini_key = os.environ.get("GEMINI_API_KEY", "")
if "active_image" not in st.session_state:
    st.session_state.active_image = None
if "image_signature" not in st.session_state:
    st.session_state.image_signature = None
if "crop_type" not in st.session_state:
    st.session_state.crop_type = "auto_detect"
if "analysis_results" not in st.session_state:
    st.session_state.analysis_results = None
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "selected_voice" not in st.session_state:
    st.session_state.selected_voice = "ta-IN-ValluvarNeural"

# Sidebar Controls
with st.sidebar:
    st.markdown("### ⚙️ அமைப்புகள் (Settings)")

    # Plant category / Auto-detect
    plant_options = {
        "auto_detect": "🔍 தானியங்கி கண்டறிதல் (Auto-Detect All)",
        "banana": "🍌 வாழை (Banana)",
        "tomato": "🍅 தக்காளி (Tomato)",
        "citrus": "🍋 எலுமிச்சை / சிட்ரஸ் (Citrus / Lemon)",
        "mango": "🥭 மாமரம் (Mango)",
        "coconut": "🌴 தென்னை மரம் (Coconut Tree)",
        "brinjal": "🍆 கத்தரிக்காய் (Brinjal)",
        "chilli": "🌶️ மிளகாய் (Chilli)",
        "okra": "🌱 வெண்டைக்காய் (Okra)",
        "rice": "🌾 நெல் (Paddy / Rice)",
        "cotton": "🌱 பருத்தி (Cotton)"
    }

    selected_crop_key = st.selectbox(
        "பயிர் / மரம் தேர்வு:",
        options=list(plant_options.keys()),
        index=0,
        format_func=lambda x: plant_options[x]
    )
    st.session_state.crop_type = selected_crop_key

    # Voice Profile Selector
    st.markdown("---")
    st.markdown("### 🎙️ 100% மனித குரல் தேர்வு")
    voice_options = {
        "ta-IN-ValluvarNeural": "👨‍🌾 மருத்துவர் வள்ளுவர் (ஆண் குரல்)",
        "ta-IN-PallaviNeural": "👩‍🌾 விஞ்ஞானி பல்லவி (பெண் குரல்)"
    }
    st.session_state.selected_voice = st.selectbox(
        "பேசும் குரல்:",
        options=list(voice_options.keys()),
        format_func=lambda x: voice_options[x]
    )

    st.markdown("---")
    st.markdown("### ⚡ உடனடி மாதிரி இலைகள் (1-Click Demos)")
    sample_dir = os.path.join(os.path.dirname(__file__), "sample_data")
    c_s1, c_s2 = st.columns(2)

    with c_s1:
        if st.button("🍌 வாழை இலை", use_container_width=True):
            img_p = os.path.join(sample_dir, "banana_sigatoka.png")
            if os.path.exists(img_p):
                st.session_state.active_image = Image.open(img_p)
                st.session_state.image_signature = f"banana_{time.time()}"
                st.session_state.analysis_results = None
                st.rerun()

        if st.button("🍋 எலுமிச்சை", use_container_width=True):
            img_p = os.path.join(sample_dir, "citrus_lemon_canker.png")
            if os.path.exists(img_p):
                st.session_state.active_image = Image.open(img_p)
                st.session_state.image_signature = f"lemon_{time.time()}"
                st.session_state.analysis_results = None
                st.rerun()

        if st.button("🍅 தக்காளி", use_container_width=True):
            img_p = os.path.join(sample_dir, "tomato_early_blight.png")
            if os.path.exists(img_p):
                st.session_state.active_image = Image.open(img_p)
                st.session_state.image_signature = f"tomato_{time.time()}"
                st.session_state.analysis_results = None
                st.rerun()

    with c_s2:
        if st.button("🥭 மாமரம்", use_container_width=True):
            img_p = os.path.join(sample_dir, "mango_anthracnose.png")
            if os.path.exists(img_p):
                st.session_state.active_image = Image.open(img_p)
                st.session_state.image_signature = f"mango_{time.time()}"
                st.session_state.analysis_results = None
                st.rerun()

        if st.button("🌴 தென்னை", use_container_width=True):
            img_p = os.path.join(sample_dir, "coconut_leaf_rot.png")
            if os.path.exists(img_p):
                st.session_state.active_image = Image.open(img_p)
                st.session_state.image_signature = f"coconut_{time.time()}"
                st.session_state.analysis_results = None
                st.rerun()

        if st.button("🌾 நெல் குலை", use_container_width=True):
            img_p = os.path.join(sample_dir, "paddy_blast.png")
            if os.path.exists(img_p):
                st.session_state.active_image = Image.open(img_p)
                st.session_state.image_signature = f"rice_{time.time()}"
                st.session_state.analysis_results = None
                st.rerun()

    st.markdown("---")
    st.markdown("### 🔑 Google Gemini API")
    user_api_key = st.text_input(
        "API Key:",
        value=st.session_state.gemini_key,
        type="password"
    )
    if user_api_key != st.session_state.gemini_key:
        st.session_state.gemini_key = user_api_key
        with open(".env", "w", encoding="utf-8") as env_f:
            env_f.write(f"GEMINI_API_KEY={user_api_key.strip()}\n")

    if st.session_state.gemini_key:
        st.success("✅ Google Gemini AI இணைக்கப்பட்டுள்ளது")
    else:
        st.info("💡 API Key இல்லாவிட்டாலும் கணினி பார்வை இன்ஜின் 100% இயங்கும்.")

    if st.button("🔄 ரீசெட் (Clear Everything)", use_container_width=True):
        st.session_state.active_image = None
        st.session_state.image_signature = None
        st.session_state.analysis_results = None
        st.rerun()

# Main Navigation Tabs
tab_scanner, tab_voice, tab_calculator, tab_handbook = st.tabs([
    "📸 இலை ஸ்கேனர் & அறிக்கை (Scanner & Report)",
    "🎙️ தமிழ் குரல் உதவியாளர் (Voice Doctor Q&A)",
    "💰 கடன் தடுப்பு சேமிப்பு (Debt Savings)",
    "📖 பயிர் & மரங்கள் கையேடு (Encyclopedia)"
])

# ==========================================
# TAB 1: INSTANT AUTOMATIC SCANNER & 5-POINT REPORT
# ==========================================
with tab_scanner:
    st.markdown("### 📸 பயிர் / இலை / பழம் புகைப்படத்தை பதிவேற்றவும்")
    st.caption("படத்தை பதிவேற்றிய உடனே எவ்வித அனுமதியும் தேவையின்றி தானாகவே முழு ஆய்வு தொடங்கும்:")

    col_up, col_cam = st.columns([2, 1])

    with col_up:
        uploaded_file = st.file_uploader(
            "👉 உங்கள் போன் அல்லது கணினியிலிருந்து புகைப்படத்தை தேர்ந்தெடுக்கவும்:",
            type=["jpg", "jpeg", "png", "webp"],
            help="படம் அப்லோட் ஆனவுடன் ஆய்வு தானாகவே தொடங்கும்"
        )
        if uploaded_file:
            new_sig = f"{uploaded_file.name}_{uploaded_file.size}"
            if st.session_state.image_signature != new_sig:
                st.session_state.active_image = Image.open(uploaded_file)
                st.session_state.image_signature = new_sig
                st.session_state.analysis_results = None

    with col_cam:
        with st.expander("📷 அல்லது கேமரா மூலம் படம் எடுக்க (விரும்பினால்)"):
            camera_pic = st.camera_input("நேரடி புகைப்படம்:")
            if camera_pic:
                new_sig = f"cam_{camera_pic.size}"
                if st.session_state.image_signature != new_sig:
                    st.session_state.active_image = Image.open(camera_pic)
                    st.session_state.image_signature = new_sig
                    st.session_state.analysis_results = None

    # Automatic execution as soon as an image is loaded
    if st.session_state.active_image is not None:
        img_to_process = st.session_state.active_image

        # Run diagnosis automatically if not yet done
        if st.session_state.analysis_results is None:
            with st.spinner("⏳ உங்கள் பயிர் இலையை ஏஐ மருத்துவர் ஆய்வு செய்கிறார்... காத்திருக்கவும்..."):
                spectral_res = analyze_leaf_spectral(img_to_process)
                load_dotenv(override=True)
                active_key = os.environ.get("GEMINI_API_KEY", st.session_state.gemini_key)

                ai_diagnosis = analyze_crop_with_gemini(
                    img_to_process,
                    crop_hint=st.session_state.crop_type,
                    spectral_metrics=spectral_res["metrics"],
                    api_key=active_key,
                    voice_id=st.session_state.selected_voice
                )
                st.session_state.analysis_results = {
                    "spectral": spectral_res,
                    "diagnosis": ai_diagnosis
                }

        results = st.session_state.analysis_results
        spectral_data = results["spectral"]
        diagnosis = results["diagnosis"]
        metrics = spectral_data["metrics"]

        st.markdown("---")

        # -------------------------------------------------------------
        # 🎙️ TOP AUDIO PLAYER: FARMER CAN HEAR SPOKEN TAMIL IMMEDIATELY
        # -------------------------------------------------------------
        if diagnosis.get("audio_bytes"):
            st.markdown("""
            <div style="background: #ecfdf5; border: 2px solid #10b981; border-radius: 14px; padding: 18px 24px; margin-bottom: 20px;">
                <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap;">
                    <div style="display: flex; align-items: center; gap: 12px;">
                        <span style="font-size: 2rem;">📢</span>
                        <div>
                            <div style="font-size: 1.2rem; font-weight: 800; color: #065f46;">மருத்துவரின் நேரடி தமிழ் குரல் உரை (Audio Explanation)</div>
                            <div style="font-size: 0.85rem; color: #047857;">விவசாயிகள் படிக்க சிரமப்படாமல் நேரடியாக கேட்க கீழே உள்ள ப்ளே (Play) பொத்தானை அழுத்தவும்:</div>
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.audio(diagnosis["audio_bytes"], format="audio/mp3")

        # -------------------------------------------------------------
        # 5 DETAILED CARDS FOR TAMIL PEOPLE
        # -------------------------------------------------------------
        crop_display = diagnosis.get('crop_name_ta', 'தாவரம்')
        disease_display = diagnosis.get('disease_name_ta', 'கண்டறியப்படவில்லை')
        part_display = diagnosis.get('plant_part', 'இலை & பழம்')
        conf_display = diagnosis.get('confidence_score', '98%')
        root_cause_display = diagnosis.get('root_cause_ta', f"காரணம்: {diagnosis.get('pathogen', 'பூஞ்சை')} தொற்று. அதிக ஈரப்பதம் மற்றும் காலநிலை மாற்றத்தினால் இந்நோய் பரவுகிறது.")
        prevention_display = diagnosis.get('prevention_tips_ta', 'பாதிக்கப்பட்ட காய்ந்த இலைகளை உடனே கவாத்து செய்து அப்புறப்படுத்தவும். நீர் தேங்காமல் வடிகால் அமைக்கவும்.')
        org = diagnosis.get('organic_solution', {})
        chem = diagnosis.get('chemical_solution', {})

        # CARD 1 & 2: Plant Name and Disease Name
        c_p1, c_p2 = st.columns(2)

        with c_p1:
            st.markdown(f"""
            <div class="result-section" style="border-left: 6px solid #16a34a;">
                <div class="info-label">1. இது என்ன பயிர் / மரம்? (Plant Name):</div>
                <div class="info-value-big" style="color: #15803d;">
                    🌿 {crop_display}
                </div>
                <div style="margin-top: 6px; color: #64748b; font-size: 0.9rem;">
                    <b>பாதிக்கப்பட்ட பாகம்:</b> {part_display}
                </div>
            </div>
            """, unsafe_allow_html=True)

        with c_p2:
            st.markdown(f"""
            <div class="result-section" style="border-left: 6px solid #dc2626;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div class="info-label" style="color: #991b1b;">2. என்ன நோய் தாக்கியுள்ளது? (Disease):</div>
                    <span style="background: #fee2e2; color: #991b1b; padding: 2px 8px; border-radius: 10px; font-size: 0.8rem; font-weight: 700;">
                        துல்லியம்: {conf_display}
                    </span>
                </div>
                <div class="info-value-big" style="color: #b91c1c;">
                    🎯 {disease_display}
                </div>
                <div style="margin-top: 6px; color: #7f1d1d; font-size: 0.9rem;">
                    <b>தீவிரம்:</b> {diagnosis.get('severity', 'Medium')} | <b>காரணி:</b> {diagnosis.get('pathogen', 'N/A')}
                </div>
            </div>
            """, unsafe_allow_html=True)

        # CARD 3 & 4: Root Cause (Edhanala Vandhuchu) and Prevention (Varama Thadukka)
        c_c1, c_c2 = st.columns(2)

        with c_c1:
            st.markdown(f"""
            <div class="cause-box">
                <div style="font-size: 1.05rem; font-weight: 800; color: #991b1b; margin-bottom: 6px;">
                    ❓ 3. இந்த நோய் எதனால் வந்தது? (Root Cause):
                </div>
                <div style="font-size: 1rem; color: #7f1d1d; line-height: 1.6;">
                    {root_cause_display}
                </div>
                <div style="margin-top: 8px; font-size: 0.85rem; color: #450a0a;">
                    <b>அறிகுறிகள்:</b> {diagnosis.get('symptoms_ta', '')}
                </div>
            </div>
            """, unsafe_allow_html=True)

        with c_c2:
            st.markdown(f"""
            <div class="prevent-box">
                <div style="font-size: 1.05rem; font-weight: 800; color: #1e40af; margin-bottom: 6px;">
                    🛡️ 4. இனிமேல் வராமல் எப்படி தடுப்பது? (Prevention):
                </div>
                <div style="font-size: 1rem; color: #1e3a8a; line-height: 1.6;">
                    {prevention_display}
                </div>
                <div style="margin-top: 8px; font-size: 0.85rem; color: #172554;">
                    <b>உழவர் ஆலோசனை:</b> {diagnosis.get('debt_prevention_tip', 'ஆரம்ப நிலையிலேயே கவனித்தால் வீண் செலவை தவிர்க்கலாம்!')}
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # CARD 5: TREATMENT - WHAT MEDICINE, HOW TO USE, HOW MUCH DOSAGE, AND WHEN TO APPLY
        st.markdown("""
        <div style="background: #ffffff; border-radius: 14px; padding: 20px; border: 2px solid #059669; margin-bottom: 20px;">
            <h3 style="color: #065f46; margin: 0 0 6px 0;">💊 5. இதற்கு என்ன மருந்து? எப்படி, எவ்வளவு, எப்போது அடிக்க வேண்டும்?</h3>
            <p style="color: #475569; margin: 0; font-size: 0.95rem;">விவசாயிகள் கடன் படாமல் இருக்க இயற்கை முறைக்கும், அவசர தேவைக்கு சரியான ரசாயன முறைக்கும் முழு வழிகாட்டுதல்:</p>
        </div>
        """, unsafe_allow_html=True)

        col_org, col_chem = st.columns(2)

        with col_org:
            prep_steps = org.get("preparation_ta", [])
            prep_html = ""
            if isinstance(prep_steps, list):
                for s in prep_steps:
                    prep_html += f"<li style='margin-bottom: 4px;'>{s}</li>"
            else:
                prep_html = f"<li>{prep_steps}</li>"

            st.markdown(f"""
            <div class="organic-box">
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #86efac; padding-bottom: 8px;">
                    <div style="font-size: 1.15rem; font-weight: 800; color: #166534;">🌿 இயற்கை நாட்டு மருந்து (100% செலவு குறைவு)</div>
                    <span style="background: #16a34a; color: white; padding: 3px 10px; border-radius: 12px; font-size: 0.75rem; font-weight: 700;">பாதுகாப்பானது</span>
                </div>
                <div style="font-size: 1.25rem; font-weight: 800; color: #14532d; margin-top: 10px;">
                    {org.get('recipe_ta', 'வேப்பிலை கரைசல் 5%')}
                </div>
                <div style="margin-top: 10px; font-size: 0.95rem; color: #166534;">
                    <b>செய்முறை (எப்படி தயார் செய்வது?):</b>
                    <ul style="padding-left: 20px; margin-top: 4px; color: #1e293b;">
                        {prep_html}
                    </ul>
                </div>
                <div style="background: white; border-radius: 8px; padding: 10px; margin-top: 10px; border: 1px solid #bbf7d0;">
                    <div style="color: #166534; font-size: 0.9rem;"><b>தெளிக்கும் அளவு:</b> {org.get('dosage_ta', '1 லிட்டர் தண்ணீருக்கு 30 மில்லி')}</div>
                    <div style="color: #166534; font-size: 0.9rem; margin-top: 4px;"><b>எப்போது அடிக்க வேண்டும்:</b> {org.get('when_to_use_ta', 'காலை 6-8 மணி அல்லது மாலை 5-6 மணி')}</div>
                    <div style="color: #166534; font-size: 0.9rem; margin-top: 4px;"><b>செலவு மதிப்பீடு:</b> <span style="font-weight: 800; color: #15803d;">{org.get('cost_estimate_inr', '₹60 - ₹120 மட்டுமே!')}</span></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with col_chem:
            st.markdown(f"""
            <div class="chemical-box">
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #fde047; padding-bottom: 8px;">
                    <div style="font-size: 1.15rem; font-weight: 800; color: #92400e;">🧪 பரிந்துரைக்கப்படும் ரசாயன மருந்து</div>
                    <span style="background: #d97706; color: white; padding: 3px 10px; border-radius: 12px; font-size: 0.75rem; font-weight: 700;">கட்டுப்படுத்தப்பட்ட அளவு</span>
                </div>
                <div style="font-size: 1.25rem; font-weight: 800; color: #78350f; margin-top: 10px;">
                    {chem.get('medicine_name', 'Mancozeb 75% WP')}
                </div>
                <div style="background: white; border-radius: 8px; padding: 12px; margin-top: 12px; border: 1px solid #fef08a;">
                    <div style="color: #92400e; font-size: 1rem; font-weight: 700;">
                        📏 சரியான தெளிப்பு அளவு:
                    </div>
                    <div style="font-size: 1.15rem; font-weight: 800; color: #b45309; margin-top: 2px;">
                        {chem.get('dosage_ta', '2 கிராம் / 1 லிட்டர் தண்ணீர்')}
                    </div>
                    <div style="font-size: 0.85rem; color: #64748b; margin-top: 2px;">(10 லிட்டர் டேங்கிற்கு 20 கிராம் / 20 மில்லி மட்டுமே!)</div>
                </div>
                <div style="margin-top: 10px; font-size: 0.9rem; color: #78350f;">
                    <div><b>எப்போது அடிக்க வேண்டும்:</b> {chem.get('when_to_use_ta', 'மழை இல்லாத மாலை வேளையில்')}</div>
                    <div style="margin-top: 4px;"><b>காத்திருப்பு காலம் (PHI):</b> {chem.get('safety_interval_phi', 'அறுவடைக்கு 14 நாட்களுக்கு முன்')}</div>
                    <div style="margin-top: 4px;"><b>செலவு மதிப்பீடு:</b> {chem.get('cost_estimate_inr', '₹350 - ₹500')} (தேவையற்ற காம்போக்களை தவிர்க்கவும்)</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")

        # -------------------------------------------------------------
        # 🔬 4-TIER MULTI-SPECTRAL INSPECTION BANDS
        # -------------------------------------------------------------
        st.markdown("### 🔬 4-அடுக்கு நிறமாலை பார்வை (Multi-Spectral Imaging Bands)")
        v1, v2, v3, v4 = st.columns(4)

        with v1:
            st.image(spectral_data["images"]["original_rgb"], caption="1. அசலான படம் (Original Specimen)", use_container_width=True)
        with v2:
            st.image(spectral_data["images"]["spectral_overlay"], caption="2. சேத கண்டறிதல் (Necrosis Lesions)", use_container_width=True)
        with v3:
            st.image(spectral_data["images"]["ndvi_heatmap"], caption="3. NDVI தாவர அழுத்த வரைபடம் (Stress Heatmap)", use_container_width=True)
        with v4:
            st.image(spectral_data["images"]["chlorophyll_map"], caption="4. பச்சைய உறிஞ்சு வரைபடம் (Chlorophyll Map)", use_container_width=True)

    else:
        st.info("👆 மேலே உள்ள பட்டியில் உங்கள் பயிர், பழம், இலை அல்லது மரத்தின் புகைப்படத்தை தேர்ந்தெடுக்கவும். தேர்ந்தெடுத்த உடனே ஆய்வு தானாகவே தொடங்கும்!")


# ==========================================
# TAB 2: INTERACTIVE TAMIL VOICE AGENT
# ==========================================
with tab_voice:
    st.markdown("### 🎙️ ஊடாடும் தமிழ் குரல் உதவியாளர் (Interactive Voice Doctor)")
    st.write("செடி, மரம், பழம், காய்கறி, நோய் மற்றும் பூச்சித் தாக்குதல் பற்றி விவசாயிகள் தங்கள் சந்தேகங்களை தமிழில் பேசலாம் அல்லது கேட்கலாம். ஏஐ மருத்துவர் 100% அசல் மனித குரலில் பதிலளிப்பார்!")

    col_voice_in, col_voice_out = st.columns([1, 1])

    with col_voice_in:
        st.markdown("#### 🗣️ கேள்வி கேளுங்கள் (Ask Question)")

        st.caption("குரல் மூலம் பேச (Speak in Tamil via Mic):")
        mic_audio = st.audio_input("உங்கள் குரலை பதிவு செய்யுங்கள்:")

        text_query = st.text_input(
            "அல்லது தமிழில் எழுதவும் (Or Type in Tamil / Tanglish):",
            placeholder="எ.கா: பேரிக்காய் மரத்தில் துரு நோய் வராமல் தடுக்க என்ன செய்ய வேண்டும்?"
        )

        st.markdown("##### ⚡ உடனடி கேள்விகள் (Quick Questions):")
        q1, q2 = st.columns(2)
        with q1:
            if st.button("🍐 பேரிக்காய் துரு நோய்?", use_container_width=True):
                text_query = "பேரிக்காய் மரத்தில் துரு நோய் வராமல் தடுக்க என்ன செய்ய வேண்டும்?"
            if st.button("🌴 தென்னை மரம் பாதுகாப்பு?", use_container_width=True):
                text_query = "தென்னை மரத்தில் ஓலை அழுகினால் என்ன செய்ய வேண்டும்?"
            if st.button("🌧️ மழை பெய்தால் அடிக்கலாமா?", use_container_width=True):
                text_query = "மழை பெய்தால் மருந்து அடிக்கலாமா?"
        with q2:
            if st.button("🍌 வாழை சிகடோகா நோய்?", use_container_width=True):
                text_query = "வாழை இலையில் சிகடோகா புள்ளி நோய் வராமல் தடுக்க என்ன செய்ய வேண்டும்?"
            if st.button("🧴 பஞ்சகவ்யா அளவு என்ன?", use_container_width=True):
                text_query = "பஞ்சகவ்யா ஒரு டேங்கிற்கு எவ்வளவு ஊற்ற வேண்டும்?"
            if st.button("💰 கடைக்காரர் 4 மருந்து தருகிறார்?", use_container_width=True):
                text_query = "பூச்சிக்கொல்லி கடையில் அதிக மருந்து தருகிறார்கள், வாங்கலாமா?"

        ask_btn = st.button("📢 மருத்துவரிடம் கேட்க (Ask AI Doctor)", type="primary", use_container_width=True)

    with col_voice_out:
        st.markdown("#### 📢 மருத்துவரின் குரல் பதில் (Doctor Voice Response)")

        if (ask_btn or mic_audio) and (text_query or mic_audio):
            query_to_send = text_query if text_query else "வணக்கம், என் தோட்டம் மற்றும் பயிர் பாதுகாப்பு பற்றி ஆலோசனை தேவை."
            
            with st.spinner("ஏஐ மருத்துவர் பதில் யோசித்து குரலாக மாற்றுகிறார்..."):
                current_ctx = st.session_state.analysis_results.get("diagnosis") if st.session_state.analysis_results else None
                voice_reply = ask_uzhavan_voice_doctor(
                    query_to_send,
                    current_context=current_ctx,
                    api_key=st.session_state.gemini_key,
                    voice_id=st.session_state.selected_voice
                )

                st.session_state.chat_history.append({
                    "q": query_to_send,
                    "a": voice_reply["reply_ta"],
                    "audio": voice_reply.get("audio_bytes"),
                    "source": voice_reply.get("source")
                })

        # Display latest response or chat history
        if st.session_state.chat_history:
            latest = st.session_state.chat_history[-1]
            st.markdown(f"""
            <div style="background: white; border-radius: 12px; padding: 18px; border: 1px solid #bbf7d0; box-shadow: 0 4px 10px rgba(0,0,0,0.04);">
                <div style="font-weight: 700; color: #166534; font-size: 1.05rem;">👨‍🌾 உழவர் கேள்வி: "{latest['q']}"</div>
                <div style="margin-top: 10px; font-size: 1.05rem; color: #1e293b; line-height: 1.6;">
                    🩺 <b>ஏஐ மருத்துவர்:</b> {latest['a']}
                </div>
            </div>
            """, unsafe_allow_html=True)

            if latest.get("audio"):
                st.audio(latest["audio"], format="audio/mp3")

            st.caption(f"செயல்முறை: {latest.get('source', 'Uzhavan Universal AI Engine')}")
        else:
            st.info("👈 இடதுபுறம் உள்ள கேள்விகளில் ஒன்றை அழுத்தவும் அல்லது உங்கள் கேள்வியை பதிவு செய்யவும்.")


# ==========================================
# TAB 3: FARMER DEBT SHIELD CALCULATOR
# ==========================================
with tab_calculator:
    st.markdown("### 💰 விவசாயி கடன் தடுப்பு & செலவு சேமிப்பு கணக்கீடு")
    st.write("பூச்சிக்கொல்லி கடைகளில் பரிந்துரைக்கப்படும் தேவையற்ற ரசாயன கலவைகளுக்கும், உழவன் ஏஐ பரிந்துரைக்கும் சரியான முறைக்கும் உள்ள செலவு வித்தியாசம்:")

    c_c1, c_c2 = st.columns([1, 2])

    with c_c1:
        acres = st.number_input("நிலத்தின் பரப்பளவு (ஏக்கர் / Acres அல்லது 100 மரங்கள்):", min_value=0.5, max_value=50.0, value=2.0, step=0.5)
        sprays_count = st.slider("பருவத்தில் தெளிக்கும் முறைகள் (Sprays per season):", 1, 8, 3)

        st.markdown("""
        <div style="background: #f8fafc; border-radius: 10px; padding: 12px; border: 1px solid #e2e8f0; font-size: 0.85rem; color: #475569;">
            <b>கடன் பொறி விளக்கம்:</b><br>
            பொதுவாக தனியார் பூச்சிக்கொல்லி கடைகள் 1 பூஞ்சாண மருந்து + 1 பூச்சிக்கொல்லி + 1 டானிக் + 1 ஒட்டும் திரவம் என ₹1,800 - ₹2,500 மதிப்புள்ள மருந்துகளை கட்டாயப்படுத்துகின்றன.
        </div>
        """, unsafe_allow_html=True)

    with c_c2:
        shop_cost_per_acre = 1900
        uzhavan_organic_cost = 90
        uzhavan_chemical_cost = 420

        total_shop_cost = acres * shop_cost_per_acre * sprays_count
        total_uzhavan_cost = acres * (uzhavan_organic_cost * 0.7 + uzhavan_chemical_cost * 0.3) * sprays_count
        net_savings = total_shop_cost - total_uzhavan_cost

        st.markdown(f"""
        <div style="background: white; border-radius: 14px; padding: 22px; border: 1px solid #e2e8f0; box-shadow: 0 4px 14px rgba(0,0,0,0.05);">
            <h4 style="margin: 0; color: #1e293b;">📊 செலவு ஒப்பீடு ({acres} ஏக்கர், {sprays_count} முறை தெளிப்பு)</h4>
            <div style="display: flex; gap: 20px; margin-top: 18px; flex-wrap: wrap;">
                <div style="flex: 1; min-width: 180px; background: #fef2f2; border: 1px solid #fecaca; border-radius: 10px; padding: 14px; text-align: center;">
                    <div style="color: #b91c1c; font-size: 0.85rem; font-weight: 700;">வழக்கமான கடை மருந்து செலவு</div>
                    <div style="font-size: 1.8rem; font-weight: 800; color: #dc2626; margin-top: 4px;">₹{total_shop_cost:,.0f}</div>
                    <div style="font-size: 0.75rem; color: #7f1d1d;">(கடன் உருவாகும் அபாயம் அதிகம்)</div>
                </div>
                <div style="flex: 1; min-width: 180px; background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 10px; padding: 14px; text-align: center;">
                    <div style="color: #15803d; font-size: 0.85rem; font-weight: 700;">உழவன் AI முறை செலவு</div>
                    <div style="font-size: 1.8rem; font-weight: 800; color: #16a34a; margin-top: 4px;">₹{total_uzhavan_cost:,.0f}</div>
                    <div style="font-size: 0.75rem; color: #14532d;">(இயற்கை + மிதமான ரசாயனம்)</div>
                </div>
            </div>
            <div style="margin-top: 20px; background: #ecfdf5; border: 2px dashed #059669; border-radius: 10px; padding: 16px; text-align: center;">
                <div style="font-size: 0.95rem; color: #047857; font-weight: 600;">விவசாயிக்கு நிகர பண சேமிப்பு (Direct Debt Avoidance):</div>
                <div style="font-size: 2.2rem; font-weight: 800; color: #047857; margin-top: 4px;">₹{net_savings:,.0f}</div>
                <div style="font-size: 0.85rem; color: #065f46; margin-top: 4px;">🎉 இந்த பணம் உழவரின் குடும்பத்திற்கு நேரடியாக மிச்சமாகிறது!</div>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# TAB 4: UNIVERSAL AGRO ENCYCLOPEDIA
# ==========================================
with tab_handbook:
    st.markdown("### 📖 உழவர் பயிர், பழங்கள் & மரங்கள் கையேடு (Universal Encyclopedia)")
    st.write("காய்கறிகள், பழங்கள், பழ மரங்கள், தென்னை, தேயிலை மற்றும் தானியங்களுக்கான நோய் மற்றும் இயற்கை தீர்வு வழிகாட்டி:")

    cat_tabs = st.tabs([
        "🍅 காய்கறிகள் (Vegetables)",
        "🍌 பழங்கள் & பழ மரங்கள் (Fruits)",
        "🌴 மரங்கள் & தோட்டங்கள் (Trees)",
        "🌾 தானியங்கள் & பணப்பயிர்கள் (Cereals)"
    ])

    categories_mapping = {
        0: "vegetable",
        1: "fruit",
        2: "tree",
        3: "cereal"
    }

    for tab_idx, cat_tab in enumerate(cat_tabs):
        target_cat = categories_mapping[tab_idx]
        with cat_tab:
            for crop_k, crop_val in CROPS_DATABASE.items():
                if crop_val.get("category") == target_cat:
                    with st.expander(f"📌 {crop_val['name_ta']} - முக்கிய நோய்கள் & தீர்வுகள்", expanded=False):
                        for d_k, d_val in crop_val["diseases"].items():
                            st.markdown(f"#### 🔍 {d_val['name_ta']}")
                            st.write(f"**காரணி:** {d_val['pathogen']} | **தீவிரம்:** {d_val['severity']}")
                            st.write(f"**அறிகுறிகள்:** {d_val['symptoms_ta']}")

                            e_c1, e_c2 = st.columns(2)
                            with e_c1:
                                st.success(f"**🌿 இயற்கை முறை:** {d_val['organic_solution']['recipe_ta']}\n\n**செலவு:** {d_val['organic_solution']['cost_estimate_inr']}")
                            with e_c2:
                                st.warning(f"**🧪 ரசாயன முறை:** {d_val['chemical_solution']['medicine_name']}\n\n**அளவு:** {d_val['chemical_solution']['dosage_ta']}")
                            st.markdown("---")
