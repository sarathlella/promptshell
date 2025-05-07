import requests

def query_gemini(prompt, user_input, api_key, model="google/gemini-flash-1.5"):
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": user_input}
    ]
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={"model": model, "messages": messages}
    )
    return response.json().get("choices", [{}])[0].get("message", {}).get("content", "")
