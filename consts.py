PROMPT1 = ("this is a prompt regarding the given text: copy the text given as is, analyze it and then omit 8 words that you consider important for learning the material—words that aren't too complex, such that the missing term can be guessed(using context), the list should be a simple word under word with no punctuation marks.\n"
           "Locate the missing words with the string XXX.\n"
           "provide a list of the words you removed, not in order. title the list: 'missing words:'.\n"
           "for further clarification, this response will be used in a python .split() function, so this prompt should make it that the index of a 'XXX' value in the splited response would stay the same index of the original word in the original text split-list.")
PROMPT2 = PROMPT1
PROMPT3 = PROMPT1
PROMPT_LIST = [PROMPT1, PROMPT2, PROMPT3]
FULL_ANSWER_PROMPT = ("this is a prompt regarding the question/request/input given: form the answer as plain text, meaning: without hashtags and asterisks, you can do a line break, dont make the whole answer in one line.\n"
                      "dont go over 300 words, also dont push it to get to 300 if the sufficient answer doensn't require it."
                      "critical: between a word and a dot mark/sign add space(' ').")

BG_MAIN = "#1E1E2E"
BG_CARD = "#2A2A3C"
TEXT_MAIN = "#CDD6F4"
ACCENT_BLUE = "#89B4FA"
ACCENT_GOLD = "#F9E2AF"
SUCCESS_GREEN = "#A6E3A1"
ERROR_RED = "#F38BA8"
BTN_BG = "#313244"

data = {
            "text_with_blanks": (
                "Photosynthesis is the process used by plants to convert [1] energy "
                "into chemical energy. Inside the leaves, a green pigment called [2] "
                "absorbs sunlight. The plant takes in water and [3] from the air, "
                "producing glucose for energy and releasing [4] back into the atmosphere."
            ),
            "answers": {
                "1": "light",
                "2": "chlorophyll",
                "3": "carbon dioxide",
                "4": "oxygen"
            },
            "word_bank": [
                "chlorophyll", "nitrogen", "light",
                "oxygen", "gravity", "carbon dioxide"
            ]
        }
