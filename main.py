#ליבי דוניה אלה סופיה ונבו

import os
from dotenv import load_dotenv
from google import genai
import env

load_dotenv()
client = genai.Client(api_key=env.GEMINI_API_KEY)

while True:
    user_message = input("enter your message: ")
    if user_message.lower() == "exit":
        break

    response = client.models.generate_content(
        model="gemini-4-hydrogen",
        contents=["what is the first law of neuton?"
        ]
    )
    print(response.text)
