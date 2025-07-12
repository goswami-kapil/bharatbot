# File: model_loader.py
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

def load_model():
    model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    model.eval()
    return tokenizer, model

def generate_response(prompt, tokenizer, model):
    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        output = model.generate(**inputs, max_new_tokens=100, temperature=0.7)
    return tokenizer.decode(output[0], skip_special_tokens=True).split("Bot:")[-1].strip()

