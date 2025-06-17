from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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 ",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)