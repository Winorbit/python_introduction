"""
Опишем с помощью классов такую сущность, как пост в блоге.
Зададим атрибуты, которые будут содержать данные нашего поста и
зададим два метода - функции, привязанные к конкретному классу.

add_text - позволяет изменить значение атрибута text
add_title - позволяет изменить значение атрибута text

Т.к изначально значения text и title пусты, мы будем менять его с помощью методов.
"""

from datetime import datetime
now = datetime.now()


class BlogPost:
	title = ""
	text = ""
	author = ""
	date = now.strftime("%d/%m/%Y %H:%M:%S")
	
	def add_text(self, text):
		"""
		self - обязательный аргумент, который являеться ссылкой объекта на самого себя.
		т.е self.text, получается - это переменная, привязанная не к классу а к объекту
		порожденному из этого класса.
		Сделав 10 объектов Lesson у этих 10 объектов будет 10 значений text равных "",
		но это будут 10 разных пустых строк. И self указывает, какой именно это text
		"""
		self.text = text

	def add_title(self, title):
		self.title = title



# Из класса BlogPost создаем объект BlogPost()
post_about_pandas = BlogPost()

# BlogPost()
# BlogPost().add_text("Любой текст поста про панд")
# BlogPost()


# print(post_about_pandas.title)
# print(post_about_pandas.text)
# print(post_about_pandas.date)


# Меняем значения его атрибутов с помощью его же методов.
# post_about_pandas.add_text("Любой текст поста про панд")
# post_about_pandas.add_title("Просто заголовок")


# print(post_about_pandas.title)
# print(post_about_pandas.text)
# print(post_about_pandas.date)


# post_about_cowboy_beebop = BlogPost()
# post_about_cowboy_beebop.add_text("один из множеста текстов про то, какое выдающееся аниме 'Ковбой Бибоп'")
# post_about_cowboy_beebop.add_title("Real Folk Blues")

# print(post_about_cowboy_beebop.title)
# print(post_about_cowboy_beebop.text)
# print(post_about_cowboy_beebop.date)


# Теперь создадим новый класс Lesson, из которого можно создавать объекты Уроков.
class Lesson:
	title = ""
	text = ""
	date = now.strftime("%d/%m/%Y %H:%M:%S")
	usefull_links = []
	
	def add_text(self, text):
		self.text = text

	def add_title(self, title):
		self.title = title

	def add_usefull_links(self, link):
		self.usefull_links.append(link)

# Lesson().add_usefull_links("Hello")
# Lesson().add_usefull_links("Bye")
# classes_inheritance = Lesson()
# classes_inheritance.add_title("ООП в Python. Наследование")
# classes_inheritance.add_text("Урок о наследовании в ООП и Python в частности")

# print(classes_inheritance.title)
# print(classes_inheritance.text)
# print(classes_inheritance.date)


# НАСЛЕДОВАНИЕ
class BaseTextModel:
	title = "test"
	text = "test"
	date = now.strftime("%d/%m/%Y %H:%M:%S")

	def add_text(self, text):
		self.text = text

	def add_title(self, title):
		self.title = title

"""
Хоть BlogPost и пустой, но т.к он отнаследован от BaseTextModel,
он обладает всеми атрибутами и методами ,что есть у BaseTextModel.
"""
class BlogPost(BaseTextModel):
	pass

# test_empty_post = BlogPost()
# print(test_empty_post.title)
# print(test_empty_post.text)
# print(test_empty_post.date)



# post_about_cowboy_beebop = BlogPost()
# post_about_cowboy_beebop.add_text("один из множеста текстов про то, какое выдающееся аниме 'Ковбой Бибоп'")
# post_about_cowboy_beebop.add_title("Real Folk Blues")

# print(post_about_cowboy_beebop.title)
# print(post_about_cowboy_beebop.text)
# print(post_about_cowboy_beebop.date)


