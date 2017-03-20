lst=[
{'school_class': '4a', 'scores': [3,4,4,5,2]},
{'school_class': '4b', 'scores': [3,3,2,5,2]}, 
{'school_class': '4c', 'scores': [5,4,2,4,2]}
]
summary_school_score=0 # общая оценка по школе
summary_school_count=0 # общее количество оценок по школе

for clas in lst: # перебираем классы
	summary_class_score=0 # суммарная оценка по классу
	summary_class_count = 0 # количество оценок в классе
	for score in clas.get("scores"): # перебираем оценки по классу
		summary_class_score+=score # прибавляем очередную оценку к суммарной оценке по классу
	summary_class_count = len(clas.get("scores"))
	print(summary_class_score / summary_class_count) # посчитаем и выведем среднюю оценку по классу
	summary_school_score+=summary_class_score # прибавим суммарную оценку по классу к суммарной оценке по школе
	summary_school_count+=len(clas.get("scores"))# прибавим суммарное количество оценок по классу к суммарному количеству оценок по школе
print(summary_school_score/summary_school_count)



