########################### Задача ###########################
"""
Нужно попрактиковаться с базовыми вещами - циклы, условия, структуры. 
Для этого напишем код, эмулирующий часть работы будущего бота.
 - юзер присылает слово на английском, 
 - в ответ на печать выводятся те предложения, в которых это слово есть и которые соответствую уровню юзера
"""

########################### Вводные данные ###########################

user = {"username" : "Egor",
		"level" : 1} 
		# Другой вариант левела? Например, попробвать текстовые - pre-intermediate, intermediate? 
		# Это можно попробовать, если быстро справятся

message = {"user": user,
		   "text": "take"}


sentences = [
	{"text": "When my time comes \n Forget the wrong that I’ve done.", 
	"level": 1},
	{"text": "In a hole in the ground there lived a hobbit.", 
	"level": 2},
	{"text": "The sky the port was the color of television, tuned to a dead channel.", 
	"level": 1},
	{"text": "I love the smell of napalm in the morning.", 
	"level": 0},
	{"text": "The man in black fled across the desert, and the gunslinger followed.", 
	"level": 0},
	{"text": "The Consul watched as Kassad raised the death wand.", 
	"level": 1},
	{"text": "If you want to make enemies, try to change something.", 
	"level": 2},
	{"text": "We're not gonna take it. \n Oh no, we ain't gonna take it \nWe're not gonna take it anymore", 
	"level": 1},
	{"text":"I learned very early the difference between knowing the name of something and knowing something.", 
	"level": 2}
]
############################ Задача
'''
Написать скрипт, который, основываясь на вводных, выведет на печать предложения, содержащие текст из message.

input -> wand

result -> "The Consul watched as Kassad raised the death wand."

input -> the

result ->  """The sky the port was the color of television, tuned to a dead channel.
		   The man in black fled across the desert, and the gunslinger followed."""


input - просто значение по ключу text из словаря message, т.е без использования input из терминала. 
Тут важно просто научиться работать с данными.

важный момент - расскзать про hapy/unhapy path, предусмотреть три варианта:
- когда ни одного предложения по запросу не найдено
- когда найдено одно
- когда найдено несколько
'''


############################ Примерно такой код должен быть в результате
user = {"username" : "Egor",
		"level" : 1} 
		# Другой вариант левела? Например, попробвать текстовые - pre-intermediate, intermediate? 
		# Это можно попробовать, если быстро справятся

message = {"user": user,
		   "text": "the"}


sentences = [
	{"text": "When my time comes \n Forget the wrong that I’ve done.", 
	"level": 1},
	{"text": "In a hole in the ground there lived a hobbit.", 
	"level": 2},
	{"text": "The sky the port was the color of television, tuned to a dead channel.", 
	"level": 1},
	{"text": "I love the smell of napalm in the morning.", 
	"level": 0},
	{"text": "The man in black fled across the desert, and the gunslinger followed.", 
	"level": 0},
	{"text": "The Consul watched as Kassad raised the death wand.", 
	"level": 1},
	{"text": "If you want to make enemies, try to change something.", 
	"level": 2},
	{"text": "We're not gonna take it. \n Oh no, we ain't gonna take it \nWe're not gonna take it anymore", 
	"level": 1},
	{"text":"I learned very early the difference between knowing the name of something and knowing something.", 
	"level": 2}
]

matched_sentences = []
result_message = ""
no_matches_message = "Sorry, not sentences for you"
user = message.get("user")

# собираем тексты из messages в один результирующий список
for sentence in sentences:
	if user.get("level") == sentence.get("level"):
		if message.get("text") in sentence.get("text"):
			matched_sentences.append(sentence.get("text"))



# Затем, на основе этого списка, создаем рзультирующее сообщение
if not matched_sentences: # тут, конечно, криво, но я хочу чтоб они попробовали и обращение по индексу и применили просто if,с неявным сравнением
	result_message = no_matches_message
if len(matched_sentences) == 1:
	result_message = matched_sentences[0]
if len(matched_sentences) > 1:
	for text in matched_sentences:
		result_message+= f"\n{text}\n..."

print(result_message)