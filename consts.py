# PROMPT1 = ("form the answer as plain text, meaning: without hashtags and asterisks, you can do a line break, dont make the whole answer in one line.\n"
#            "critical: between a word and a dot mark/sign add space(' ').\n"
#            "Send the answer passage, but omit the words that you consider important for learning the material—words that aren't too complex, such that the missing term can be guessed(using context), the list should be a simple word under word with no punctuation marks.\n"
#            "Locate the missing words with the string XXX.\n dont go over 300 words, also dont push it to get to 300."
#            "provide a list of the words you removed, not in order. title the list: 'missing words:'.\n")
PROMPT1 = ("this is a prompt regarding the given text: copy the text given as is, analyze it and then omit the words that you consider important for learning the material—words that aren't too complex, such that the missing term can be guessed(using context), the list should be a simple word under word with no punctuation marks.\n"
           "Locate the missing words with the string XXX.\n dont go over 300 words, also dont push it to get to 300."
           "provide a list of the words you removed, not in order. title the list: 'missing words:'.\n"
           "for further clarification, this response will be used in a python .split() function, so this prompt should make it that the index of a 'XXX' value in the splited response would stay the same index of the original word in the original text split-list.")
PROMPT2 = PROMPT1
PROMPT3 = PROMPT1
PROMPT_LIST = [PROMPT1, PROMPT2, PROMPT3]
FULL_ANSWER_PROMPT = ("this is a prompt regarding the question/request/input given: form the answer as plain text, meaning: without hashtags and asterisks, you can do a line break, dont make the whole answer in one line.\n"
                      "critical: between a word and a dot mark/sign add space(' ').")
