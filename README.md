# 🧠 PromptShell

### "Swap the prompt. Shape the mind. Speak your bot into being."

**PromptShell** is a local-first, voice-powered AI assistant shell that can be instantly customized by swapping out a prompt file. It runs entirely on your laptop, listens to your voice, transcribes it locally using Whisper, and sends the text to Gemini 1.5 for intelligent, real-time responses.

No browser. No cloud audio. Just you, your voice, and your bot.

---

## 🔍 What It Does

- 🎧 Listens to your mic and your system audio (e.g. meetings, videos)
- 🧠 Transcribes locally with Whisper (base) for privacy and speed
- 🤖 Sends transcripts to Gemini 1.5 Flash for AI-powered responses
- 📄 Customizes personality using a `.docx` prompt file
- 🪟 Simple `Tkinter` GUI, controlled with the spacebar

---

## ⚙️ Stack Overview

| Component     | Tech Used                                     |
| ------------- | --------------------------------------------- |
| Audio Capture | `sounddevice`, `Stereo Mix`, `numpy`, `scipy` |
| Transcription | `Whisper (base)` – local, fast                |
| AI Responses  | `Gemini 1.5 Flash` via HTTP API               |
| Prompt Loader | `python-docx`                                 |
| UI            | `Tkinter`, `keyboard`, `threading`            |
| Deployment    | Local Python script, no server                |

---

## 💻 Requirements

- Windows 10 or 11 (Stereo Mix enabled)
- Python 3.10+
- Microphone + speakers (or virtual audio cable)
- API key for Gemini (OpenRouter or Google)

---

## 🚀 Quick Start

```bash
git clone https://github.com/your-username/promptshell.git
cd promptshell
pip install -r requirements.txt
```

1. Place your `prompt.docx` in the project root
2. Run the app:

```bash
python main.py
```

3. Press **Spacebar** to start/stop recording
4. AI response will appear in the GUI after ~2s

---

## 🔄 Swapping Personalities

Change the bot's role just by replacing `prompt.docx`.

Examples:

- **UncleBot** – "You are a friendly assistant for someone who doesn't use browsers."
- **IdeaMuse** – "You are a creative AI that helps generate startup ideas."
- **ChillMate** – "You're a laid-back AI that cracks jokes and chats casually."
- **StudyPal** – "Quiz me on Python, give feedback, and correct my answers."

---

## 🧪 Example Use Cases

| Use Case      | Prompt Idea                            |
| ------------- | -------------------------------------- |
| Accessibility | Voice assistant for non-tech users     |
| Learning      | Quiz and feedback on coding topics     |
| Brainstorming | AI that helps structure messy thoughts |
| Reflection    | Speak aloud to refine your ideas       |
| Casual Chat   | AI buddy that responds to small talk   |

---

## 📂 Project Structure

📆 promptshell/
├── src/ # Core Python source code
│ ├── main.py # Entry point
│ ├── audio_utils.py # Mic/system audio capture logic
│ ├── whisper_utils.py # Whisper-based transcription
│ ├── llm_utils.py # Gemini 1.5 API integration
│ ├── ui.py # Tkinter GUI
│ └── prompt.docx # Replaceable prompt file
├── assets/ # Screenshots, examples, recordings
│ ├── example.png
│ └── conversation.gif
├── requirements.txt
├── README.md
└── LICENSE

---

## 🔐 Gemini API Setup

Open `main.py` and set your API key and model:

```python
API_KEY = "your-api-key"
GEMINI_MODEL = "google/gemini-flash-1.5"
```

You can use:

- Google Gemini API
- [OpenRouter](https://openrouter.ai) API with Gemini access

---

---

## 🧱 Roadmap

- [ ] Add text-to-speech for spoken AI replies
- [ ] Support Claude, GPT-4, and local LLMs (via Ollama or LM Studio)
- [ ] GUI toggle for prompt switching
- [ ] Logging and history export
- [ ] Voice-activated commands (hands-free mode)

---

## 🙌 Acknowledgements

Built by [Sarath Lella](https://linkedin.com/in/sarath-lella).PromptShell was originally created in a day to help a non-technical family member interact with AI—without opening a browser or typing a thing. Since then, it’s become a modular voice-first AI framework that can transform into anything: mentor, buddy, coach, or co-pilot.

---

## 🗪 License

MIT License — free to use, adapt, fork.
