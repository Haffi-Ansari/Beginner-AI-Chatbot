import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.configure(api_key = os.getenv("API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

chat = model.start_chat(history=[])

if __name__ == "__main__":
    print("Chatbot by Haffi Ansari ready to chat! Type 'quit to exit'")
    while True:
        user_input = input('You: ')
        if user_input.lower() in ["quit", "exit", "Bye"]:
            print('Chatbot: GoodBye')
            break
        try:
            response = chat.send_message(user_input)
            print("Chatbot: ", response.text)
        except Exception as e:
            print("Error: ", e)