# УСЛОВИЯ

"""
if превращает все, что справа от него в True либо False.
Если True - едем дальше, если False - операция заканчиваеться.
"""

name = "Rick Decard"
city = "NeoTokyo"

print(2 == 2)

if name == "Rick Decard":
	print("equal is True")



# else перехватывает операцию, если условие if не проходит.

if name == "Rick Decard":
	print("equal is True")
else:
	print("equal is False")

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

user = {"name": "Alex",
		"age": 44,
		"is_admin": False}

admin = {"name": "FF.t",
		"age": 25,
		"is_admin": True}


# if type(user) == dict:
#     # пустой словарь - {} в условиях превращаеться в False а имеющий хоть какой-то значение - True.
#     # поэтому вместо if user == True можно поставить просто if user.
#     if user:
#         if user.get("is_admin"):
#             print("Multiple checking is done!")
#     if not user:
#         if user.get("is_admin"):
#             print("Multiple checking is done!")


# if type(admin) == dict:
# 	if admin:
# 		if admin.get("is_admin"):
# 			print("Multiple checking is done!")
# 	if not admin:
# 		if admin.get("is_admin"):
# 			print("Multiple checking is done!")

