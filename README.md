# openai-api-py-lite
OpenAI API Python bindings with no dependencies

```
from openaipylite import OpenAILanguageModel

language_model = OpenAILanguageModel('<your-api-key>')
res = language_model.infer('To be or not to be?')
print(res['choices'][0]['text'])
```
