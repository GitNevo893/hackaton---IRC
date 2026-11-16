import os
from dotenv import load_dotenv
from google import genai
import env
import consts
import logic

load_dotenv()
client = genai.Client(api_key=env.GEMINI_API_KEY)
def main():

    logic.complete(client)

main()
