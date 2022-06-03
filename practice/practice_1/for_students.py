########################### Задача ###########################
'''
Написать скрипт, который, основываясь на вводных, выведет на печать предложения, содержащие текст из message.

input -> wand

result -> "The Consul watched as Kassad raised the death wand."

input -> the

result ->  """The sky the port was the color of television, tuned to a dead channel.
		   The man in black fled across the desert, and the gunslinger followed."""


Т.е result это одна строка, содержащая в себе предложение, в которое входит слово, заданное юзером (поле text в словаре message)

P.S:
Вносить изменения в исходную структуру можно. Например, если хотите создать словарь для описания уровней типа
eng_levels = {"beginner": 0,
 			  "pre-intermediate": 1,
 			  "intermediate": 2}
'''

########################### Вводные данные ###########################

user = {"username" : "Egor",
		"level" : 1} 

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

# Ваш код здесь:

...

# В результате выполнения вот этой команды:
print(result_message)
# В терминале должно вывестись вот это:
"""
"We're not gonna take it. \n Oh no, we ain't gonna take it \nWe're not gonna take it anymore"
"""


"""
Варианты улучшения кода:

- Предусмотрите 3 варианта развития событий
	- одно совпадение
	- несколько совпадений
	- ни одного совпадения

- Сделайте так ,чтоб в случае нескольких совпадений предложения внутри результирующей строки как-то визуально разбивались.
  Например серез три точки:

  The sky the port was the color of television, tuned to a dead channel.
  ...
  The Consul watched as Kassad raised the death wand.
  ...

- Напишите варианты кода в случаях, когда level это цифра и когда это строка. Т.е 1 или "beginner"
"""