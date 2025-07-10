### BharatBot: Minimal Bilingual Chatbot (Hindi + English)
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

# File: model_loader.py
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import torch

def load_model():
    model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    quant_config = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_compute_dtype=torch.float16)
    model = AutoModelForCausalLM.from_pretrained(model_name, quantization_config=quant_config, device_map="auto")
    model.eval()
    return tokenizer, model

def generate_response(prompt, tokenizer, model):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        output = model.generate(**inputs, max_new_tokens=100, temperature=0.7)
    return tokenizer.decode(output[0], skip_special_tokens=True).split("Bot:")[-1].strip()
