# Создание кортежа
immutable_var = 1, 2, 3, 4, ("command", "step")
print(immutable_var)
print(type(immutable_var))

# Изменение кортежа
immutable_var [2] = 52
print(immutable_var)    # >>> immutable_var [2] = 52 Traceback (most recent call last):  File "<stdin>", line 1, in <module> TypeError: 'tuple' object does not support item assignment >>> print(immutable_var)  (1, 2, 3, 4, 'command', '4barzzz')
# Кортеж не получится изменить, т.к. это встроенный тип данных, который используется для хранения нескольких элементов в одной переменной.

# Изменение списка
mutable_list = [1, 2, 3, 4, ("command", "step")]
mutable_list [2] = 52
mutable_list [4] = "stay"
print(mutable_list)