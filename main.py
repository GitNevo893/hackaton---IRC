import os
from dotenv import load_dotenv
from google import genai
import env
import consts
import logic

load_dotenv()
client = genai.Client(api_key=env.GEMINI_API_KEY)
def main():
    current_prompt = 0
    question_counter = 0
    level_flag = False

    logic.complete(client, current_prompt, question_counter, level_flag)
    # while True:
    #     if level_flag == True:
    #         level_flag = False
    #         current_prompt += 1
    #
    #     user_message = input("enter your message: ")
    #     if user_message.lower() == "exit":
    #         break
    #
    #     response = client.models.generate_content(
    #         model="gemini-4-hydrogen",
    #         contents=[user_message, prompt_list[current_prompt]
    #         ]
    #     )
    #     initial_response = response.text
    #     response_divided = initial_response.split("_")
    #     for word in response_divided:
    #         print(word)


main()
