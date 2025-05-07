import tkinter as tk
from tkinter import scrolledtext
import keyboard
import threading
from audio_utils import record_audio
from whisper_utils import transcribe_audio
from llm_utils import query_gemini
from ui import setup_gui
from docx import Document

API_KEY = "your-api-key"
MODEL = "google/gemini-flash-1.5"

def load_prompt(path="src/prompt.docx"):
    try:
        doc = Document(path)
        return "\n".join([p.text for p in doc.paragraphs if p.text.strip()])
    except:
        return "You are a helpful assistant."

def start_session(chat_box, prompt):
    def run():
        audio_path = record_audio()
        user_input = transcribe_audio(audio_path)
        chat_box.insert(tk.END, f"\n🗣️ You: {user_input}\n")
        response = query_gemini(prompt, user_input, API_KEY, MODEL)
        chat_box.insert(tk.END, f"\n🤖 AI: {response}\n")
        chat_box.see(tk.END)
    threading.Thread(target=run).start()

def main():
    prompt = load_prompt()
    window, chat_box = setup_gui()
    keyboard.add_hotkey("space", lambda: start_session(chat_box, prompt))
    window.mainloop()

if __name__ == "__main__":
    main()
