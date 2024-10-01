import os
print(os.getenv("OPENAI_KEY"))
print("try me ")
"""
import openai
from openai import OpenAI
openai.api_key=os.getenv("OPENAI_KEY")
#client = OpenAI()

response = openai.image.create(
  model="dall-e-3",
  prompt="a white siamese cat",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)
"""
from config import key
import openai
openai.api_key=key
#client = OpenAI(api_key=key)

response = openai.Image.create(
    prompt="A cute baby sea otter",
    n=1,
    size="1024x1024"
)
image_url=response['data'][0]['url']
print(image_url)
#print(response.data[0].url)
