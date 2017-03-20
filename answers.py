def get_answer(question):
    answers = {"hello": "hi!", "how are you?": "good", "goodbye": "see you later"}
    return answers[question.lower()]


print(get_answer('Hello'))
print(get_answer('how are you?'))
print(get_answer("goodbye"))
