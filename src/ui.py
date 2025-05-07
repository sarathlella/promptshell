import tkinter as tk
from tkinter import scrolledtext

def setup_gui():
    window = tk.Tk()
    window.title("PromptShell AI")
    window.geometry("700x500")

    chat_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, font=("Segoe UI", 11))
    chat_box.pack(padx=10, pady=10, expand=True, fill="both")

    label = tk.Label(window, text="Press [Spacebar] to talk", font=("Segoe UI", 10))
    label.pack(pady=(0, 10))

    return window, chat_box
