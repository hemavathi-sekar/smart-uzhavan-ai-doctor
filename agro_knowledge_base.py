"""
Agro Knowledge Base for Smart Uzhavan AI Doctor
Universal Agricultural Database for Crop, Vegetable, Fruit, Leaf, and Tree Diseases,
Tamil / English Symptoms, Organic Localized Remedies (நாட்டு மருத்துவம்), and Safe Chemical Dosages.
"""

CROPS_DATABASE = {
    "auto_detect": {
        "name_ta": "🔍 தானியங்கி கண்டறிதல் (Auto-Detect Any Plant / Fruit / Tree)",
        "name_en": "Universal Auto-Detection (All Plants, Fruits, Leaves & Trees)",
        "category": "universal",
        "diseases": {
            "general_blight": {
                "name_ta": "இலைக்கருகல் & பூஞ்சாணத் தாக்குதல் (Foliage Blight & Spot)",
                "name_en": "Universal Foliage Blight / Leaf Spot",
                "pathogen": "Fungus / Bacteria Pathogen",
                "severity": "Medium (நடுத்தரம்)",
                "symptoms_ta": "இலையில் பழுப்பு நிற புள்ளிகள், நுனிக்கருகல் அல்லது நீர் ஊறிய கறை காணப்படுகிறது.",
                "symptoms_en": "Chlorotic halos, necrotic brown lesions and foliar blight on lamina/fruit surface.",
                "organic_solution": {
                    "title_ta": "🌿 இயற்கை நாட்டு மருத்துவம் (Universal Organic Remedy)",
                    "recipe_ta": "வேப்பிலை கரைசல் 5% + புளித்த மோர் அல்லது பஞ்சகவ்யா 3%",
                    "preparation_ta": [
                        "5 கிலோ வேப்பிலையை 10 லிட்டர் நீரில் 24 மணி நேரம் ஊறவைத்து அரைத்து வடிகட்டவும்.",
                        "இதனுடன் 100 கிராம் காதி சோப்பு கரைத்து 100 லிட்டர் நீரில் கலந்து காலை அல்லது மாலை வேளையில் தெளிக்கவும்.",
                        "அல்லது 30 மில்லி பஞ்சகவ்யா / லிட்டர் தண்ணீரில் கலந்து தெளிக்கலாம்."
                    ],
                    "cost_estimate_inr": "₹70 - ₹100 / ஏக்கர் (மரங்களுக்கு ₹150)",
                    "frequency": "7-10 நாட்கள் இடைவெளியில்"
                },
                "chemical_solution": {
                    "title_ta": "🧪 பரிந்துரைக்கப்படும் இரசாயன மருந்து & அளவு (Safe Chemical Dosage)",
                    "medicine_name": "Mancozeb 75% WP அல்லது Copper Oxychloride 50% WP (காப்பர் ஆக்ஸிகுளோரைடு)",
                    "dosage_ta": "2 கிராம் மருந்து / 1 லிட்டர் தண்ணீர் (10 லிட்டர் டேங்கிற்கு 20 கிராம்).",
                    "dosage_en": "2.0g per 1 Liter of water.",
                    "safety_interval_phi": "அறுவடைக்கு 10-14 நாட்களுக்கு முன் தெளிப்பதை நிறுத்தவும்.",
                    "safety_precautions_ta": "முகக்கவசம் அணியவும். காற்று வீசும் திசைக்கு எதிரே தெளிக்க வேண்டாம்.",
                    "cost_estimate_inr": "₹350 - ₹500 / ஏக்கர்"
                },
                "debt_prevention_tip": "எந்த மரம், செடி, காய்கறி ஆனாலும் ஆரம்ப நிலையிலேயே வேப்பிலை கரைசல் தெளித்தால் 80% பூஞ்சாணங்கள் கட்டுப்படும். கடைகளில் விற்கப்படும் தேவையற்ற காம்போக்களை வாங்காதீர்கள்!",
                "audio_script_ta": "வணக்கம் உழவரே! உங்கள் தாவரத்தில் பூஞ்சாண இலைக்கருகல் அல்லது புள்ளி நோய் அறிகுறிகள் தென்படுகின்றன. உடனடியாக 5 சதவீத வேப்பிலை கரைசல் அல்லது பஞ்சகவ்யா தெளிக்கவும். நோய் தீவிரமாக இருந்தால் ஒரு லிட்டர் தண்ணீருக்கு 2 கிராம் காப்பர் ஆக்ஸிகுளோரைடு அல்லது மான்கோசெப் கலந்து தெளிக்கவும். நலமான விளைச்சல் பெற வாழ்த்துகள்!"
            },
            "healthy": {
                "name_ta": "ஆரோக்கியமான தாவரம் / மரம் (Healthy Foliage / Fruit)",
                "name_en": "Healthy Plant Specimen",
                "pathogen": "None (நோய்த்தொற்று இல்லை)",
                "severity": "Good (ஆரோக்கியம்)",
                "symptoms_ta": "இலை மற்றும் பழங்கள் நலம். எவ்வித பூச்சி அல்லது பூஞ்சாண தாக்குதலும் இல்லை.",
                "symptoms_en": "Uniform chlorophyll coloration, no necrotic spots or viral lesions.",
                "organic_solution": {
                    "title_ta": "🌿 வளர்ச்சி ஊக்கி (Natural Growth Tonic)",
                    "recipe_ta": "பஞ்சகவ்யா 3% அல்லது மீன் அமிலம் (Fish Amino Acid)",
                    "preparation_ta": [
                        "30 மில்லி பஞ்சகவ்யாவை 1 லிட்டர் நீரில் கலந்து 15 நாட்களுக்கு ஒருமுறை தெளிக்கவும்."
                    ],
                    "cost_estimate_inr": "₹50 / ஏக்கர்",
                    "frequency": "15 நாட்களுக்கு ஒருமுறை"
                },
                "chemical_solution": {
                    "title_ta": "🧪 இரசாயன மருந்து தேவையில்லை",
                    "medicine_name": "பூச்சிக்கொல்லி தேவையில்லை (Zero chemical needed)",
                    "dosage_ta": "எந்த ரசாயன மருந்தும் அடிக்க வேண்டாம்; பணம் மிச்சம்!",
                    "dosage_en": "No chemical application required.",
                    "safety_interval_phi": "பொருந்தாது",
                    "safety_precautions_ta": "பாசனம் மற்றும் களை மேலாண்மை மட்டும் தொடருங்கள்.",
                    "cost_estimate_inr": "₹0"
                },
                "debt_prevention_tip": "உங்கள் செடி/மரம் மிக ஆரோக்கியமாக உள்ளது! யாரும் மருந்து அடிக்கச் சொன்னாலும் வீணாக பணத்தை செலவழிக்காதீர்கள்.",
                "audio_script_ta": "மகிழ்ச்சியான செய்தி உழவரே! உங்கள் தாவரம் மிக ஆரோக்கியமாக உள்ளது. எந்த நோய்த்தொற்றும் இல்லை. எந்த ரசாயன மருந்தும் அடிக்க வேண்டாம். உங்கள் பணம் மிச்சம்!"
            }
        }
    },

    # ==========================
    # VEGETABLES (காய்கறிகள்)
    # ==========================
    "tomato": {
        "name_ta": "🍅 தக்காளி (Tomato)",
        "name_en": "Tomato",
        "category": "vegetable",
        "diseases": {
            "early_blight": {
                "name_ta": "முன்கூட்டிய கருகல் நோய் (Early Blight)",
                "name_en": "Early Blight (Alternaria solani)",
                "pathogen": "Fungus: Alternaria solani",
                "severity": "Medium - High (இடைநிலை - தீவிரம்)",
                "symptoms_ta": "அடி இலைகளில் வட்ட வடிவ பழுப்பு நிறப் புள்ளிகள் மற்றும் வளையங்கள் (Bullseye rings) தோன்றும். இலைகள் மஞ்சள் நிறமாக மாறி காய்ந்து உதிரும்.",
                "symptoms_en": "Dark brown circular spots with concentric target-like rings on older leaves. Leaves turn yellow and drop prematurely.",
                "organic_solution": {
                    "title_ta": "🌿 இயற்கை நாட்டு மருத்துவம் (Organic Remedy)",
                    "recipe_ta": "வேப்பிலை கரைசல் 5% அல்லது புளித்த மோர் கரைசல்",
                    "preparation_ta": [
                        "5 கிலோ பசுமையான வேப்பிலையை 10 லிட்டர் நீரில் 24 மணி நேரம் ஊறவைத்து அரைத்து சாறு எடுக்கவும்.",
                        "இதனுடன் 100 கிராம் காதி சோப்பு கரைத்து 100 லிட்டர் நீரில் கலந்து காலை அல்லது மாலை வேளையில் தெளிக்கவும்.",
                        "அல்லது 5 லிட்டர் புளித்த மோருடன் 100 கிராம் பெருங்காயத்தூள் கலந்து 100 லிட்டர் நீரில் தெளிக்கலாம்."
                    ],
                    "cost_estimate_inr": "₹60 - ₹100 / ஏக்கர்",
                    "frequency": "7 நாட்களுக்கு ஒருமுறை (2 முறைகள்)"
                },
                "chemical_solution": {
                    "title_ta": "🧪 பரிந்துரைக்கப்படும் இரசாயன மருந்து & அளவு (Safe Chemical Dosage)",
                    "medicine_name": "Mancozeb 75% WP (மான்கோசெப்)",
                    "dosage_ta": "2 கிராம் மருந்தை 1 லிட்டர் தண்ணீரில் கலக்கவும் (10 லிட்டர் தெளிப்பான் டேங்கிற்கு 20 கிராம்).",
                    "dosage_en": "2g per 1 Liter of water (20g per 10L knapsack sprayer).",
                    "safety_interval_phi": "அறுவடைக்கு 7-10 நாட்களுக்கு முன் தெளிப்பதை நிறுத்தவும் (Waiting Period).",
                    "safety_precautions_ta": "கையுறை, முகக்கவசம் அணியவும். காற்று வீசும் திசையை நோக்கி தெளிக்காதீர்கள்.",
                    "cost_estimate_inr": "₹350 - ₹500 / ஏக்கர்"
                },
                "debt_prevention_tip": "பயிர்ப் பாதுகாப்பு கடையில் தேவையற்ற விலை உயர்ந்த 4-5 ரசாயன மருந்துகளை சேர்த்து வாங்காதீர்கள்! வெறும் வேப்பிலை கரைசலே ஆரம்ப கட்டத்தில் 85% நோயைக் கட்டுப்படுத்தும். சேமிப்பு: ₹1,500 - ₹2,000!",
                "audio_script_ta": "வணக்கம் உழவரே! உங்கள் தக்காளி இலையை ஆய்வு செய்ததில் 'முன்கூட்டிய கருகல் நோய்' (Early Blight) இருப்பது கண்டறியப்பட்டுள்ளது. ஆரம்ப கட்டம் என்பதால் பயப்பட வேண்டாம்! 100 லிட்டர் தண்ணீரில் வேப்பிலை கரைசல் அல்லது 5 லிட்டர் புளித்த மோர் உடன் பெருங்காயம் கலந்து தெளித்தால் 3 நாட்களில் நோய் கட்டுக்குள் வரும். நோய் அதிகமாக இருந்தால் மட்டும் ஒரு லிட்டர் தண்ணீருக்கு 2 கிராம் மான்கோசெப் மருந்து கலந்து தெளிக்கவும். நலமான விளைச்சல் பெற வாழ்த்துகள்!"
            },
            "late_blight": {
                "name_ta": "பிற்கால கருகல் நோய் (Late Blight)",
                "name_en": "Late Blight (Phytophthora infestans)",
                "pathogen": "Oomycete: Phytophthora infestans",
                "severity": "Critical (மிகவும் தீவிரமானது - விரைவு நடவடிக்கை தேவை)",
                "symptoms_ta": "இலைகளின் நுனியில் நீர் ஊறிய பழுப்பு மற்றும் கறுப்பு நிற திட்டுகள். அதிக ஈரப்பதமான காலநிலையில் இலையின் அடிப்பகுதியில் வெள்ளை நிற பூஞ்சாண வளர்ச்சி தோன்றும்.",
                "symptoms_en": "Water-soaked dark lesions spreading rapidly on foliage, white fungal growth under humid conditions.",
                "organic_solution": {
                    "title_ta": "🌿 இயற்கை நாட்டு மருத்துவம் (Organic Remedy)",
                    "recipe_ta": "1% போர்டோ கலவை (Bordeaux Mixture) அல்லது சூடோமோனாஸ்",
                    "preparation_ta": [
                        "1 கிலோ மயில் துத்தம் (Copper Sulphate) மற்றும் 1 கிலோ பொடித்த நீற்று சுண்ணாம்பு தனித்தனியாக நீரில் கரைத்து 100 லிட்டர் போர்டோ கலவை தயாரிக்கவும்.",
                        "உடனடியாக இலைகளின் அடிப்புறம் நனையும்படி தெளிக்கவும்."
                    ],
                    "cost_estimate_inr": "₹150 / ஏக்கர்",
                    "frequency": "5 நாட்கள் இடைவெளியில்"
                },
                "chemical_solution": {
                    "title_ta": "🧪 பரிந்துரைக்கப்படும் இரசாயன மருந்து & அளவு (Safe Chemical Dosage)",
                    "medicine_name": "Metalaxyl 8% + Mancozeb 64% WP (ரிடோமில் / Ridomil MZ)",
                    "dosage_ta": "2.5 கிராம் மருந்து / 1 லிட்டர் நீர் (டேங்கிற்கு 25 கிராம்).",
                    "dosage_en": "2.5g per 1 Liter of water.",
                    "safety_interval_phi": "அறுவடைக்கு 14 நாட்களுக்கு முன்.",
                    "safety_precautions_ta": "மழை பெய்யும் நேரத்தில் தெளிக்கக் கூடாது; உடனடி பாதுகாப்பு கவசம் அவசியம்.",
                    "cost_estimate_inr": "₹600 - ₹800 / ஏக்கர்"
                },
                "debt_prevention_tip": "பிற்கால கருகல் நோய் வேகமாக பரவக்கூடியது. ஆனால் கடைகளில் ரூ. 3000 வரை விற்கப்படும் காம்போக்களை நம்ப வேண்டாம். சரியான போர்டோ கலவை அல்லது ரிடோமில் மட்டுமே போதும்.",
                "audio_script_ta": "உழவரே கவனம்! உங்கள் தக்காளியில் பிற்கால கருகல் நோய் தாக்கியுள்ளது. இது வேகமாகப் பரவும் நோய். உடனடியாக ஒரு சதவீத போர்டோ கலவை தெளிக்கவும். அல்லது மெட்டலாக்சில் மான்கோசெப் மருந்தை ஒரு லிட்டருக்கு இரண்டரை கிராம் கலந்து உடனடியாக மாலை நேரத்தில் அடியிலை நனையும்படி தெளிக்கவும்."
            }
        }
    },

    "brinjal": {
        "name_ta": "🍆 கத்தரிக்காய் (Brinjal / Eggplant)",
        "name_en": "Brinjal / Eggplant",
        "category": "vegetable",
        "diseases": {
            "shoot_fruit_borer": {
                "name_ta": "கத்தரி தண்டு மற்றும் காய் துளைப்பான் (Shoot & Fruit Borer)",
                "name_en": "Brinjal Shoot & Fruit Borer (Leucinodes orbonalis)",
                "pathogen": "Insect Pest: Leucinodes orbonalis",
                "severity": "High (அதிகம்)",
                "symptoms_ta": "குருத்துகள் வாடி தொங்கும். காய்களில் துளைகள் மற்றும் புழுக்களின் கழிவுகள் காணப்படும். விளைச்சல் 50% வரை குறையும்.",
                "symptoms_en": "Wilting shoots, entry holes plugged with excreta in fruits, unmarketable harvest.",
                "organic_solution": {
                    "title_ta": "🌿 இயற்கை நாட்டு மருத்துவம் (Organic Remedy)",
                    "recipe_ta": "வேப்பெண்ணெய் 3% + இனக்கவர்ச்சிப் பொறி (Pheromone Traps)",
                    "preparation_ta": [
                        "ஏக்கருக்கு 5 லூசி லூர் இனக்கவர்ச்சி பொறிகளை (Pheromone traps) அமைத்து ஆண் அந்துப்பூச்சிகளை அழிக்கவும்.",
                        "30 மில்லி வேப்பெண்ணெய் + 5 மில்லி காதி சோப்பு லிட்டர் தண்ணீரில் கலந்து 7 நாட்கள் இடைவெளியில் தெளிக்கவும்.",
                        "தாக்கப்பட்ட குருத்துகளை புழுவுடன் கிள்ளி எடுத்து மண்ணில் புதைக்கவும்."
                    ],
                    "cost_estimate_inr": "₹150 / ஏக்கர்",
                    "frequency": "வாரத்திற்கு ஒருமுறை"
                },
                "chemical_solution": {
                    "title_ta": "🧪 பரிந்துரைக்கப்படும் இரசாயன மருந்து & அளவு (Safe Chemical Dosage)",
                    "medicine_name": "Chlorantraniliprole 18.5% SC (கொராசின் / Coragen)",
                    "dosage_ta": "0.3 மில்லி / 1 லிட்டர் தண்ணீர் (10 லிட்டர் டேங்கிற்கு 3 மில்லி மட்டுமே!).",
                    "dosage_en": "0.3ml per 1 Liter of water.",
                    "safety_interval_phi": "அறுவடைக்கு 5 நாட்களுக்கு முன்.",
                    "safety_precautions_ta": "அளவை கூட்டாதீர்கள். காய் பறித்த உடனேயே தெளிப்பது நன்று.",
                    "cost_estimate_inr": "₹650 / ஏக்கர்"
                },
                "debt_prevention_tip": "கத்தரிக்கு வாராவாரம் 4 மருந்து அடிப்பதை விட இனக்கவர்ச்சி பொறி வைத்தால் 70% புழுக்கள் மாட்டிவிடும். மருந்து செலவு மிச்சம்!",
                "audio_script_ta": "உழவரே, உங்கள் கத்தரி செடியில் தண்டு மற்றும் காய் துளைப்பான் புழு தாக்கியுள்ளது. ஏக்கருக்கு 5 இனக்கவர்ச்சி பொறி வையுங்கள். தாக்கப்பட்ட குருத்துகளை புழுவோடு கிள்ளி எறியுங்கள். வேப்பெண்ணெய் 30 மில்லி தெளித்தால் புழுக்கள் முட்டையிடுவது நிற்கும்."
            },
            "little_leaf": {
                "name_ta": "கத்தரி சிறு இலை நோய் (Little Leaf of Brinjal)",
                "name_en": "Little Leaf of Brinjal (Phytoplasma)",
                "pathogen": "Phytoplasma (தத்துப்பூச்சி மூலம் பரவுகிறது)",
                "severity": "Medium - High",
                "symptoms_ta": "இலைகள் மிகச்சிறியதாக மாறி செடி புதர் போல வளரும். பூக்காது, காய்க்காது.",
                "symptoms_en": "Extreme reduction in leaf size, bushy appearance, leaves turn soft and pale.",
                "organic_solution": {
                    "title_ta": "🌿 இயற்கை முறை",
                    "recipe_ta": "வேப்பங்கொட்டை சாறு 5% + பாதிக்கப்பட்ட செடியை அகற்றுதல்",
                    "preparation_ta": [
                        "நோய் தாக்கிய செடியை உடனே வேருடன் பிடுங்கி அப்புறப்படுத்தவும்.",
                        "தத்துப்பூச்சியை விரட்ட வேப்பங்கொட்டை சாறு 5% தெளிக்கவும்."
                    ],
                    "cost_estimate_inr": "₹80 / ஏக்கர்",
                    "frequency": "10 நாட்களுக்கு ஒருமுறை"
                },
                "chemical_solution": {
                    "title_ta": "🧪 பரிந்துரைக்கப்படும் மருந்து",
                    "medicine_name": "Dimethoate 30% EC (ரோகார்)",
                    "dosage_ta": "1.5 மில்லி / லிட்டர் தண்ணீர்.",
                    "dosage_en": "1.5ml per Liter of water.",
                    "safety_interval_phi": "10 நாட்கள்.",
                    "safety_precautions_ta": "பூ பூக்கும் போது தெளிக்கக் கூடாது.",
                    "cost_estimate_inr": "₹320 / ஏக்கர்"
                },
                "debt_prevention_tip": "சிறு இலை நோய்க்கு மருந்து அடித்து பயனில்லை, செடியை பிடுங்கி விட்டு தத்துப்பூச்சியை கட்டுப்படுத்தினாலே போதும்.",
                "audio_script_ta": "உழவரே, உங்கள் கத்தரியில் சிறு இலை நோய் உள்ளது. இந்த செடி காய்க்காது என்பதால் உடனே பிடுங்கி எறியுங்கள். தத்துப்பூச்சியை அழிக்க வேப்பங்கொட்டை சாறு தெளிக்கவும்."
            }
        }
    },

    "chilli": {
        "name_ta": "🌶️ மிளகாய் (Chilli / Pepper)",
        "name_en": "Chilli / Pepper",
        "category": "vegetable",
        "diseases": {
            "anthracnose_dieback": {
                "name_ta": "மிளகாய் நுனிக்கருகல் & பழ அழுகல் (Anthracnose / Dieback)",
                "name_en": "Chilli Anthracnose & Fruit Rot (Colletotrichum capsici)",
                "pathogen": "Fungus: Colletotrichum capsici",
                "severity": "High (அதிகம்)",
                "symptoms_ta": "கிளைகளின் நுனியிலிருந்து கீழ்நோக்கி காய்ந்து கருகி வரும். பழுத்த மிளகாயில் வட்ட வடிவ பள்ளமான கருப்பு திட்டுகள் தோன்றும்.",
                "symptoms_en": "Die-back of twigs from top downward, circular sunken black spots with concentric rings on ripe fruits.",
                "organic_solution": {
                    "title_ta": "🌿 இயற்கை நாட்டு மருத்துவம் (Organic Remedy)",
                    "recipe_ta": "சூடோமோனாஸ் புளோரசன்ஸ் 1% + போர்டோ கலவை 1%",
                    "preparation_ta": [
                        "10 கிராம் சூடோமோனாஸ் ஒரு லிட்டர் நீரில் கலந்து தெளிக்கவும் அல்லது 1% போர்டோ கலவை தெளிக்கவும்."
                    ],
                    "cost_estimate_inr": "₹120 / ஏக்கர்",
                    "frequency": "10 நாட்கள் இடைவெளியில்"
                },
                "chemical_solution": {
                    "title_ta": "🧪 பரிந்துரைக்கப்படும் இரசாயன மருந்து & அளவு (Safe Chemical Dosage)",
                    "medicine_name": "Azoxystrobin 18.2% + Difenoconazole 11.4% SC (அமிஸ்டார் டாப்)",
                    "dosage_ta": "1 மில்லி / 1 லிட்டர் தண்ணீர்.",
                    "dosage_en": "1.0ml per 1 Liter of water.",
                    "safety_interval_phi": "அறுவடைக்கு 7 நாட்களுக்கு முன்.",
                    "safety_precautions_ta": "காலை நேரத்தில் காய்கள் காய்ந்த பின் அடிக்கவும்.",
                    "cost_estimate_inr": "₹700 / ஏக்கர்"
                },
                "debt_prevention_tip": "நுனிக்கருகல் வந்தால் உடனடியாக தாக்கப்பட்ட நுனிகளை கவாத்து செய்து அகற்றுங்கள். வெறும் மருந்தை மட்டும் நம்பி பணம் இழக்காதீர்கள்.",
                "audio_script_ta": "உழவரே, உங்கள் மிளகாயில் நுனிக்கருகல் மற்றும் பழ அழுகல் நோய் உள்ளது. காய்ந்த நுனிகளை கத்தரித்து அப்புறப்படுத்துங்கள். ஒரு லிட்டருக்கு 10 கிராம் சூடோமோனாஸ் அல்லது 1 மில்லி அமிஸ்டார் டாப் கலந்து தெளிக்கவும்."
            }
        }
    },

    "okra": {
        "name_ta": "🌱 வெண்டைக்காய் (Okra / Ladies Finger)",
        "name_en": "Okra / Ladies Finger",
        "category": "vegetable",
        "diseases": {
            "yellow_vein_mosaic": {
                "name_ta": "வெண்டை நரம்பு வெளுத்தல் நோய் (Yellow Vein Mosaic Virus)",
                "name_en": "Yellow Vein Mosaic Virus (YVMV)",
                "pathogen": "Virus (வெள்ளை ஈ - Whitefly மூலம் பரவுகிறது)",
                "severity": "Critical (விளைச்சல் முற்றிலும் குறையும்)",
                "symptoms_ta": "இலைகளின் நரம்புகள் மஞ்சள் நிறமாக வெளுத்து வலைப்பின்னல் போல மாறும். காய்கள் மஞ்சள் நிறமாக தடித்து சிறுத்துவிடும்.",
                "symptoms_en": "Alternating network of yellow veins and green lamina, fruits become dwarf and yellow-green.",
                "organic_solution": {
                    "title_ta": "🌿 இயற்கை நாட்டு மருத்துவம் (Organic Remedy)",
                    "recipe_ta": "மஞ்சள் ஒட்டும் பொறி + வேப்பெண்ணெய் 3%",
                    "preparation_ta": [
                        "ஏக்கருக்கு 12 மஞ்சள் நிற ஒட்டும் பொறிகளை பயிர் மட்டத்தில் அமைத்து வெள்ளை ஈக்களைப் பிடிக்கவும்.",
                        "வேப்பெண்ணெய் 30 மில்லி + காதி சோப்பு லிட்டர் தண்ணீரில் தெளிக்கவும்."
                    ],
                    "cost_estimate_inr": "₹150 / ஏக்கர்",
                    "frequency": "7 நாட்கள் இடைவெளியில்"
                },
                "chemical_solution": {
                    "title_ta": "🧪 பரிந்துரைக்கப்படும் இரசாயன மருந்து & அளவு (Safe Chemical Dosage)",
                    "medicine_name": "Acetamiprid 20% SP அல்லது Thiamethoxam 25% WG",
                    "dosage_ta": "0.5 கிராம் தயமீதாக்சம் / 1 லிட்டர் தண்ணீர்.",
                    "dosage_en": "0.5g Thiamethoxam per Liter of water.",
                    "safety_interval_phi": "5 நாட்கள்.",
                    "safety_precautions_ta": "பிஞ்சு காய்கள் பறித்த உடனேயே தெளிக்கவும்.",
                    "cost_estimate_inr": "₹380 / ஏக்கர்"
                },
                "debt_prevention_tip": "வைரஸ் நோய்க்கு பூஞ்சாண மருந்து அடிக்கக் கூடாது. வெள்ளை ஈயை கட்டுப்படுத்தினாலே நோய் பரவாது!",
                "audio_script_ta": "உழவரே, உங்கள் வெண்டையில் மஞ்சள் நரம்பு வைரஸ் நோய் வெள்ளை ஈக்கள் மூலம் பரவுகிறது. மஞ்சள் ஒட்டும் பொறி வையுங்கள். தயமீதாக்சம் மருந்தை குறைந்த அளவில் தெளித்து வெள்ளை ஈயை கட்டுப்படுத்துங்கள்."
            }
        }
    },

    # ==========================
    # FRUITS & FRUIT TREES (பழங்கள் & பழ மரங்கள்)
    # ==========================
    "banana": {
        "name_ta": "🍌 வாழை (Banana)",
        "name_en": "Banana",
        "category": "fruit",
        "diseases": {
            "sigatoka": {
                "name_ta": "வாழை சிகடோகா இலைப்புள்ளி நோய் (Sigatoka Leaf Spot)",
                "name_en": "Sigatoka Leaf Spot (Mycosphaerella musicola)",
                "pathogen": "Fungus: Pseudocercospora musae",
                "severity": "High (அதிகம் - தார் எடை குறையும்)",
                "symptoms_ta": "இலைகளில் சிறிய நீள்வட்ட வடிவ மஞ்சள் புள்ளிகள் தோன்றி, பின் பழுப்பு நிறமாகி நடுப்பகுதி சாம்பல் நிறத்தில் காய்ந்து விடும். இலைகள் முன்கூட்டியே கருகி உதிரும்.",
                "symptoms_en": "Spindle-shaped yellow streaks maturing to dark brown oval lesions with grey centers and yellow halos.",
                "organic_solution": {
                    "title_ta": "🌿 இயற்கை நாட்டு மருத்துவம் (Organic Remedy)",
                    "recipe_ta": "சூடோமோனாஸ் புளோரசன்ஸ் 2% + பாதிக்கப்பட்ட இலை நீக்கம்",
                    "preparation_ta": [
                        "காய்ந்த பாதிக்கப்பட்ட இலைகளை கவாத்து செய்து வெட்டி அப்புறப்படுத்தவும்.",
                        "20 கிராம் சூடோமோனாஸ் புளோரசன்ஸ் + 10 மில்லி ஒட்டும் திரவத்தை ஒரு லிட்டர் நீரில் கலந்து இலைகளின் அடிப்புறம் நனையும்படி தெளிக்கவும்."
                    ],
                    "cost_estimate_inr": "₹200 / ஏக்கர்",
                    "frequency": "15 நாட்கள் இடைவெளியில்"
                },
                "chemical_solution": {
                    "title_ta": "🧪 பரிந்துரைக்கப்படும் இரசாயன மருந்து & அளவு (Safe Chemical Dosage)",
                    "medicine_name": "Propiconazole 25% EC (டில்ட்) + Mineral Oil (வாழை எண்ணெய்)",
                    "dosage_ta": "1 மில்லி புரோபிகோனசோல் + 10 மில்லி மினரல் ஆயில் / 1 லிட்டர் தண்ணீர்.",
                    "dosage_en": "1.0ml Propiconazole + 10ml mineral oil per 1 Liter of water.",
                    "safety_interval_phi": "அறுவடைக்கு 20 நாட்களுக்கு முன்.",
                    "safety_precautions_ta": "தார் போடும் தருணத்தில் இலைகள் ஆரோக்கியமாக இருப்பது தாரின் எடைக்கு மிக முக்கியம்.",
                    "cost_estimate_inr": "₹750 / ஏக்கர்"
                },
                "debt_prevention_tip": "வாழையில் காய்ந்த இலைகளை வெட்டி வயலுக்கு வெளியே அப்புறப்படுத்தினாலே 50% சிகடோகா நோய் பரவாது. மருந்து செலவை பாதியாக குறைக்கலாம்!",
                "audio_script_ta": "வணக்கம் உழவரே! உங்கள் வாழை மரத்தில் சிகடோகா இலைப்புள்ளி நோய் தாக்கியுள்ளது. முதலில் காய்ந்த இலைகளை வெட்டி வயலுக்கு வெளியே தள்ளுங்கள். சூடோமோனாஸ் 20 கிராம் அல்லது புரோபிகோனசோல் ஒரு மில்லி வீதம் வாழை எண்ணெயுடன் கலந்து இலைகளின் அடிப்பகுதியில் தெளிக்கவும்."
            },
            "panama_wilt": {
                "name_ta": "வாழை பனாமா வாடல் நோய் (Panama Wilt)",
                "name_en": "Panama Wilt (Fusarium oxysporum f. sp. cubense)",
                "pathogen": "Soil-borne Fungus: Fusarium oxysporum",
                "severity": "Critical (மரம் முற்றிலும் பட்டுப்போகும்)",
                "symptoms_ta": "கீழ்மட்ட இலைகள் மஞ்சளாகி காம்புடன் ஒடிந்து தொங்கும். தண்டின் உள்பகுதி செம்பழுப்பு நிறமாக மாறி அழுகிய துர்நாற்றம் வீசும்.",
                "symptoms_en": "Yellowing of lower leaf margins, collapse of petiole forming skirt around pseudostem, vascular browning.",
                "organic_solution": {
                    "title_ta": "🌿 இயற்கை நாட்டு மருத்துவம் (Organic Remedy)",
                    "recipe_ta": "டிரைக்கோடெர்மா விரிடி (Trichoderma viride) வேர்ப்பகுதியில் இடுதல்",
                    "preparation_ta": [
                        "50 கிராம் டிரைக்கோடெர்மா விரிடி நுண்ணுயிரியை மக்கிய தொழுவுரத்துடன் கலந்து மரத்தின் வேர்ப்பகுதியில் இட்டு பாசனம் செய்யவும்."
                    ],
                    "cost_estimate_inr": "₹150 / 100 மரங்களுக்கு",
                    "frequency": "மாதம் ஒருமுறை"
                },
                "chemical_solution": {
                    "title_ta": "🧪 பரிந்துரைக்கப்படும் இரசாயன முறை",
                    "medicine_name": "Carbendazim 50% WP (பாவிஸ்டின்)",
                    "dosage_ta": "2 கிராம் கார்பென்டாசிம் / லிட்டர் தண்ணீரில் கரைத்து மரத்தின் வேர் பகுதியில் ஊற்றவும் (Soil Drenching).",
                    "dosage_en": "2g Carbendazim per Liter drenching root zone.",
                    "safety_interval_phi": "30 நாட்கள்.",
                    "safety_precautions_ta": "நோய் தாக்கிய கன்றுகளை நடவு செய்யக் கூடாது.",
                    "cost_estimate_inr": "₹400 / 100 மரங்களுக்கு"
                },
                "debt_prevention_tip": "பனாமா நோய் நிலத்தின் வேரில் பரவுகிறது. மேல் தெளிக்கும் மருந்துகளை வாங்கி பணத்தை விரயம் செய்யாதீர்கள்; வேர்ப்பகுதியில் டிரைக்கோடெர்மா இடவும்.",
                "audio_script_ta": "உழவரே, உங்கள் வாழையில் பனாமா வாடல் நோய் அறிகுறி தென்படுகிறது. மரத்தின் அடியில் தேங்கும் தண்ணீரை வடித்துவிட்டு, வேர்ப்பகுதியில் டிரைக்கோடெர்மா மற்றும் கார்பென்டாசிம் கரைத்து ஊற்றுங்கள்."
            }
        }
    },

    "mango": {
        "name_ta": "🥭 மாமரம் (Mango)",
        "name_en": "Mango",
        "category": "fruit",
        "diseases": {
            "anthracnose": {
                "name_ta": "மாமரம் ஆந்த்ராக்னோஸ் இலை & பழக்கருகல் (Mango Anthracnose)",
                "name_en": "Mango Anthracnose (Colletotrichum gloeosporioides)",
                "pathogen": "Fungus: Colletotrichum gloeosporioides",
                "severity": "High (பூக்கள் மற்றும் பிஞ்சுகள் உதிரும்)",
                "symptoms_ta": "இலைகளில் ஒழுங்கற்ற பழுப்பு மற்றும் கறுப்பு நிறப் புள்ளிகள். பூங்கொத்துகள் கருகி உதிரும். காய்களில் கரும்புள்ளிகள் தோன்றி அழுகும்.",
                "symptoms_en": "Blossom blight, black spots on tender leaves, black tear-stain markings on ripening fruits.",
                "organic_solution": {
                    "title_ta": "🌿 இயற்கை நாட்டு மருத்துவம் (Organic Remedy)",
                    "recipe_ta": "1% போர்டோ கலவை அல்லது பஞ்சகவ்யா தெளிப்பு",
                    "preparation_ta": [
                        "மயில் துத்தம் மற்றும் நீற்று சுண்ணாம்பு கலந்த 1% போர்டோ கலவை பூ மலர்வதற்கு முன்பும், பிஞ்சு பிடித்த பின்னும் தெளிக்கவும்."
                    ],
                    "cost_estimate_inr": "₹250 / ஏக்கர் (தோப்பு)",
                    "frequency": "பூக்கும் தருணத்தில்"
                },
                "chemical_solution": {
                    "title_ta": "🧪 பரிந்துரைக்கப்படும் இரசாயன மருந்து & அளவு (Safe Chemical Dosage)",
                    "medicine_name": "Azoxystrobin 23% SC அல்லது Carbendazim 12% + Mancozeb 63% WP (சாப்)",
                    "dosage_ta": "2 கிராம் சாப் மருந்து / 1 லிட்டர் தண்ணீர்.",
                    "dosage_en": "2.0g Carbendazim + Mancozeb per 1 Liter of water.",
                    "safety_interval_phi": "அறுவடைக்கு 15 நாட்களுக்கு முன்.",
                    "safety_precautions_ta": "பூ பூக்கும் உச்சக்கட்டத்தில் தேனீக்கள் இருக்கும் போது ரசாயனம் தெளிக்காதீர்கள்.",
                    "cost_estimate_inr": "₹600 / ஏக்கர்"
                },
                "debt_prevention_tip": "பூ பிடிக்கும் முன் போர்டோ கலவை அடித்துவிட்டால் பிஞ்சு உதிர்வது தடுத்து மாங்காய் மகசூல் இரட்டிப்பாகும். விலை உயர்ந்த டானிக்குகள் தேவையில்லை!",
                "audio_script_ta": "உழவரே, உங்கள் மாமரத்தில் ஆந்த்ராக்னோஸ் பூஞ்சாணம் தாக்கியுள்ளது. பூக்கள் மற்றும் இலைகள் கருகாமல் பாதுகாக்க ஒரு சதவீத போர்டோ கலவை அல்லது லிட்டருக்கு 2 கிராம் சாப் மருந்தை மரங்கள் நன்கு நனையும்படி தெளிக்கவும்."
            }
        }
    },

    "citrus": {
        "name_ta": "🍋 எலுமிச்சை / சிட்ரஸ் (Citrus / Lemon)",
        "name_en": "Citrus / Lemon",
        "category": "fruit",
        "diseases": {
            "citrus_canker": {
                "name_ta": "எலுமிச்சை திட்டு நோய் / கேங்கர் (Citrus Canker)",
                "name_en": "Citrus Canker (Xanthomonas axonopodis pv. citri)",
                "pathogen": "Bacteria: Xanthomonas axonopodis",
                "severity": "High (காய்களின் சந்தை மதிப்பு குறையும்)",
                "symptoms_ta": "இலைகள், கிளைகள் மற்றும் பழங்களில் சொறி போன்ற மேடான பழுப்பு நிறப் புள்ளிகள் தோன்றும். புள்ளியைச் சுற்றி மஞ்சள் வளையம் காணப்படும்.",
                "symptoms_en": "Raised corky crater-like lesions on leaves, stems, and fruits surrounded by a distinctive oily yellow halo.",
                "organic_solution": {
                    "title_ta": "🌿 இயற்கை நாட்டு மருத்துவம் (Organic Remedy)",
                    "recipe_ta": "வேப்பிலை கரைசல் 5% + காய்ந்த கிளைகளை கவாத்து செய்தல்",
                    "preparation_ta": [
                        "தாக்கப்பட்ட கிளைகளை கவாத்து செய்து எரித்துவிட்டு, வெட்டிய இடத்தில் போர்டோ பசையைத் தடவவும்.",
                        "வேப்பிலை கரைசல் 5% தெளித்து இலை துளைப்பானை (Leaf Miner) கட்டுப்படுத்தவும்."
                    ],
                    "cost_estimate_inr": "₹100 / ஏக்கர்",
                    "frequency": "மழைக்காலத்திற்கு பின்"
                },
                "chemical_solution": {
                    "title_ta": "🧪 பரிந்துரைக்கப்படும் இரசாயன மருந்து & அளவு (Safe Chemical Dosage)",
                    "medicine_name": "Streptocycline (1g) + Copper Oxychloride (25g) / 10L Water",
                    "dosage_ta": "1 கிராம் ஸ்ட்ரெப்டோசைக்ளின் + 25 கிராம் காப்பர் ஆக்ஸிகுளோரைடு / 10 லிட்டர் தண்ணீர்.",
                    "dosage_en": "1g Streptocycline + 25g Copper Oxychloride per 10 Liters of water.",
                    "safety_interval_phi": "14 நாட்கள்.",
                    "safety_precautions_ta": "மழைக்கு முன் மற்றும் மழை நின்ற பின் தெளிக்கவும்.",
                    "cost_estimate_inr": "₹450 / ஏக்கர்"
                },
                "debt_prevention_tip": "எலுமிச்சை கேங்கருக்கு வெறும் பூஞ்சாணக் கொல்லி பயனளிக்காது; பாக்டீரியா மருந்து மட்டுமே வேலை செய்யும். வீண் செலவை தவிருங்கள்.",
                "audio_script_ta": "உழவரே, உங்கள் எலுமிச்சையில் கேங்கர் திட்டு நோய் உள்ளது. தாக்கப்பட்ட கிளைகளை கவாத்து செய்துவிட்டு, 10 லிட்டர் தண்ணீருக்கு ஒரு கிராம் ஸ்ட்ரெப்டோசைக்ளின் மற்றும் 25 கிராம் காப்பர் ஆக்ஸிகுளோரைடு கலந்து தெளிக்கவும்."
            }
        }
    },

    "papaya": {
        "name_ta": "🍈 பப்பாளி (Papaya)",
        "name_en": "Papaya",
        "category": "fruit",
        "diseases": {
            "ringspot_virus": {
                "name_ta": "பப்பாளி வளையப்புள்ளி வைரஸ் நோய் (Papaya Ringspot Virus - PRSV)",
                "name_en": "Papaya Ringspot Virus",
                "pathogen": "Potyvirus (அசுவினிப் பூச்சி மூலம் பரவுகிறது)",
                "severity": "Critical (காய்கள் சுவை இழக்கும்)",
                "symptoms_ta": "இலைகளில் மஞ்சள் பச்சை நிற வளையங்கள், இலைகள் தோல் போல மெலிந்து போகும். காய்களில் வட்ட வடிவ வளையப் புள்ளிகள் தோன்றும்.",
                "symptoms_en": "Shoestring leaves, yellow mosaic patterns, dark green water-soaked rings on fruit and petioles.",
                "organic_solution": {
                    "title_ta": "🌿 இயற்கை முறை",
                    "recipe_ta": "எல்லைப் பயிராக மக்காச்சோளம் நடுதல் + வேப்பெண்ணெய் 3%",
                    "preparation_ta": [
                        "பப்பாளி தோட்டத்தைச் சுற்றி 3 வரிசை மக்காச்சோளம் விதைத்து அசுவினிப் பூச்சிகளை தடுத்து நிறுத்தவும்.",
                        "வேப்பெண்ணெய் 30 மில்லி / லிட்டர் தெளித்து அசுவினியை விரட்டவும்."
                    ],
                    "cost_estimate_inr": "₹200 / ஏக்கர்",
                    "frequency": "வளரும் பருவம் முழுவதும்"
                },
                "chemical_solution": {
                    "title_ta": "🧪 பரிந்துரைக்கப்படும் இரசாயனம்",
                    "medicine_name": "Dimethoate 30% EC அல்லது Imidacloprid 17.8% SL",
                    "dosage_ta": "0.5 மில்லி இமிடாக்ளோப்ரிட் / 1 லிட்டர் தண்ணீர்.",
                    "dosage_en": "0.5ml Imidacloprid per Liter.",
                    "safety_interval_phi": "10 நாட்கள்.",
                    "safety_precautions_ta": "அசுவினிப் பூச்சியை கட்டுப்படுத்துவதே முக்கியம்.",
                    "cost_estimate_inr": "₹350 / ஏக்கர்"
                },
                "debt_prevention_tip": "வைரஸுக்கு மருந்து அடிக்காதீர்கள்; எல்லை பயிராக மக்காச்சோளம் போட்டாலே பூச்சிகள் உள்ளே வராது!",
                "audio_script_ta": "உழவரே, உங்கள் பப்பாளியில் வளையப்புள்ளி வைரஸ் நோய் பரவியுள்ளது. அசுவினிப் பூச்சியைக் கட்டுப்படுத்த வேப்பெண்ணெய் அல்லது இமிடாக்ளோப்ரிட் தெளிக்கவும்."
            }
        }
    },

    # ==========================
    # TREES & PLANTATION (மரங்கள் & தோட்டங்கள்)
    # ==========================
    "coconut": {
        "name_ta": "🌴 தென்னை மரம் (Coconut Tree)",
        "name_en": "Coconut Tree",
        "category": "tree",
        "diseases": {
            "leaf_rot": {
                "name_ta": "தென்னை இலை அழுகல் நோய் (Coconut Leaf Rot)",
                "name_en": "Coconut Leaf Rot (Bipolaris incurvata / Colletotrichum)",
                "pathogen": "Fungus Complex: Bipolaris / Colletotrichum",
                "severity": "High (குருத்து பட்டுப்போகும்)",
                "symptoms_ta": "குருத்து ஓலைகளின் நுனி அழுகி கருப்பு நிறமாகி உலர்ந்து போகும். காற்று வீசும்போது ஓலைகள் ஒடிந்து தொங்கும்.",
                "symptoms_en": "Blackening and shrivelling of spear leaf distal leaflets, drying of spear and fan leaf rot.",
                "organic_solution": {
                    "title_ta": "🌿 இயற்கை நாட்டு மருத்துவம் (Organic Remedy)",
                    "recipe_ta": "வேப்பிலை சாறு + மரத்தின் உச்சியில் மணல் மற்றும் வேப்பம்பிண்ணாக்கு இடுதல்",
                    "preparation_ta": [
                        "அழுகிய இலை பாகங்களை வெட்டி அப்புறப்படுத்தவும்.",
                        "குருத்து மட்டையின் இடுக்குகளில் 250 கிராம் வேப்பம்பிண்ணாக்குடன் சம அளவு மணல் கலந்து வைக்கவும்."
                    ],
                    "cost_estimate_inr": "₹150 / 25 மரங்களுக்கு",
                    "frequency": "மழைக்காலத்திற்கு முன்"
                },
                "chemical_solution": {
                    "title_ta": "🧪 பரிந்துரைக்கப்படும் இரசாயன முறை",
                    "medicine_name": "Contaf 5% EC (Hexaconazole) அல்லது காப்பர் ஆக்ஸிகுளோரைடு",
                    "dosage_ta": "5 மில்லி ஹெக்சாகோனசோல் மருந்தை 300 மில்லி தண்ணீரில் கலந்து குருத்து மட்டையின் அடிப்பகுதியில் ஊற்றவும்.",
                    "dosage_en": "5ml Hexaconazole in 300ml water poured around crown.",
                    "safety_interval_phi": "இல்லை (Crown treatment).",
                    "safety_precautions_ta": "உச்சி மட்டைகளில் மருந்து படும்படி இடவும்.",
                    "cost_estimate_inr": "₹300 / 25 மரங்களுக்கு"
                },
                "debt_prevention_tip": "தென்னைக்கு தேவையில்லாமல் காஸ்ட்லி டானிக்குகளை ஊற்றாதீர்கள். வேப்பம்பிண்ணாக்கு மற்றும் மணல் கலவையே வண்டுகளையும் அழுகலையும் விரட்டும்!",
                "audio_script_ta": "வணக்கம் உழவரே! உங்கள் தென்னை மரத்தில் குருத்து இலை அழுகல் நோய் தென்படுகிறது. அழுகிய பாகங்களை வெட்டிவிட்டு, மரத்தின் உச்சியில் வேப்பம்பிண்ணாக்கு மற்றும் மணல் சம அளவு கலந்து வையுங்கள். ஹெக்சாகோனசோல் 5 மில்லி மருந்தை குருத்தில் ஊற்றவும்."
            },
            "tanjore_wilt": {
                "name_ta": "தென்னை தஞ்சாவூர் வாடல் நோய் (Thanjavur Wilt / Ganoderma)",
                "name_en": "Thanjavur Wilt / Basal Stem Rot (Ganoderma lucidum)",
                "pathogen": "Fungus: Ganoderma lucidum",
                "severity": "Critical (மரம் அழுகி சாய்ந்துவிடும்)",
                "symptoms_ta": "அடிமரத்தில் செம்பழுப்பு நிற திரவம் கசிந்து வழியும். கீழ் ஓலைகள் மஞ்சளாகி உதிரும். மரத்தின் வேர்கள் அழுகி மரம் சாய்ந்துவிடும்.",
                "symptoms_en": "Reddish brown gummy exudation from trunk base, drooping of outer leaves, decaying roots.",
                "organic_solution": {
                    "title_ta": "🌿 இயற்கை முறை",
                    "recipe_ta": "வேப்பம்பிண்ணாக்கு 5 கிலோ + சூடோமோனாஸ் மரத்தை சுற்றி இடுதல்",
                    "preparation_ta": [
                        "மரம் ஒன்றுக்கு 5 கிலோ வேப்பம்பிண்ணாக்கு மற்றும் 200 கிராம் சூடோமோனாஸ் தூளை வேர்ப்பகுதியில் இட்டு பாசனம் செய்யவும்."
                    ],
                    "cost_estimate_inr": "₹180 / மரம்",
                    "frequency": "6 மாதத்திற்கு ஒருமுறை"
                },
                "chemical_solution": {
                    "title_ta": "🧪 பரிந்துரைக்கப்படும் முறை (வேர் மூலம் ஏற்றுதல் - Root Feeding)",
                    "medicine_name": "Aureofungin-sol (2g) + Copper Sulphate (1g) அல்லது Hexaconazole (2ml)",
                    "dosage_ta": "2 மில்லி ஹெக்சாகோனசோல் மருந்தை 100 மில்லி நீரில் கலந்து மரத்தின் உயிருள்ள வேர் வழியே ஏற்றவும் (Root Feeding).",
                    "dosage_en": "2ml Hexaconazole in 100ml water root feeding.",
                    "safety_interval_phi": "45 நாட்கள் இளநீர் பறிக்கக் கூடாது.",
                    "safety_precautions_ta": "நோய் தாக்கிய மரத்தைச் சுற்றி வடிகால் வாய்க்கால் வெட்டி நோய் பரவலை தடுக்கவும்.",
                    "cost_estimate_inr": "₹120 / மரம்"
                },
                "debt_prevention_tip": "தஞ்சாவூர் வாடல் வந்தால் மற்ற மரங்களுக்கு பரவாமல் தடுக்க உடனே சுற்றி அகழி வெட்டுங்கள். ஒரே மரத்தை காப்பாற்ற அதிக செலவு செய்வதை விட மற்ற மரங்களை பாதுகாப்பதே புத்திசாலித்தனம்.",
                "audio_script_ta": "உழவரே, உங்கள் தென்னையில் தஞ்சாவூர் வாடல் நோய் அறிகுறி தெரிகிறது. மரத்தின் அடியில் வேப்பம்பிண்ணாக்கு இடுங்கள். ஹெக்சாகோனசோல் மருந்தை வேர் வழியாக ஏற்றி மற்ற மரங்களுக்கு பரவாமல் சுற்றிலும் வாய்க்கால் வெட்டுங்கள்."
            }
        }
    },

    "tea_coffee": {
        "name_ta": "☕ தேயிலை & காபி (Tea & Coffee)",
        "name_en": "Tea & Coffee Plantation",
        "category": "tree",
        "diseases": {
            "blister_blight": {
                "name_ta": "தேயிலை கொப்புள நோய் (Blister Blight of Tea)",
                "name_en": "Tea Blister Blight (Exobasidium vexans)",
                "pathogen": "Fungus: Exobasidium vexans",
                "severity": "High (கொழுந்து இலைகள் அழுகும்)",
                "symptoms_ta": "இளந்தளிர்களில் வட்ட வடிவ வெளிர் நிற கொப்புளங்கள் தோன்றும். பின் அடியில் வெள்ளை நிற பூஞ்சாண தூள் படிந்து இலைகள் சுருங்கும்.",
                "symptoms_en": "Translucent circular spots turning into blister-like depressions, white velvety fungal sporulation.",
                "organic_solution": {
                    "title_ta": "🌿 இயற்கை முறை",
                    "recipe_ta": "சூடோமோனாஸ் தெளிப்பு + நிழல் மேலாண்மை",
                    "preparation_ta": [
                        "நிழல் மரங்களின் கிளைகளை கவாத்து செய்து சூரிய ஒளி படும்படி செய்யவும்.",
                        "சூடோமோனாஸ் 10 கிராம் / லிட்டர் நீரில் கலந்து தெளிக்கவும்."
                    ],
                    "cost_estimate_inr": "₹220 / ஏக்கர்",
                    "frequency": "7 நாட்கள் இடைவெளியில்"
                },
                "chemical_solution": {
                    "title_ta": "🧪 பரிந்துரைக்கப்படும் இரசாயனம்",
                    "medicine_name": "Copper Oxychloride (210g) + Hexaconazole (200ml) / ஹெக்டேர்",
                    "dosage_ta": "காப்பர் ஆக்ஸிகுளோரைடு 1.5 கிராம் / 1 லிட்டர் தண்ணீர்.",
                    "dosage_en": "1.5g Copper Oxychloride per Liter.",
                    "safety_interval_phi": "கொழுந்து பறிப்பதற்கு 7 நாட்களுக்கு முன்.",
                    "safety_precautions_ta": "மழைக்காலத்தில் தொடர் தெளிப்பு தேவை.",
                    "cost_estimate_inr": "₹550 / ஏக்கர்"
                },
                "debt_prevention_tip": "தோட்டத்தில் அதிக நிழலை தவிர்த்து சரியான கவாத்து செய்தாலே கொப்புள நோய் 50% குறையும்.",
                "audio_script_ta": "உழவரே, உங்கள் தேயிலையில் கொப்புள நோய் தென்படுகிறது. நிழல் கிளைகளை கவாத்து செய்துவிட்டு, காப்பர் ஆக்ஸிகுளோரைடு குறைந்த அளவில் தெளிக்கவும்."
            }
        }
    },

    # ==========================
    # CEREALS & CASH CROPS (தானியங்கள் & பணப்பயிர்கள்)
    # ==========================
    "rice": {
        "name_ta": "🌾 நெல் / நெற்பயிர் (Paddy / Rice)",
        "name_en": "Rice / Paddy",
        "category": "cereal",
        "diseases": {
            "blast": {
                "name_ta": "நெல் குலை நோய் (Paddy Blast)",
                "name_en": "Rice Blast (Pyricularia oryzae)",
                "pathogen": "Fungus: Pyricularia oryzae",
                "severity": "Very High (மிக அதிகம் - நெல் தானியம் பாதிக்கப்படலாம்)",
                "symptoms_ta": "இலைகளில் கதிர் வடிவில் (கண் வடிவில் / Spindle shape) சாம்பல் நிற மையமும் பழுப்பு நிற ஓரமும் கொண்ட புள்ளிகள் தோன்றும். கணு மற்றும் கழுத்துப்பகுதி தாக்கினால் நெல் மணிகள் பதராகிவிடும்.",
                "symptoms_en": "Spindle-shaped lesions with gray/whitish centers and reddish-brown borders. Severe infections cause neck rot and grain choking.",
                "organic_solution": {
                    "title_ta": "🌿 இயற்கை நாட்டு மருத்துவம் (Organic Remedy)",
                    "recipe_ta": "சூடோமோனாஸ் புளோரசன்ஸ் + வேப்பங்கொட்டை சாறு 5%",
                    "preparation_ta": [
                        "1 கிலோ சூடோமோனாஸ் புளோரசன்ஸ் நுண்ணுயிரியை 100 லிட்டர் நீரில் கலந்து மாலை நேரத்தில் தெளிக்கவும்.",
                        "அல்லது 5% வேப்பங்கொட்டை பருப்பு சாறு தயாரித்து தெளிக்கலாம்."
                    ],
                    "cost_estimate_inr": "₹120 / ஏக்கர்",
                    "frequency": "7 நாட்கள் இடைவெளியில்"
                },
                "chemical_solution": {
                    "title_ta": "🧪 பரிந்துரைக்கப்படும் இரசாயன மருந்து & அளவு (Safe Chemical Dosage)",
                    "medicine_name": "Tricyclazole 75% WP (ட்ரைசைக்ளசோல் - பாண்)",
                    "dosage_ta": "1 கிராம் மருந்து / 1 லிட்டர் தண்ணீர் (10 லிட்டர் தெளிப்பானுக்கு 10-12 கிராம்).",
                    "dosage_en": "1.0g per 1 Liter of water (Beam / Tricyclazole).",
                    "safety_interval_phi": "21 நாட்கள் இடைவெளி.",
                    "safety_precautions_ta": "தழைச்சத்து (யூரியா) இடுவதை உடனடியாக நிறுத்தவும்.",
                    "cost_estimate_inr": "₹450 / ஏக்கர்"
                },
                "debt_prevention_tip": "குலை நோய் வந்தால் யூரியாவை உடனடியாக நிறுத்த வேண்டும். மாறாக யூரியா போட்டால் நோய் பன்மடங்கு பெருகும்! டிரைசைக்ளசோல் 1 கிராம் போதுமானது; விலை உயர்ந்த கலவைகளை வாங்காதீர்கள்.",
                "audio_script_ta": "வணக்கம் உழவரே! உங்கள் நெற்பயிரில் குலை நோய் அதாவது பிளாஸ்ட் தாக்குதல் அறிகுறி தெரிகிறது. இலையில் கண் வடிவ புள்ளிகள் உள்ளன. முதலில் யூரியா உரம் இடுவதை உடனே நிறுத்துங்கள்! ஏக்கருக்கு ஒரு கிலோ சூடோமோனாஸ் அல்லது ட்ரைசைக்ளசோல் மருந்தை ஒரு லிட்டருக்கு ஒரு கிராம் வீதம் மாலை நேரத்தில் தெளிக்கவும்."
            },
            "bacterial_blight": {
                "name_ta": "பாக்டீரியா இலைக்கருகல் நோய் (Bacterial Leaf Blight - BLB)",
                "name_en": "Bacterial Leaf Blight (Xanthomonas oryzae)",
                "pathogen": "Bacteria: Xanthomonas oryzae pv. oryzae",
                "severity": "Critical (தீவிரமானது)",
                "symptoms_ta": "இலைகளின் நுனியிலிருந்து ஓரங்களில் அலை அலையான மஞ்சள் நிறக் கோடுகள் தோன்றி, பின்னர் வைக்கோல் நிறத்தில் காய்ந்து கருகிவிடும். காலை நேரத்தில் பாக்டீரியா திரவத் துளிகள் (Ooze) காணப்படும்.",
                "symptoms_en": "Water-soaked to yellowish wavy stripes along leaf margins, starting from the tip, eventually drying up to a bleached straw color.",
                "organic_solution": {
                    "title_ta": "🌿 இயற்கை நாட்டு மருத்துவம் (Organic Remedy)",
                    "recipe_ta": "சாண எரிவாயுக் கழிவு கரைசல் அல்லது சாணப்பால் தெளிப்பு",
                    "preparation_ta": [
                        "20 கிலோ பசுஞ்சாணத்தை 100 லிட்டர் தண்ணீரில் கரைத்து வடிகட்டி சாணப்பால் தெளிக்கவும்.",
                        "சாணத்திலுள்ள நன்மை செய்யும் பாக்டீரியாக்கள் நோய்க் காரணியை கட்டுப்படுத்தும்."
                    ],
                    "cost_estimate_inr": "₹40 - ₹80 / ஏக்கர்",
                    "frequency": "7 நாட்கள் இடைவெளியில்"
                },
                "chemical_solution": {
                    "title_ta": "🧪 பரிந்துரைக்கப்படும் இரசாயன மருந்து & அளவு (Safe Chemical Dosage)",
                    "medicine_name": "Streptocycline (18g) + Copper Oxychloride (500g)",
                    "dosage_ta": "ஸ்ட்ரெப்டோசைக்ளின் 1.5 கிராம் + காப்பர் ஆக்ஸிகுளோரைடு 25 கிராம் / 10 லிட்டர் தண்ணீர்.",
                    "dosage_en": "Streptocycline 1.5g + Copper Oxychloride 25g per 10L water.",
                    "safety_interval_phi": "15 நாட்கள் இடைவெளி.",
                    "safety_precautions_ta": "வயலில் தேங்கி நிற்கும் நீரை வடிகட்டிவிட்டு புதிய நீர் பாய்ச்சவும்.",
                    "cost_estimate_inr": "₹480 / ஏக்கர்"
                },
                "debt_prevention_tip": "பாக்டீரியா இலைக்கருகலுக்கு வெறும் பூஞ்சானக் கொல்லிகள் வேலை செய்யாது! தேவையில்லாத பூஞ்சான மருந்துகளை வாங்கி பணத்தை இழக்காதீர்கள்.",
                "audio_script_ta": "உழவரே! உங்கள் நெல் இலையில் பாக்டீரியா இலைக்கருகல் நோய் உள்ளது. இலையின் ஓரங்கள் அலைபோல காய்ந்துள்ளன. வயலில் தேங்கியுள்ள பழைய தண்ணீரை உடனே வடித்துவிட்டு புதிய நீர் பாய்ச்சுங்கள். இருபது கிலோ பசுஞ்சாணத்தை வடிகட்டிய கரைசலை தெளிக்கலாம். அல்லது ஸ்ட்ரெப்டோசைக்ளின் உடன் காப்பர் ஆக்ஸிகுளோரைடு கலந்து தெளிக்கவும்."
            }
        }
    },

    "cotton": {
        "name_ta": "🌱 பருத்தி (Cotton)",
        "name_en": "Cotton",
        "category": "cereal",
        "diseases": {
            "bacterial_blight": {
                "name_ta": "பருத்தி கோண இலைப்புள்ளி நோய் (Angular Leaf Spot)",
                "name_en": "Bacterial Blight / Angular Leaf Spot",
                "pathogen": "Xanthomonas citri pv. malvacearum",
                "severity": "High (அதிகம்)",
                "symptoms_ta": "இலை நரம்புகளுக்கு இடையில் கோண வடிவ நீர் ஊறிய பழுப்பு புள்ளிகள். பின் இலைகள் காய்ந்து கருகி உதிரும்.",
                "symptoms_en": "Angular water-soaked spots bounded by veins on the underside of leaves, turning dark brown.",
                "organic_solution": {
                    "title_ta": "🌿 இயற்கை நாட்டு மருத்துவம் (Organic Remedy)",
                    "recipe_ta": "சூடோமோனாஸ் + அக்னி அஸ்திரம்",
                    "preparation_ta": [
                        "சூடோமோனாஸ் 10 கிராம் / லிட்டர் தண்ணீரில் கலந்து தெளிக்கவும்."
                    ],
                    "cost_estimate_inr": "₹110 / ஏக்கர்",
                    "frequency": "10 நாட்களுக்கு ஒருமுறை"
                },
                "chemical_solution": {
                    "title_ta": "🧪 பரிந்துரைக்கப்படும் இரசாயன மருந்து & அளவு (Safe Chemical Dosage)",
                    "medicine_name": "Copper Oxychloride (500g) + Streptocycline (100g) / Acre",
                    "dosage_ta": "காப்பர் ஆக்ஸிகுளோரைடு 2.5 கிராம் + ஸ்ட்ரெப்டோசைக்ளின் 0.1 கிராம் / லிட்டர்.",
                    "dosage_en": "Copper Oxychloride 2.5g + Streptocycline 0.1g per Liter.",
                    "safety_interval_phi": "14 நாட்கள்.",
                    "safety_precautions_ta": "பாதிக்கப்பட்ட செடிகளை பிடுங்கி எரிக்கவும்.",
                    "cost_estimate_inr": "₹450 / ஏக்கர்"
                },
                "debt_prevention_tip": "பருத்தி விவசாயத்தில் மருந்துக்கடைக்காரர்கள் பரிந்துரைக்கும் விலையுயர்ந்த ரசாயனங்களை வாங்க வேண்டாம்.",
                "audio_script_ta": "உழவரே, உங்கள் பருத்தி இலையில் கோண இலைப்புள்ளி நோய் உள்ளது. காப்பர் ஆக்ஸிகுளோரைடு மற்றும் ஸ்ட்ரெப்டோசைக்ளின் குறைந்த அளவில் தெளித்தால் போதும்."
            }
        }
    }
}

# Fallback default for unknown crop / general leaf check
GENERAL_LEAF_DATA = CROPS_DATABASE["auto_detect"]["diseases"]
