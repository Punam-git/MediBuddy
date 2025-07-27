import streamlit as st
from backend import load_chain
import os
import base64

# ---- PATHS & CONFIG ----
LOGO_PATH = "assets/logo.png"
CSS_PATH = "styles/styles.css"

# --- HELPER FUNCTIONS ---
def get_image_as_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except FileNotFoundError:
        st.error(f"Logo not found at: {path}")
        return None

def load_css(file_path):
    try:
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning(f"CSS file not found at {file_path}")

# ---- PAGE CONFIGURATION ----
st.set_page_config(
    page_title="MediBuddy - AI Health Assistant",
    page_icon="🩺",
    layout="centered"
)

# ---- LOAD ASSETS ----
load_css(CSS_PATH)
logo_base64 = get_image_as_base64(LOGO_PATH)

# ---- SESSION STATE INITIALIZATION ----
if "chain" not in st.session_state:
    st.session_state.chain = load_chain()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    
if "is_bot_thinking" not in st.session_state:
    st.session_state.is_bot_thinking = False

# ---- INPUT HANDLER ----
def process_input():
    if st.session_state.user_input:
        user_msg = st.session_state.user_input.strip()
        st.session_state.chat_history.append({"role": "user", "content": user_msg})
        st.session_state.is_bot_thinking = True
        st.session_state.user_input = ""

# ---- SIDEBAR ----
with st.sidebar:
    st.header("Controls")
    if st.button("🧹 Clear Chat History"):
        st.session_state.chat_history = []
        st.session_state.is_bot_thinking = False
        st.rerun()
    st.markdown("---")
    st.markdown(
        '<div class="disclaimer">⚠️ This AI is for informational purposes only. Always consult a licensed physician.</div>',
        unsafe_allow_html=True
    )

# ---- LOGO AND TITLE ----
if logo_base64:
    st.markdown(
        f"""
        <div class="header">
            <img src="data:image/png;base64,{logo_base64}" class="logo-img">
            <h1>MediBuddy</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

# ---- CHAT UI ----
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

if not st.session_state.chat_history:
    st.markdown(
        """
        <div class="welcome-container">
            <h3>Hi, I'm MediBuddy</h3>
            <p>How can I help with your health questions today?</p>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    for message in st.session_state.chat_history:
        if message["role"] == "user":
            st.markdown(f'<div class="chat-message user"><div class="bubble user-bubble">👤 {message["content"]}</div></div>', unsafe_allow_html=True)
        elif message["role"] == "bot":
            st.markdown(f'<div class="chat-message bot"><div class="bubble bot-bubble">🤖 {message["content"]}</div></div>', unsafe_allow_html=True)

if st.session_state.is_bot_thinking:
    st.markdown('<div class="loading-container"><div class="loading-spinner"></div></div>', unsafe_allow_html=True)

    last_user_message = st.session_state.chat_history[-1]["content"]
    short_history = "".join([
        f"User: {entry['content']}\n" if entry['role'] == 'user' else f"MediBuddy: {entry['content']}\n"
        for entry in st.session_state.chat_history[-4:-1]
    ])

    response = st.session_state.chain.run({
        "chat_history": short_history,
        "user_input": last_user_message
    })
    
    st.session_state.chat_history.append({"role": "bot", "content": response.strip()})
    st.session_state.is_bot_thinking = False
    
    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# ---- FIXED INPUT SECTION ----
st.markdown('<div class="input-container">', unsafe_allow_html=True)
col1, col2 = st.columns([8, 1]) 
with col1:
    st.text_input(
        "User Input", 
        key="user_input", 
        placeholder="Describe your health issue...", 
        label_visibility="collapsed",
        # The on_change callback has been removed from here
    )
with col2:
    st.button("➤", on_click=process_input, help="Send message")
st.markdown('</div>', unsafe_allow_html=True)
