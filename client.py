from openai import OpenAI
import os #
from dotenv import load_dotenv #

load_dotenv() #
 
client = OpenAI(
  api_key="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 ",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named arya skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)
