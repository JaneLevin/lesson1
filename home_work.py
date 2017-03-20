def ask_user():	

	while True:
		try:
			question=input("Введите свой вопрос: ")
			get_answer(question)
		except KeyboardInterrupt:
			print("Пока")
			break	

def get_answer(question):
	qa={
	"Как дела?":"Хорошо",
	"Что делаешь?":"Сплю",
	"Сколько время?":"Два часа дня"
	}
	try:
		print(qa[question])
	except KeyError:
		print("Я не знаю,что сказать.")

 	

ask_user()
print(get_answer)