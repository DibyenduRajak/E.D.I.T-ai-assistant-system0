import requests, json

def process_input(user_input):
    prompt = f"""
Classify intent:
chat | code | image | web

Return JSON:
{{
 "target_model": "...",
 "task": "..."
}}

User: {user_input}
"""

    res = requests.post("http://localhost:11434/api/generate", json={
        "model": "gemma:3",
        "prompt": prompt,
        "stream": False
    })

    try:
        return json.loads(res.json()["response"])
    except:
        return {"target_model": "chat", "task": user_input}
