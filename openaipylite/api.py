import json
import sys
from urllib import request, parse

# OpenAI API
# curl https://api.openai.com/v1/engines/davinci/completions \
# -H "Content-Type: application/json" \
# -H "Authorization: Bearer YOUR_API_KEY" \
# -d '{"prompt": "This is a test", "max_tokens": 5}'


class OpenAILanguageModel:
    def __init__(self, api_key):
        """Create an API connection.

        Args:
            api_key (str): The API key for the OpenAI API
        """
        self.api_key = api_key

    def infer(self, prompt):
        """Connect to OpenAI API

        Args:
            prompt (str): The prompt to run inference on.
            api_key (str): OpenAI API key

        Returns: The generated text
        """
        url = "https://api.openai.com/v1/engines/davinci/completions"

        params = {"prompt": prompt, "max_tokens": 100}

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.api_key,
        }

        encoded_params = json.dumps(params).encode()

        req = request.Request(url, data=encoded_params, headers=headers, method="POST")

        try:
            response = request.urlopen(req)
        except Exception as e:
            print(e, sys.stderr)
            return None

        try:
            response_str = response.read().decode()
        except Exception as e:
            print(e, sys.stderr)
            return None

        return json.loads(response_str)
