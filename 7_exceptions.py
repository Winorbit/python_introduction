"""
Если у нас происходит что-то не предусмотренное и программа ломается,
интерпретатор Python останавливает обработку кода, а так же создает специальный объект
Exception, содержащий информацию об ошибке.

Делается это с помощью конструкции try-except.
"""

# try:
#     print(undefiened_value)
# except Exception:
#     # Здесь описано, что делать после появления объекта Exception.
#     print("Exception catched")



# try:
#     print(undefiened_value)
# except Exception as e:
#     # Исключение можно словить, и, как объект, передать дальше и делать с ним все, что нужно.
#     print(f"Exception catched: {e}")



# try:
#     print(undefiened_value)
# except Exception as e:
#     # Можем увидеть, что исключение - объект определенного класса.
#     print(type(e))

"""
Исключение - это такой же класс, как и все другие, и из них,
точно так же, создаются объекты.
Исключений много, под каждый тип ошибок, и они сконструированы с помощью наследования,
от базового класса Exception.

Посмотреть их можно тут:
https://pythonworld.ru/tipy-dannyx-v-python/isklyucheniya-v-python-konstrukciya-try-except-dlya-obrabotki-isklyuchenij.html
"""


# try:
#     print(undefiened_value)
# except NameError as name_error:
#     print(f"Wrong value name catched - {name_error}")

# try:
#     print(undefiened_value)
#     245/0
# except Exception as name_error:
#     print(f"Wrong value name catched - {name_error}")


# try:
#     245/0
# except Exception as name_error:
#     print(f"Wrong value name catched - {name_error}")

# Код прервался


# try:
#     print(undefiened_value)
# except ZeroDivisionError as zero_division_error:
#     print(f"Exception catched - {zero_division_error}")

# try:
#     245/0
# except ZeroDivisionError as zero_division_error:
#     raise NameError(f"Exception catched - {zero_division_error}")


# Можно установить несколько исключений на разные виды ошибок.

try:
    245/0
except NameError as zero_division_error:
    print(ZeroDivisionError)
    print(zero_division_error)
except Exception as name_error:
    print(f"Wrong value name catched - {name_error}")



"""
Можно также установить инструкцию, которая будет выполнена, несмотря на любое исключение.
За это отвечает конструкция try-except-finally.
Например, нам нужно обязательно закрыть файла, что бы не случилось, если он был открыт.
"""


# existing_file = "testfile.txt"
# filename = "unexisted_file.json"
# try:
#     unexisted_file = open(existing_file, "w")
#     res = unexisted_file.read()
# except FileNotFoundError as e:
#     print(f"Error on trying to open file {filename} with exception {e}")
# except Exception as e:
#     print(f"Error on trying to open file {filename} with exception {e}")
# finally:
#     unexisted_file.close()


# with open(existing_file, "w") as f:
#     res = f.read()
#     print(res)


"""
Исключения можно вызывать самостоятельно, с помощью ключевого слова raise. 
Можно их кастомизировать и создавать самому, с помощью наследования.
"""

# 245/0
# raise ZeroDivisionError("Bla-bla-bla")
/users/43434234
def find_user(user_id):
    request_to_db
    id time > 20second:


        raise Exception("Timeout!")
# raise Exception("Exception catched")



"""
Операторы контекста это конструкции, в которые изначально встроено
try-except-finally.
Пример это конструкция with-as
"""



# with open(existing_file, "w") as f:
#     res = f.read()
#     print(res)

