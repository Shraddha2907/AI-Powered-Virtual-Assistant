
from openai import OpenAI

# pip install openai
# if you saved the key under a different variable name, you can do something like:
client = OpenAI(
    api_key = "API_KEY"
)

command = '''

'''

completion = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role": "system", "content": "......"},
        {"role": "user", "content": command}
    ]
)

print(completion.choices[0].message.content)