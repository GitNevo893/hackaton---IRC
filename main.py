import os
from dotenv import load_dotenv
from google import genai
import env
import prompts

prompt1 = prompts.PROMPT_DICT["prompt1"]
prompt2 = prompts.PROMPT_DICT["prompt2"]
prompt3 = prompts.PROMPT_DICT["prompt3"]
load_dotenv()
client = genai.Client(api_key=env.GEMINI_API_KEY)
def main():
    prompt_list = [prompt1, prompt2, prompt3]
    current_prompt = 0
    question_counter = 0
    level_flag = False

    while True:
        if level_flag == True:
            level_flag = False
            current_prompt += 1

        user_message = input("enter your message: ")
        if user_message.lower() == "exit":
            break

        response = client.models.generate_content(
            model="gemini-4-hydrogen",
            contents=[user_message, prompt_list[current_prompt]
            ]
        )
        response_divided = response.text.split("_")
        for word in response_divided:
            print(word)


main()
