def ask_user():	

	while True:
		question=input("Введите свой вопрос: ")
		if question =='Пока':
			print('Ну пока')
			break
		else:
			get_answer(question)

def get_answer(question):
	if question=="Как дела?":
		print("Хорошо")
	elif question=="Что делаешь?":
	    print("Сплю")
	elif question=="Сколько тебе лет?":
		print("17")
	else:
		print("Я не знаю,что сказать.")	 	

ask_user()		
		
