import requests

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