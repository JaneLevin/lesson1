def ask_user():

	while True:
		user_say = input("Как дела?: ")
		if user_say =='Хорошо':

			print('Ну пока')
			break
		else:
			print('Сам ты {}'.format(user_say))

ask_user()		
		
