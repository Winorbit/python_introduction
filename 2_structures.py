{"name": "Oleg"}	#dict (словарь)
(1,2)				#tuple (кортеж)
[1,2]				#list (список)
{1,2}				#set
frozenset({1,2})	#frozenset


################## СЛОВАРЬ ###########################

""" 
- Обозначается как {}
- Изменяемый
- Хранит данные по принципу ключ-значение.
- Содержит любые типы данных
- Подробнее про словари - https://pythonworld.ru/tipy-dannyx-v-python/slovari-dict-funkcii-i-metody-slovarej.html
"""

# Значением  может быть все, что угодно.
# Ключом - только неизменемый тип данных.
test_dict = {1: 2, "name": "Oleg", False: True, 22.0: None}


# Пример реального словаря:
weather_info = {"username": "Egor",
 				"location": "Kyiv",
 				"weather": "mist",
 				"coords": {"lat": 98.06, 
 							"lon": 123.01}
 				}


# ПОЛУЧИТЬ значение из словаря можно по ключу.
name = my_dict["name"]
# Если значение это структура, например, словарь, то также обращаемся по ключу, глубина не важна.
lattitude = weather_info["coords"]["lat"] 

# Но если такого ключа нет, ты получим ошибку.
unexisted_value = my_dict["value"]

# Более безопасный способ. Если ключа нет, мы получим None.
unexisted_value = my_dict.get("value")
lattitude = my_dict.get("coords").get("lat")


# ИЗМЕНИТЬ ЗНАЧЕНИЕ.
weather_info["username"] = "Newname"

# ДОБАВИТЬ ПАРУ КЛЮЧ-ЗНАЧЕНИЕ.
weather_info["new_field"] = 42

# УДАЛИТЬ ПАРУ КЛЮЧ-ЗНАЧЕНИЕ.
del weather_info["new_field"]


# Немного практики.
user = {"username": "Egor",
		"city": "Kyiv",
		"birthdate":"01.05.1994",
		"phones":{"sim1":{"operator":"MTC","phone_number": "+232322322333333"}
          		  "sim2":{"operator":"A1", "phone_number": "+12121212122"}
		}}

print(user["phones"])
print(user["phones"]["sim1"])
print(user["phones"]["sim1"]["operator"])

#Сменим оператора у сим-карты 1
user["phones"]["sim1"]["operator"] = "New operator"

#удалим номер с симки 2
del user["phones"]["sim1"]["phone_number"]


####################### СПИСКИ ###########################
""" 
- Обозначается как []
- Изменяемый
- Хранит данные по принципу последовательности, одно за одним.
- Может хранить любые значения, в том числе  другие структуры любой степени вложенности.
- Подробно про списки - https://pythonworld.ru/tipy-dannyx-v-python/spiski-list-funkcii-i-metody-spiskov.html
"""


[1, 2.0, True, None, "Some string", {"key": "value"}, [{"a":"b"}, {"c": 25}]]


# Пример - храним песни для музыкального приложения. Информация о песне - словарь, все песни - в списке.

[
{"artist":"Disturbed", "name": "The light" ,"long": 4.16, "band": True, "album":"Immortalized"}
{"artist":"Guns N' Roses", "name": "Civil War", "long": 7.42, "band":True, "album": "Use Your Illusion II"}
{"artist":"Ben Nichols", "name": "The last pale light in the west", "long": 3.24, "band":False, "album": None}
]

# Чтобы легче обращаться к списку, присвоим его значение переменной:

songs = [
		{"artist":"Disturbed", "name": "The light" ,"long": 4.16, "band": True, "album":"Immortalized"}
		{"artist":"Guns N' Roses", "name": "Civil War", "long": 7.42, "band":True, "album": "Use Your Illusion II"}
		{"artist":"Ben Nichols", "name": "The last pale light in the west", "long": 3.24, "band":False, "album": None}
		]


# Разумеется, можно присвоить значения отдельных песен переменным, и положить их в список:

