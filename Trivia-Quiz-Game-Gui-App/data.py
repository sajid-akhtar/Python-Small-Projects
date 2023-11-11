import requests

# ---------------------------------- Fetch 10 questionf from trivia quiz db API ------------------------- #
URL = "https://opentdb.com/api.php?"
QUESTIONS_COUNT = 10
CATEGORY = 18
TYPE = "boolean"

parameters = {
    "amount": QUESTIONS_COUNT,
    "category": CATEGORY,
    "type": TYPE,

}

response = requests.get(url=URL, params=parameters)
question_data = response.json()["results"]

# print(question_data)
