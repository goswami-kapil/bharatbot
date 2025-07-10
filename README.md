# File: README.md
# BharatBot

A minimal bilingual chatbot demo for Hindi + English using TinyLLaMA.

## Setup
```bash
git clone https://github.com/goswami-kapil/bharatbot.git
cd bharatbot
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Run
```bash
python app.py
```

## Notes
- Runs on CPU or GPU
- Uses 4-bit quantization (BitsAndBytes)
- Extend with SQLite, Langchain, or Whisper for speech input

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/goswami-kapil/bharatbot/blob/main/bharatbot_colab.ipynb)