song_one = {"artist":"Disturbed", "name": "The light" ,"long": 4.16, "band": True, "album":"Immortalized"}
song_two = {"artist":"Guns N' Roses", "name": "Civil War", "long": 7.42, "band":True, "album": "Use Your Illusion II"}
song_three = {"artist":"Ben Nichols", "name": "The last pale light in the west", "long": 3.24, "band":False, "album": None}
song_four = {"artist":"Linkin Park", "name": "Leave out all the rest", "long": 3.19, "band":True, "album": "Minutes to Midnight"}
song_five = {"artist":"", "name": "i'm still here", "long": 3.26, "band":False, "album": "Treasure Planet OST"}

songs = [song_one, song_two, song_three, song_four, song_five]

"""
Как извлечь отдельный элемент? 
По ИНДЕКСУ. 
Индекс - порядковый номер элмента в списке, но начинаеться отсчет с 0
"""
songs[0]
songs[1]
songs[4]

# Можно использовать отрицательные индексы, тогда счет пойдет с конца. -1 это последний элемент
songs[-1]

# Можно извлекать не только отдельные элементы, но и подсписки - срезы.
# Более подробно о срезых по ссылке - https://pythonworld.ru/osnovy/indeksy-i-srezy.html
songs[2:4]

# Как изменить значение элемента?
songs[0] = 1

#Как добавить новый элемент в конец
songs.append(1)
songs.append("New element")

# Как вставить элемент на определнную позицию

# insert(номер позиции, значение)
songs.insert(2, "New element")

# Если номер позиции больше длинны списка, элемент добавиться в конец
songs.insert(2222, "New element")

# Как удалить элемент по значению:
songs.remove(1)

# Как удалить элемент по индексу(номеру позиции в списке):
del songs[1]


# Два списка можно объеденить:
another_songs = [{"artist":"Порнофильмы", "name": "Мы вам не верим", "band": True}
				 {"artist":"ДДТ", "name": "Не стреляй!", "band":True}]
print(songs + another_songs)



####################### ТУПЛИ (КОРТЕЖИ) ###########################

""" 
- Обозначается как (), либо без скобок, перечисляя элементы через запятую.
- Неизменяемый.
- Ровно то же самое, что и список, только без возможности добавлять, удалять и изменять элементы.

"""
test_tuple = (1, 2.0, True, None, "Some string", {"key": "value"}, [{"a":"b"}, {"c": 25}])
#Точно так же можно объявить и без круглых скобок, просто перечисляя элементы. 
test_tuple = 1, 2.0, True, None, "Some string", {"key": "value"}, [{"a":"b"}, {"c": 25}]

#Извлечение элементов и срезов работает так же, как у списка.



####################### SET ###########################
""" 
- Обозначается как {}, но, в отличие от списка, внутри не пары ключ-значение, а перечисление элементов через запятую.
- Изменяемый
- Может содержать только неизменяемые, не повторяющиеся элементы.
- Подробнее про sets/frozensets - https://pythonworld.ru/tipy-dannyx-v-python/mnozhestva-set-i-frozenset.html

"""
test_set = {1, 2.0, True, None, "Some string"}

# Если в сете добавлены повторяющиеся элементы, они просто не будут учитываться.
test_set = {1,1,1, "Hello"} # в результате будет {1, "Hello"}.

# Не предназнчен для извлечения отдельных элементов по индексу или ключу.

# Как добавить новый элемент в конец:
test_set.add("New element")

# Как удалить элемент по значению:
test_set.remove("New element")


####################### FROZENSET ###########################
""" 
- Обозначается как frozenset().
- Неизменяемый.
- Ровно то же самое, что и SET, только без возможности добавлять, удалять и изменять элементы.
- То есть, это такой тупль, только еще и элементы не повторяються
"""

test_frozenset = frozenset({1, 2.0, True, None, "Some string"})


# Структуры, как и примитивные типы данных, можно трансформировать друг в друга

tuple([1,2])
set([1,2])
frozenset(tuple(["Hello", False]))
list(frozenset((None, True, "Name")))

# СТРОКИ это тоже последовательности, как список, поэтому из строки так же можно извлекать срезы и элементы по индексу.
test_string = "Some lorem ipsum string"
test_string[8]
test_string[8:13]


# У каждой последоватлеьности есть длинна. Ее можно узнать функцией len()
len(test_string)
len(test_frozenset)
len(test_tuple)
len(songs)
