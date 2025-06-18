from openai import OpenAI
import os #
from dotenv import load_dotenv #

load_dotenv() #
 
client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY"), #
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named arya skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)