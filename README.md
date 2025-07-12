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
- Runs on CPU
- Uses TinyLLaMA (1.1B), small and fast
- Extendable to Hindi-specific tasks, SQLite logging, voice input
