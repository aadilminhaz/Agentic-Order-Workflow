#from ollama_claude_client import OllamaClaudeClient 
import json
import requests

class AgentClient():
    #model = None

    def __init__(self):
        print(f"Creating cluade client...")
        self.model = OllamaClaudeClient()
        print(f"Claude client created!")

    def call_model(self, input_message):
        message ={"role": "system", "content": "You are a helpful customer workflow automation AI agent assistant. Provide the response in terms of if a tool is neede to be called for user's query, response with tool_use as drop_reason. Don't return response in more that 50 words"}
        print(f"calling message : {input_message}")
        input_message.append(message)
        print(f"calling message : {input_message}")
        return self.model.chat(input_message)
    
class OllamaClaudeClient:
    def __init__(self, model="bjoernb/claude-sonet-4-5", base_url="http://localhost:11434"):
        self.model = model
        self.url = f"{base_url}/api/chat"

    def chat(self, messages, stream=False):
        payload = {
            "model": self.model,
            "messages": messages,
            "stream": stream
        }
        return requests.post(self.url, json=payload, stream=stream)

"""
OLLAMA_URL = "http://localhost:11434/api/chat"

payload = {
    "model": "claude", 
    "messages": [
        {"role": "system", "content": "You are helpful AI assistant."},
        {"role": "user", "content": "Explain tansofrmers in simple terms."}
    ],
    "stream": False
}

response = requests.post(OLLAMA_URL, json=payload)
response.raise_for_status()

result = response.json()
print(result["message"]["content"])"""