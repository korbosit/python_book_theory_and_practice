#

"""Чтобы импортировать переменную argv прямо в программу и не писать всякий раз sys.
при обращении к ней, можно воспользоваться выражением “from sys import argv”.
Для импорта всех имён, использующихся в модуле sys, можно выполнить команду “from
sys import *”. Это работает для любых модулей.
В общем случае вам следует избегать использования этого оператора и использовать
вместо этого оператор import, чтобы предотвратить конфликты имён и не затруднять
чтение программы."""

# Пример:
from math import *

n = input("Введите диапазон:- ")
p = [2, 3]
count = 2
a = 5
while (count < n):
    b=0
    for i in range(2,a):
        if ( i <= sqrt(a)):
            if (a % i == 0):
                print("a neprost",a)
                b = 1
            else:
                pass
    if (b != 1):
        print("a prost",a)
        p = p + [a]
        count = count + 1
        a = a + 2
print p
