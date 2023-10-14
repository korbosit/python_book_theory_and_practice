# Функция dir


"""Вы можете использовать встроенную функцию dir, чтобы получить список идентифика-
торов, которые объект определяет. Так в число идентификаторов модуля входят функции,
классы и переменные, определённые в этом модуле.
Когда вы передаёте функции dir() имя модуля, она возвращает список имён, опреде-
лённых в этом модуле. Если никакого аргумента не передавать, она вернёт список имён,
определённых в текущем модуле.
Пример:
"""

# $ python3
# >>> import sys # получим список атрибутов модуля 'sys'
# >>> dir(sys)
# ['__displayhook__', '__doc__', '__excepthook__', '__name__', '__package__', '__s
# tderr__', '__stdin__', '__stdout__', '_clear_type_cache', '_compact_freelists',
# '_current_frames', '_getframe', 'api_version', 'argv', 'builtin_module_names', '
# byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dllhandle'
# , 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable',
# 'exit', 'flags', 'float_info', 'getcheckinterval', 'getdefaultencoding', 'getfil
# esystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof',
# 'gettrace', 'getwindowsversion', 'hexversion', 'intern', 'maxsize', 'maxunicode
# ', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platfor
# m', 'prefix', 'ps1', 'ps2', 'setcheckinterval', 'setprofile', 'setrecursionlimit
# ', 'settrace', 'stderr', 'stdin', 'stdout', 'subversion', 'version', 'version_info', 'warnoptions', 'winver']


# >>> dir() # получим список атрибутов текущего модуля
# ['__builtins__', '__doc__', '__name__', '__package__', 'sys']
# >>> a = 5 # создадим новую переменную 'a'
# >>> dir()
# ['__builtins__', '__doc__', '__name__', '__package__', 'a', 'sys']
# >>> del a # удалим имя 'a'
# >>> dir()
# ['__builtins__', '__doc__', '__name__', '__package__', 'sys']
# >>>


"""Как это работает:
Сперва мы видим результат применения dir к импортированному модулю
sys. Видим огромный список атрибутов, содержащихся в нём.
Затем мы вызываем функцию dir, не передавая ей параметров. По умолча-
нию, она возвращает список атрибутов текущего модуля. Обратите внимание,
что список импортированных модулей также входит туда.
Чтобы пронаблюдать за действием dir, мы определяем новую переменную
a и присваиваем ей значение, а затем снова вызываем dir. Видим, что в
полученном списке появилось дополнительное значение. Удалим перемен-
ную/атрибут из текущего модуля при помощи оператора del, и изменения
вновь отобразятся на выводе функции dir.
Замечание по поводу del: этот оператор используется для удаления перемен-
ной/имени, и после его выполнения, в данном случае – del a, к переменной
a больше невозможно обратиться – её как будто никогда и не было.
Обратите внимание, что функция dir() работает для любого объекта. Напри-
мер, выполните “dir('print')”, чтобы увидеть атрибуты функции print, или
“dir(str)”, чтобы увидеть атрибуты класса str."""


