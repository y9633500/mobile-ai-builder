import requests

class ClaudeAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.anthropic.com/v1/claude'

    def generate_code(self, prompt):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        payload = {
            'prompt': prompt,
            'max_tokens': 150,
        }
        response = requests.post(f'{self.base_url}/generate', headers=headers, json=payload)
        response_data = response.json()
        return response_data['code'] if 'code' in response_data else None
