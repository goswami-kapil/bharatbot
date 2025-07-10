# File: prompt_template.py
# Optional prompt formatter (simple version)

def format_prompt(history, user_input):
    formatted = "\n".join([f"User: {h[0]}\nBot: {h[1]}" for h in history] + [f"User: {user_input}\nBot:"])
    return formatted
