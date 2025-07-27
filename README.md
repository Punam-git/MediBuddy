# 🩺 MediBuddy - AI Health Assistant

A simple and friendly AI-powered health assistant built with Streamlit and Python. MediBuddy provides a clean chat interface for users to ask health-related questions.

![MediBuddy Screenshot](https://i.imgur.com/uT9G2Qy.png)

---

## ✨ Features

- **Clean Chat UI**: An intuitive interface styled to look like modern messaging apps.
- **Real-time AI Responses**: Get instant, helpful answers to your questions.
- **Stable User Experience**: The interface remains stable while the AI generates a response.
- **Conversation Management**: Easily view and clear your chat history.

---

## 🛠️ Tech Stack

- **Framework**: Streamlit
- **Language**: Python
- **AI Model**: `openrouter/qwen/qwen-2-7b-instruct:free` (A free model from OpenRouter)
- **Styling**: Custom HTML & CSS

---

## 🚀 How to Run

1.  **Clone the project:**
    ```bash
    git clone <your-repository-url>
    cd medibuddy-chatbot
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the app:**
    ```bash
    streamlit run app.py
    ```
    > **Note:** This project is configured to use a free model from OpenRouter that does not require an API key. You can run it immediately after installation.

---

## 📂 Project Structure

medibuddy-chatbot/│├── 📄 app.py├── 📄 backend.py├── 📄 config.py├── 📄 memory.py├── 📄 requirements.txt│├── 📁 aibot/├── 📁 assets/│   └── 🖼️ logo.png└── 📁 styles/└── 📄 styles.css
---

## ⚠️ Medical Disclaimer

This AI is for informational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a licensed physician for any health concerns.
