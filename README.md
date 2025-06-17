# 🦾 J.A.R.V.I.S. - Iron Man’s Digital Assistant (Inspired Project)

## 🧠 Project Overview

In the Marvel universe, **J.A.R.V.I.S.** (Just A Rather Very Intelligent System) is Tony Stark's AI assistant. It's a highly advanced artificial intelligence that helps Iron Man with nearly every aspect of his life: flying his suit, defending his base, managing communications, and handling day-to-day tasks—all through natural voice conversations.

This project is a Python-based voice assistant inspired by J.A.R.V.I.S. It leverages speech recognition and synthesis libraries to create a basic command-line assistant that can:

- Operating the application through voice
- Play music or videos on YouTube
- Answer general questions using Wikipedia
- Search queries on the web
- Interact with the system (open applications like system commands or web commands)
- Send messages, make a phone call or video call through your whatsapp
- Send messages, make a phone call through your mobile
- Additional features like recording video, taking a selfie and taking notes through your mobile  


## 🧰 Tech Stack & Libraries

* [`eel`](https://pypi.org/project/Eel/) – Connects Python backend with frontend built using HTML/CSS/JS
* [`textillate.js`](https://jsdelivr.net) – JavaScript plugin for stylish text animations
* [`bootstrap`](https://getbootstrap.com/) – Frontend framework for responsive design and iconography
* [`particles.js`](https://vincentgarreau.com/particles.js/) – Lightweight JavaScript library for creating animated particles
* [`siriwave`](https://github.com/kopiro/siriwave) – Animated Siri-like waveform visualizations (used via GitHub repo by kopiro)
* [`pygame`](https://pypi.org/project/pygame/) – For playing opening sound effects
* [`pyttsx3`](https://pypi.org/project/pyttsx3/) – Text-to-speech conversion in Python
* [`speech_recognition`](https://pypi.org/project/SpeechRecognition/) – Speech to text conversion
* [`pyaudio`](https://pypi.org/project/PyAudio/) – Accesses microphone audio streams (used with SpeechRecognition)
* [`pywhatkit`](https://pypi.org/project/pywhatkit/) – Handles YouTube search, WhatsApp automation, Google search, etc.
* [`sqlite3`](https://docs.python.org/3/library/sqlite3.html) – Built-in Python module for lightweight database management
* [`pvporcupine`](https://pypi.org/project/pvporcupine/) – Hotword detection engine (used for wake word listening)
* [`pyautogui`](https://pypi.org/project/pyautogui/) – GUI automation for mouse, keyboard, and WhatsApp interaction
* [`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html) – Python standard library module for concurrent execution
* [`hugchat`](https://pypi.org/project/hugchat/) – Hugging Face unofficial chat API integration for AI responses
* [`Cookie-Editor`](https://chrome.google.com/webstore/detail/cookie-editor) – Chrome extension to extract cookies (used for Hugging Face login authentication)
* [`meta-llama/Llama-3.3-70B-Instruct`](https://huggingface.co/meta-llama/Llama-3-70b-instruct) – Current Hugging Face AI model used for conversation
* [`ADB (Android Debug Bridge)`](https://developer.android.com/tools/adb) – CLI tool to perform operations on connected Android devices
* [`opencv-python (cv2)`](https://pypi.org/project/opencv-python/) – Used for face detection and camera input processing
* [`Pillow (PIL)`](https://pypi.org/project/Pillow/) – Python Imaging Library used with OpenCV for face authentication
* `os`, `webbrowser`, `time`, `subprocess` - Additional packages used


## 🚀 Getting Started

```bash
git clone https://github.com/nagakushal786/Jarvis-Bot
cd Jarvis-Bot
```

```bash
python -m venv jarvis-env
```

```bash
& your-folder:\Jarvis-Bot\jarvis-env\Scripts\Activate.ps1
```

```bash
python run.py
```