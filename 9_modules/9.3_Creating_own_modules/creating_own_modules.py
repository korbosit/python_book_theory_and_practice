# Создание собственных модулей

"""Создать собственный модуль очень легко. Да вы всё время делали это! Ведь каждая про-
грамма на Python также является и модулем. Необходимо лишь убедиться, что у неё уста-
новлено расширение .py. Следующий пример объяснит это"""


# Пример: (сохраните как mymodule.py)

# def sayhi():
#     print('Привет! Это говорит мой модуль.')


# __version__ = '0.1'
# # Конец модуля mymodule.py

"""Выше приведён простой модуль. Как видно, в нём нет ничего особенного по сравнению с
обычной программой на Python. Далее посмотрим, как использовать этот модуль в дру-
гих наших программах.
Помните, что модуль должен находиться либо в том же каталоге, что и программа, в ко-
торую мы импортируем его, либо в одном из каталогов, указанных в sys.path.
Ещё один модуль (сохраните как mymodule_demo.py):"""


# import mymodule

# mymodule.sayhi()
#     print ('Версия', mymodule.__version__)


# Вывод:
# $ python mymodule_demo.py
# Привет! Это

"""Как это работает:
Обратите внимание, что мы используем всё то же обозначение точкой для до-
ступа к элементам модуля. Python повсеместно использует одно и то же обо-
значение точкой, придавая ему таким образом характерный «Python-овый»
вид и не вынуждая нас изучать всё новые и новые способы делать что-либо.
Вот версия, использующая синтаксис from..import (сохраните как mymodule_demo2.py):
from mymodule import sayhi, __version__
sayhi()
print('Версия', __version__)
Вывод mymodule_demo2.py такой же, как и mymodule_demo.py."""


# Обратите внимание, что если в модуле, импортирующем данный модуль, уже было объ-
# явлено имя __version__, возникнет конфликт. Это весьма вероятно, так как объявлять
# версию любого модуля при помощи этого имени – общепринятая практика. Поэтому
# всегда рекомендуется отдавать предпочтение оператору import, хотя это и сделает вашу
# программу немного длиннее.
# Вы могли бы также использовать:
# from mymodule import *
# Это импортирует все публичные имена, такие как sayhi, но не импортирует __version__,
# потому что оно начинается с двойного подчёркивания
