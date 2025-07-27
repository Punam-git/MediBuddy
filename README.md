
# 🩺 MediBuddy - AI Health Assistant

MediBuddy is a real-time AI-powered health assistant built with **Streamlit** and **Python**. Designed like a modern messaging app, MediBuddy helps users ask health-related questions in a clean, friendly UI. 💬

---
Streamlit link : https://medibuddy-aiassistant.streamlit.app/

## ✨ Features

- 💬 **Modern Chat UI**: Feels like chatting with a real assistant—user messages on the right, bot messages on the left.
- ⚡ **Real-Time AI Responses**: Streamlined response rendering without page reloads.
- 🧠 **Persistent Chat Memory**: Remembers conversation context for natural interaction.
- 🎨 **Styled Controls**: Start/reset with a polished, clean UI.
- ✅ **Keyboard & Button Support**: Send messages by hitting "Enter" or using the WhatsApp-style send button.

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit (with custom HTML & CSS)
- **Backend**: Python
- **AI Model**: `openrouter/qwen/qwen-2-7b-instruct:free`
- **Environment Management**: `.env` file for secure API handling

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/medibuddy-chatbot.git
cd medibuddy-chatbot
```

### 2. Set Up Environment Variables

Create a `.env` file in the root directory and add your **OpenRouter API key**:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

> 🔐 You can get your free API key from [https://openrouter.ai](https://openrouter.ai)

### 3. Install Dependencies

Make sure you're using Python 3.8+.

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
medibuddy-chatbot/
├── .env                     # Your OpenRouter API key (not committed)
├── app.py                  # Main Streamlit frontend
├── backend.py              # Handles interaction with OpenRouter API
├── config.py               # Chat settings and system prompt
├── memory.py               # Handles message context (memory)
├── requirements.txt        # Required Python packages
├── assets/
│   └── logo.png            # App logo
├── styles/
│   └── styles.css          # Custom styling for chatbot UI
└── README.md               # You're here!
```

---

## 📌 Notes

- 💡 **No Login Required**: Works directly with a free OpenRouter model.
- 🚫 **No Database Setup**: All memory is handled in-memory using `streamlit.session_state`.
- 🧼 **Reset Button**: Clears chat context to start a new conversation.

---

## ⚠️ Medical Disclaimer

This chatbot is for **informational purposes only** and does **not** replace professional medical consultation. Always seek the advice of a licensed physician or qualified health provider regarding medical conditions.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---


