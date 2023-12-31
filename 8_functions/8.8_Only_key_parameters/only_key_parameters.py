# Только ключевые параметры


"""Если некоторые ключевые параметры должны быть доступны только по ключу, а не как
позиционные аргументы, их можно объявить после параметра со звёздочкой"""

def total(initial=5, *numbers, extra_number):
    count = initial
    for number in numbers:
    count += number
    count += extra_number
    print(count)


total(10, 1, 2, 3, extra_number=50)
total(10, 1, 2, 3)
# Вызовет ошибку, поскольку мы не указали значение
# аргумента по умолчанию для 'extra_number'.

# Вывод:
# $ python keyword_only.py
# 66
# Traceback (most recent call last):
# File "keyword_only.py", line 12, in <module>
# total(10, 1, 2, 3)
# TypeError: total() needs keyword-only argument extra_number

# Как это работает:
# Объявление параметров после параметра со звёздочкой даёт только ключевые
# аргументы. Если для таких аргументов не указано значение по умолчанию, и
# оно не передано при вызове, обращение к функции вызовет ошибку, в чём
# мы только что убедились.
# Обратите внимание на использование +=, который представляет собой сокра-
# щённый оператор, позволяющий вместо x = x + y просто написать x +=
# y.
# Если вам нужны аргументы, передаваемые только по ключу, но не нужен па-
# раметр со звёздочкой, то можно просто указать одну звёздочку без указания
# имени: def total(initial=5, *, extra_number).
