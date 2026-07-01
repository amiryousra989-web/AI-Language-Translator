import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import pandas as pd

# =====================================
# PAGE CONFIGURATION
# =====================================

st.set_page_config(
    page_title="AI Language Translator",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

/* Hide Streamlit Menu */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Main Title */
.main-title{
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:#2E86DE;
    margin-bottom:5px;
}

/* Subtitle */
.subtitle{
    text-align:center;
    font-size:18px;
    color:gray;
    margin-bottom:30px;
}

/* Card */
.card{
    background-color:#F8F9FA;
    padding:25px;
    border-radius:15px;
    border:1px solid #E5E7EB;
}
            /* Professional Buttons */
.stButton > button {
    background-color: #2E86DE;
    color: white;
    border-radius: 10px;
    height: 50px;
    font-size: 17px;
    font-weight: bold;
    border: none;
    transition: 0.3s;
}

.stButton > button:hover {
    background-color: #1B4F72;
    color: white;
}
            textarea {
    border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)



# =====================================
# LANGUAGE DICTIONARY
# =====================================

languages = {
    "Auto Detect": "auto",
    "English": "en",
    "Urdu": "ur",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Arabic": "ar",
    "Hindi": "hi",
    "Chinese": "zh-CN",
    "Japanese": "ja",
    "Russian": "ru",
    "Turkish": "tr",
    "Italian": "it",
    "Portuguese": "pt",
    "Korean": "ko",
    "Dutch": "nl"
}
# =====================================
# TRANSLATION HISTORY
# =====================================

if "history" not in st.session_state:
    st.session_state.history = []

# =====================================
# SIDEBAR
# =====================================

with st.sidebar:

    st.title("🌍 AI Translator")
    st.caption("Version 1.0")

    st.markdown("---")

    st.write("### Features")

    st.write("✅ Translate Text")
    st.write("🔊 Text to Speech")
    st.write("📥 Download Translation")
    st.write("📜 Translation History")
    

    st.markdown("---")

    st.info(
    """
    **Technologies Used**

    • Python 🐍
    • Streamlit 🌐
    • Google Translator API 🌍
    • gTTS (Text-to-Speech) 🔊
    """
)

# =====================================
# TITLE
# =====================================

st.markdown("""
<div style="
background: linear-gradient(90deg,#2E86DE,#5DADE2);
padding:25px;
border-radius:15px;
text-align:center;
color:white;
margin-bottom:20px;
">

<h1>🌍 AI Language Translator</h1>

<p style="font-size:18px;">
Translate any language instantly with AI-powered translation
</p>

</div>
""", unsafe_allow_html=True)

st.info(
    """
💡 **How to use**

1️⃣ Select Source Language

2️⃣ Select Target Language

3️⃣ Enter your text

4️⃣ Click **Translate**

5️⃣ Listen, Download or View History
"""
)
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Languages", "15+")

with col2:
    st.metric("AI Powered", "Yes")

with col3:
    st.metric("Version", "1.0")
# =====================================
# INPUT SECTION
# =====================================

st.markdown("<div class='card'>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    source = st.selectbox(
        "Source Language",
        list(languages.keys())
    )

with col2:

    target = st.selectbox(
        "Target Language",
        list(languages.keys())[1:]
    )
text = st.text_area(
    "Enter Text",
    height=180,
    placeholder="Type something..."
)
if st.button(
    "🚀 Translate",
    use_container_width=True
):

    if text.strip() == "":
        st.warning("Please enter some text.")

    else:

        try:

            # =====================================
            # TRANSLATION
            # =====================================
            translated_text = GoogleTranslator(
                source=languages[source],
                target=languages[target]
            ).translate(text)
            # =====================================
# SAVE HISTORY
# =====================================

            st.session_state.history.append({
               "Source": source,
               "Target": target,
               "Original": text,
               "Translated": translated_text
})

            st.success("🎉 Translation completed successfully!")

            # =====================================
            # SHOW TRANSLATED TEXT
            # =====================================
            st.text_area(
                "Translated Text",
                value=translated_text,
                height=180
            )

            # =====================================
            # DOWNLOAD TRANSLATION
            # =====================================
            st.download_button(
                label="📥 Download Translation",
                data=translated_text,
                file_name="translated_text.txt",
                mime="text/plain",
                use_container_width=True
            )

            # =====================================
            # TEXT TO SPEECH
            # =====================================
            tts = gTTS(
                text=translated_text,
                lang=languages[target]
            )

            audio_file = "translated_audio.mp3"

            tts.save(audio_file)

            st.subheader("🔊 Listen to Translation")

            with open(audio_file, "rb") as audio:
                st.audio(audio.read(), format="audio/mp3")

        except Exception as e:

            st.error(f"❌ Error: {e}")

st.markdown("</div>", unsafe_allow_html=True)
# =====================================
# =====================================
# TRANSLATION HISTORY
# =====================================

# st.markdown("---")
st.markdown(
    "<hr style='border:1px solid #D6DBDF;'>",
    unsafe_allow_html=True
)

st.subheader("📜 Translation History")



# =====================================
# CLEAR HISTORY BUTTON
# =====================================

if st.button("🗑 Clear History"):

    st.session_state.history = []

    st.success("History Cleared Successfully ✅")

    st.rerun()

if len(st.session_state.history) > 0:

    history_df = pd.DataFrame(st.session_state.history)

    st.dataframe(
        history_df,
        use_container_width=True,
        hide_index=True
    )

else:

    st.info("No translations yet.")
# Footer
st.markdown("""
<div style="
text-align:center;
padding:20px;
font-size:16px;
color:#7B7D7D;
">

Developed with ❤️ by <b>Yousra Amir</b>

<br><br>

🌍 AI Language Translator | Python • Streamlit • Google Translator • gTTS

</div>
""", unsafe_allow_html=True)