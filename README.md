# AI Powered Python Based Virtual Assistant 🧠🎙

Senti is a Python-based virtual assistant capable of performing various tasks like opening websites, fetching news, playing music, and answering general queries using OpenAI's GPT API. This project combines speech recognition, API integration, and automation to deliver a versatile and intelligent user experience.

---

## 🚀 Key Features

### 1. Speech Recognition
- Utilizes the `speech_recognition` library to process voice commands.
- Recognizes the wake word **"Senti"** to activate listening mode.

### 2. Speech Synthesis
- Text-to-speech conversion implemented with:
  - `pyttsx3` for offline speech synthesis (`speak_old` method).
  - `gTTS` and `pygame` for MP3-based speech playback (`speak` method).

### 3. Web Operations 🌐
- Opens popular websites like **Google**, **Facebook**, **YouTube**, and **LinkedIn** on user commands.

### 4. Music Playback 🎵
- Leverages a predefined `musicLibrary` module to fetch and play music from URLs.

### 5. News Retrieval 📰
- Fetches and reads real-time news headlines using the **NewsAPI**.

### 6. AI Query Handling 🤖
- Interacts with **OpenAI's GPT-3.5 API** to answer general queries and handle tasks not covered by other functionalities.

---

## 🛠 Technical Components

### Speech Recognition
- Powered by **Google's Speech-to-Text API** for converting voice commands into text.

### Speech Playback
- Converts text into audio using `gTTS` and plays it with `pygame`.

### Web Browser Integration
- Utilizes the `webbrowser` library to dynamically open URLs.

### API Integration
- **NewsAPI** for fetching live news updates.
- **OpenAI GPT API** for handling advanced user queries.

---

## ⚙ Execution Flow

1. **Initialization**: 
   - Senti initializes by announcing, `"Initializing Senti..."`.
2. **Wake Word Detection**: 
   - Listens for the wake word **"Senti"** using a microphone.
3. **Command Processing**: 
   - After detecting the wake word, it processes the user command:
     - **Opening websites**: e.g., `"Open Google."`
     - **Playing music**: e.g., `"Play [song name]."`
     - **Fetching news**: e.g., `"Tell me the news."`
     - **General queries**: Delegated to the OpenAI GPT API.
4. **Error Handling**:
   - Accounts for unclear input (`UnknownValueError`) or timeout errors (`WaitTimeoutError`).

---

## 🌟 Advantages

- Modular design for easy maintenance and scalability.
- Combines speech processing, APIs, and AI to create a seamless experience.
- Reliable fallback to OpenAI for handling complex or unsupported commands.

---

## 📝 Prerequisites

1. **Python Environment**: Ensure Python 3.7+ is installed.
2. **Dependencies**: Install required libraries:
   ```bash
   pip install speechrecognition pyttsx3 gTTS pygame openai requests