"""
Когда у класса-наследника объявлены методы и атрибуты
Они прибавляются к методам и атрибутам родителя. 
"""
class BlogPost(BaseTextModel):
	author = ""

	def add_author(self,author_username):
		self.author = author_username

	def post_as_dict(self):
		post = {}
		post["date"] = self.date
		post["title"] = self.title
		post["text"] = self.text
		post["author"] = self.author
		return post

# post_about_cowboy_beebop = BlogPost()
# post_about_cowboy_beebop.add_text("один из множеста текстов про то, какое выдающееся аниме 'Ковбой Бибоп'")
# post_about_cowboy_beebop.add_title("Real Folk Blues")

# post_as_dict = post_about_cowboy_beebop.post_as_dict()
# print(post_as_dict)



class Lesson(BaseTextModel):
	def lesson_as_dict(self):
		lesson = {}
		lesson["date"] = self.date
		lesson["title"] = self.title
		lesson["text"] = self.text
		return lesson

# classes_inheritance = Lesson()
# classes_inheritance.add_title("ООП в Python. Наследование")
# classes_inheritance.add_text("Урок о наследовании в ООП и Python в частности")

# lesson_as_dict = classes_inheritance.lesson_as_dict()
# print(lesson_as_dict)

"""
Наследование может иметь сколь угодно длинную цепочку.
Lesson унаследован от BaseTextModel и имеет все его методы и атрибуты
А SpecialLesson, унаследованный от Lesson имеет все методы и атрибуты 
и от BaseTextModel и от Lesson.
"""


class SpecialLesson(Lesson):
	def add_interpreteor_block_in_code(self):
		pass

# epic_lesson = SpecialLesson()
# epic_lesson.add_title("ООП в Python. Наследование")
# epic_lesson.add_text("Урок о наследовании в ООП и Python в частности")

# epic_lesson_as_dict = epic_lesson.lesson_as_dict()
# print(epic_lesson_as_dict)

"""
Множесственное наследование.

Зададим два класса для двух разных объектов видеоигры.
NPC - неигровой персонаж, массовка.
Character - игровой персонаж.
"""
class NPC:
	base_hp = 100

	def decrease_hp():
		pass

	def increase_hp():
		pass


class Character(NPC):
	aggression = False

	def __init__(self, name):
		self.name = name

	def start_dialog(self):
		pass

ivan = Character("Ivan Drago")
rocky = Character("Rocky Balboa")

print(ivan.name, rocky.name)


# dealer = Character("Sidorovich")
# print(dealer.name)

"""
Простое наследование. 
Mob - противник, наследуется от класса неигрового персонажа,
но еще имеет метод attack, позволяющий нападать.
"""
class Mob(NPC):
	aggression:bool = True

	def __init__(self, armor_type, weapon_type):
		self.armor = armor_type
		self.weapon = weapon_type

	def attack(self):
		pass


"""
А здесь зададим класс опционального босса.
Это неигровой персонаж, которого можно атаковать, и тогда он 
начнет с нами сражаться. 
Для этого дадим ему возможности как NPC так и моба.
"""

class OptionalBoss(Mob, Character):
	pass

"""
У __init__() для класса Mob всго 2 аргумента, и списке аргументов он первый,
а значит именно этот __init__() будет использован, по правилам множественного наследования.
Поэтому здесь мы получим ошибку из-за неверного колличества аргументов.
"""
# some_boss = OptionalBoss("N7 Armor", "Dragon Slayer Sword","Boss")
# print(some_boss.agrresive)



class OptionalBoss(Character, Mob):
	def __init__(self, name, armor_type, weapon_type):
		self.name = weapon_type
		self.armor = armor_type
		self.weapon = weapon_type

	def do_agro(self):
		self.aggression = True

# А вот так, поменяв родителей местами, все выйдет:
# boss = OptionalBoss("N7 Armor", "Dragon Slayer Sword","Boss")
# print(boss.aggression)


class OptionalBoss(Character, Mob):
	pass

