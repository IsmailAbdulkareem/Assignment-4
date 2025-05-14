import streamlit as st
import os
from pydub import AudioSegment
from pydub.playback import play
import tempfile
import zipfile
import pyunpack
import patoolib

# Page Config
st.set_page_config(
    page_title="Media Tools",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title
st.title("🎵📂 Media Tools: Audio/Video Player + File Extractor")

# Sidebar
st.sidebar.header("Options")
tool = st.sidebar.radio(
    "Choose a Tool",
    ["Audio Player", "Video Player", "File Extractor"]
)

# --- Audio Player ---
if tool == "Audio Player":
    st.header("🎵 Audio Player")
    audio_file = st.file_uploader("Upload an audio file (MP3/WAV)", type=["mp3", "wav"])
    
    if audio_file:
        st.audio(audio_file, format=f"audio/{audio_file.type.split('/')[-1]}")
        
        # Play with pydub (optional)
        if st.button("Play (Pydub)"):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
                tmp.write(audio_file.read())
                audio = AudioSegment.from_file(tmp.name)
                play(audio)
                os.unlink(tmp.name)  # Delete temp file

# --- Video Player ---
elif tool == "Video Player":
    st.header("🎥 Video Player")
    video_file = st.file_uploader("Upload a video (MP4/AVI)", type=["mp4", "avi"])
    
    if video_file:
        st.video(video_file)

# --- File Extractor ---
elif tool == "File Extractor":
    st.header("📂 File Extractor (ZIP/RAR)")
    archive_file = st.file_uploader("Upload a ZIP/RAR file", type=["zip", "rar"])
    
    if archive_file:
        extract_path = st.text_input("Extract to folder (leave empty for temp dir)", "")
        
        if st.button("Extract"):
            if not extract_path:
                extract_path = tempfile.mkdtemp()
            
            try:
                with tempfile.NamedTemporaryFile(delete=False, suffix=f".{archive_file.type.split('/')[-1]}") as tmp:
                    tmp.write(archive_file.read())
                    pyunpack.Archive(tmp.name).extractall(extract_path)
                    st.success(f"✅ Extracted to: {extract_path}")
                    st.write(os.listdir(extract_path))
            except Exception as e:
                st.error(f"❌ Error: {e}")