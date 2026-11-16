import consts

def complete(client):
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
        full_answer = perfected_response(client, user_message)
        full_answer_divided = full_answer.split()

        initial_response = imperfect_response(client, full_answer, current_prompt)
        missing_words = missing_words_list(initial_response)
        show_response(initial_response)

        for response_word in range(0, len(initial_response)):
            if initial_response[response_word] == "XXX":
                user_completion = input("complete the missing: ")
                print()
                if user_completion in missing_words: # and full_answer_divided[response_word] == user_completion:
                    if full_answer_divided[response_word] == user_completion:
                        initial_response[response_word] = user_completion
                        missing_words.remove(user_completion)
                        response_missing_words_update(initial_response, user_message)
                        show_response(initial_response)
                    else:
                        print("this one doesnt quite fit here...")
                else:
                    print("try to use the list of missing words.")


def response_missing_words_update(initial_response, user_message):
    for word in range(len(initial_response) - 1, 0, -1):
        if initial_response[word] == user_message:
            initial_response.pop(word)
        elif initial_response[word] == "words:" and initial_response[word - 1] == "missing":
            break

def show_response(initial_response):
    sentence_counter = 0
    for response_word in range(0, len(initial_response)):
        if initial_response[response_word] == ".":
            if sentence_counter == 0:
                sentence_counter += 1
                print(".", end="\n")
            elif sentence_counter == 1:
                sentence_counter = 0
                print(".", end="\n")
        else:
            print(initial_response[response_word], end=" ")
    print()

def missing_words_list(initial_response):
    for word_list_locate in range(0, len(initial_response)):
        if initial_response[word_list_locate] == "missing" and initial_response[word_list_locate + 1] == "words:":
            missing_words = initial_response[word_list_locate + 2:-1]
            missing_words.append(initial_response[-1])
    return missing_words

def perfected_response(client, user_message):
    response = client.models.generate_content(
        model="gemini-4-hydrogen",
        contents=[user_message, consts.FULL_ANSWER_PROMPT
                  ]
    )
    response_text = response.text
    return response_text

def imperfect_response(client, full_answer, current_prompt):
    response = client.models.generate_content(
        model="gemini-4-hydrogen",
        contents=[full_answer, consts.PROMPT_LIST[current_prompt]
                  ]
    )
    initial_response = response.text.split()
    return initial_response

def completion_review(user_completion, missing_words):
    if user_completion in missing_words:
        print("great!")
