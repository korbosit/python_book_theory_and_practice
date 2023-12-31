# Оператор «return»

"""Оператор return используется для возврата5 из функции, т.е. для прекращения её работы
и выхода из неё. При этом можно также вернуть некоторое значение из функции."""


# def maximum(x, y):
#     if x > y:
#         return x
#     elif x == y:
#         return 'Числа равны.'
#     else:
#         return y


# print(maximum(2, 3))

# Вывод:
# $ python func_return.py
# 3

"""Обратите внимание, что оператор return без указания возвращаемого значения эквива-
лентен выражению return None. None – это специальный тип данных в Python, обознача-
ющий ничего. К примеру, если значение переменной установлено в None, это означает,
что ей не присвоено никакого значения.
Каждая функция содержит в неявной форме оператор return None в конце, если вы
не указали своего собственного оператора return. В этом можно убедиться, запустив
print(someFunction()), где функция someFunction – это какая-нибудь функция, не име-
ющая оператора return в явном виде. Например:"""

# def someFunction():
#     pass

# Оператор pass используется в Python для обозначения пустого блока команд.

# Примечание: Существует встроенная функция max, в которой уже реализован функци-
# онал «поиск максимума», так что пользуйтесь этой встроенной функцией, где это воз-
# можно.
