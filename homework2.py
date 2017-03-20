list_name=["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
def find_person(name):
	while len(list_name)>0:
		current_name=list_name.pop()
		if current_name==name:
			print(name)
			break
	


find_person("Валера")

		
		


		

	