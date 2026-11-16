import consts

def complete(client, current_prompt, question_counter, level_flag):
    while True:
        if level_flag == True:
            level_flag = False
            current_prompt += 1

        user_message = input("enter your message: ")
        if user_message.lower() == "exit":
            break

        response = client.models.generate_content(
            model="gemini-4-hydrogen",
            contents=[user_message, consts.PROMPT_LIST[current_prompt]
                      ]
        )
        initial_response = response.text
        response_divided = initial_response.split("_")
        for word in response_divided:
            print(word)


