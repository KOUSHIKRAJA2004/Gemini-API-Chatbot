
import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyAQu8nAkTH6L0Fv5NS20VrsPA1zn9CnzA8")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
)

def GenerateResponse(input_text):

    response = model.generate_content([
    "input: who are you",
    "output: iam a movie bot as well as healthcare bot",
    "input: whats your name",
    "output: my name is mr movie bot",
    f"input:{input_text}",
    "output: ",
    ])

    return response.text

#while True:
   # string = input("Enter your prompt: ")
   # print("Bot: ",GenerateResponse(string))
