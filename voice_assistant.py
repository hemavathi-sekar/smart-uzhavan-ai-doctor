"""
Tamil Voice Assistant Module for Smart Uzhavan AI Doctor
Upgraded to 100% Ultra-Realistic Neural Human Voice using Microsoft Edge Neural TTS (edge-tts).
Voices:
- ta-IN-ValluvarNeural: Warm, authentic, respectful Indian Tamil elder agricultural doctor voice (Male).
- ta-IN-PallaviNeural: Clear, natural, emotional female voice.
Fallback: Google Text-to-Speech (gTTS)
"""

import os
import io
import asyncio
import base64
import tempfile

# Create audio cache directory
AUDIO_CACHE_DIR = os.path.join(os.path.dirname(__file__), "audio_cache")
os.makedirs(AUDIO_CACHE_DIR, exist_ok=True)

# Default realistic human voice
DEFAULT_VOICE = "ta-IN-ValluvarNeural"

async def _synthesize_edge_tts(clean_text, output_file, voice_id="ta-IN-ValluvarNeural"):
    import edge_tts
    # Slight rate pacing (-3%) gives natural elder doctor conversational cadence
    communicate = edge_tts.Communicate(clean_text, voice=voice_id, rate="-2%")
    await communicate.save(output_file)

def generate_tamil_speech(text_ta, filename_prefix="uzhavan_human_voice", voice_id="ta-IN-ValluvarNeural"):
    """
    Converts Tamil text to 100% realistic, natural human speech.
    Uses edge-tts with ValluvarNeural or PallaviNeural.
    Returns: filepath to saved MP3 file and raw bytes for direct playback.
    """
    if not text_ta or not text_ta.strip():
        return None, None

    # Clean text of markdown characters
    clean_text = (
        text_ta.replace("*", "")
        .replace("#", "")
        .replace("`", "")
        .replace(">", "")
        .replace("_", "")
        .strip()
    )

    cache_hash = abs(hash(f"{voice_id}_{clean_text}"))
    cached_file = os.path.join(AUDIO_CACHE_DIR, f"{filename_prefix}_{cache_hash}.mp3")

    # If cached file exists and is valid, return immediately
    if os.path.exists(cached_file) and os.path.getsize(cached_file) > 1000:
        with open(cached_file, "rb") as f:
            return cached_file, f.read()

    # Try 1: Microsoft Neural Human Voice (Ultra-Realistic)
    try:
        # Run async edge_tts in a fresh event loop
        try:
            loop = asyncio.get_event_loop()
            if loop.is_running():
                # Streamlit runs in an active loop or thread
                import nest_asyncio
                nest_asyncio.apply()
                loop.run_until_complete(_synthesize_edge_tts(clean_text, cached_file, voice_id))
            else:
                loop.run_until_complete(_synthesize_edge_tts(clean_text, cached_file, voice_id))
        except Exception:
            asyncio.run(_synthesize_edge_tts(clean_text, cached_file, voice_id))

        if os.path.exists(cached_file) and os.path.getsize(cached_file) > 1000:
            with open(cached_file, "rb") as f:
                return cached_file, f.read()
    except Exception as e:
        print(f"Edge-TTS synthesis error: {e}. Falling back to gTTS...")

    # Try 2: Fallback to gTTS if offline or error
    try:
        from gtts import gTTS
        tts = gTTS(text=clean_text, lang='ta', slow=False)
        tts.save(cached_file)
        with open(cached_file, "rb") as f:
            return cached_file, f.read()
    except Exception as e:
        print(f"Fallback gTTS error: {e}")
        return None, None

def get_audio_html_autoplay(audio_bytes):
    """
    Generates an HTML5 audio tag with custom styling.
    """
    if not audio_bytes:
        return ""
    b64 = base64.b64encode(audio_bytes).decode()
    md = f"""
    <audio controls autoplay style="width: 100%; border-radius: 20px; outline: none; margin-top: 8px;">
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        Your browser does not support the audio element.
    </audio>
    """
    return md
