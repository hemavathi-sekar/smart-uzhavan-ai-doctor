# 🌾 ஸ்மார்ட் உழவன் AI மருத்துவர் (Smart "Uzhavan" AI Doctor)
### with Tamil Human Voice Agent & Universal Botanical Disease Scanner (AgriTech)

> **"உழவன் கடன் சுமையில் விழாமல் காப்போம்; பயிர் நோய்களை தூய தமிழிலேயே தீர்ப்போம்!"**  
> *Protecting Indian farmers from spurious pesticide debt traps with human-like Tamil voice AI, instant leaf scanning, and localized treatments.*

---

1. **🌾 Universal Plant & Tree Support (அனைத்து இலைகள், பயிர்கள், மரங்கள்)**:
   - Covers not just tomatoes, but **Paddy, Brinjal, Banana, Mango, Citrus/Lemon, Guava, Cotton, Pear, Apple, Jasmine, Pepper, Papaya, Coconut, Sugarcane, Rose**, and any agricultural/horticultural leaf.
2. **🎙️ Studio-Grade 100% Natural Human Tamil Voice**:
   - Uses Microsoft Edge Neural Voice (`ta-IN-ValluvarNeural` - authentic Tamil rural elder agriculture doctor).
   - Crisp natural intonation, cadence, and pause handling (replaces robotic speech).
3. **📋 5 Core Questions Answered in High-Contrast Cards**:
   - 🌿 **1. இது என்ன பயிர் / மரம்?** (Plant & Leaf Identification)
   - 🔬 **2. என்ன நோய் தாக்கியுள்ளது?** (Exact Disease & Severity %)
   - ❓ **3. இந்த நோய் எதனால் வந்தது?** (Root Cause - Fungal, Humidity, Soil, Vector)
   - 🛡️ **4. இனிமேல் வராமல் தடுக்க என்ன செய்ய வேண்டும்?** (Long-term Prevention Strategy)
   - 💊 **5. இதற்கு என்ன மருந்து? எப்படி, எவ்வளவு, எப்போது அடிக்க வேண்டும்?**
     - **இயற்கை முறை (Organic):** Full home recipe (வேப்பிலை கரைசல், இஞ்சி பூண்டு கரைசல்), 10L dilution, spraying hours.
     - **இரசாயன முறை (Chemical):** Exact chemical name, exact dose (ml/gm per liter water), and Pre-Harvest Interval (PHI).
4. **⚡ Zero Friction UX (உடனடி ரிசல்ட்)**:
   - Instant auto-scan on photo upload without permission nags or extra clicks.
5. **🛡️ Farmer Debt Shield**:
   - Compares costs: Chemical dealer cocktail (~₹2,500/acre) vs. Uzhavan AI prescription (~₹120/acre organic), saving smallholder farmers thousands of rupees.

---

## 📂 Project Structure

```text
├── app.py                      # Main Streamlit Web Application (Tamil UI)
├── uzhavan_ai.py               # AI Diagnostics (Gemini Multimodal + Botanical fallback)
├── botanical_classifier.py     # Offline morphological & spectral CV classifier
├── agro_knowledge_base.py      # Comprehensive Tamil & English disease database
├── voice_assistant.py          # Microsoft Edge Neural Human Tamil Voice engine
├── spectral_scanner.py         # NDVI, Chlorophyll & Necrosis heatmap generator
├── generate_samples.py         # Test sample generator
├── run_app.bat                 # One-click launcher for Windows (Double-click to run!)
├── requirements.txt            # Python dependencies
├── .env                        # Google Gemini API key configuration
├── .env.example                # Template for API key
└── sample_data/                # Built-in sample leaf images for quick demo
```

---

## 🚀 How to Run the Project

### Method 1: One-Click Run (Windows)
Simply double-click the **`run_app.bat`** file! It will automatically:
1. Check Python installation
2. Create virtual environment and install requirements
3. Start the application and launch it in your browser (`http://localhost:8501`)

---

### Method 2: Manual Setup (Terminal / PowerShell / Mac / Linux)

1. **Clone or Extract the Project folder**:
   ```bash
   cd project
   ```

2. **Create and Activate a Virtual Environment**:
   - **Windows (PowerShell)**:
     ```powershell
     python -m venv .venv
     .venv\Scripts\Activate.ps1
     ```
   - **Mac / Linux**:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Gemini API Key**:
   - Open `.env` and verify your key:
     ```env
     GEMINI_API_KEY=your_gemini_api_key_here
     ```
   - *(Free API Key can be obtained from [Google AI Studio](https://aistudio.google.com/app/apikey))*

5. **Start the Application**:
   ```bash
   streamlit run app.py
   ```
   Open your browser at **`http://localhost:8501`**.

---

## 🌐 Public Sharing / Deployment
To share live on the internet during presentations or with judges:
```bash
cloudflared tunnel --url http://localhost:8501
```
Or deploy freely on **Streamlit Community Cloud** with 1 click from your GitHub repository!
