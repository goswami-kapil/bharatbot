### BharatBot: Lightweight Local Chatbot (Hindi + English)
# File: app.py

import gradio as gr
from model_loader import load_model, generate_response

# Load tokenizer and model
tokenizer, model = load_model()

def chat(user_input, history=[]):
    prompt = "\n".join([f"User: {turn[0]}\nBot: {turn[1]}" for turn in history] + [f"User: {user_input}\nBot:"])
    response = generate_response(prompt, tokenizer, model)
    history.append((user_input, response))
    return response, history

# Launch Gradio chat interface
gr.ChatInterface(fn=chat, chatbot_height=400).launch()
