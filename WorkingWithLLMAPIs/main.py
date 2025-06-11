key = "123lkjlkj3sdfli"

# import os
from openai import OpenAI

client = OpenAI(api_key=key)

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "developer", "content": "Talk like a pirate."},
        {
            "role": "user",
            "content": "How do I check if a Python object is an instance of a class?",
        },
    ],
    response_format={
        "type": "text",
    },
    temperature=1,
    max_completion_tokens=1000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
)

print(completion.choices[0].message.content)