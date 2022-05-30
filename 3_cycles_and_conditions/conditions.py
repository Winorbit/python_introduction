# УСЛОВИЯ

"""
if превращает все, что справа от него в True либо False.
Если True - едем дальше, если False - операция заканчиваеться.
"""

name = "Rick Decard"
city = "NeoTokyo"

# print(2 == 3)

# if name == "Rick Decard":
# 	print("equal is True")



# else перехватывает операцию, если условие if не проходит.

# if name == "Rick Decard":
# 	print("equal is True")
# else:
# 	print("equal is False")

"""
Условия могут быть многочисленными, соедененными через or или and. 
or - всего одно из условий может сработать.
and - сработать должны условия справа и слева от and.
or/and могут использоваться в связке:
"""
# if name == "Rick Decard" and city == "NonLonDon":
# 	print("Welcome to NonLonDon, Rick!")
# else:
# 	print("Hello Decard!")

# if name == "Rick Decard" or city == "NonLonDon":
# 	print("Welcome to NonLonDon, Rick!")
# else:
# 	print("Hello Decard!")

"""
Условия могут быть вложенными сколько угодно раз.
Скажем, если пользователь - администратор, то идем дальше и там проверяем новое условие.
Если нет - перехватываем и там обрабатываем другими условиями.
"""

# Соответственно, мы можем использовать условия для подбора подохдящих предложений.

# Вот наш юзер, с его уровнем:
user = {"username" : "Egor",
		"id" : 34253234234,
		"level" : 1}

# Вот сообщение от него:
message = {"user": user,
		   "message_text": "not"}

sentences = [{"text": "We're not gonna take it. \n Oh no, we ain't gonna take it \nWe're not gonna take it anymore", 
			  "level": 1},
			  {"text":"I learned very early the difference between knowing the name of something and knowing something.", 
			  "level": 2}]


sentence = sentences[1]

if message.get("user").get("level") >= sentence.get("level"):
	if message.get("message_text") in sentence.get("text"):
		print(sentence)