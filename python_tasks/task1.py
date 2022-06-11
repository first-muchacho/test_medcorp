'''Дана функция f. Что выведет print #1 и print #2?'''


def f(x):
    if getattr(f, "x", None) is None:
        f.x = x
f(6)
f(7)
print(f.x)  # 1 -> 6
setattr(f, "x", 67)
print(f.x)  # 2 -> 67


'''
В данном примере используется встроенная функция 'getattr', которая возвращает значение атрибута объекта.
'getattr' имеет следующую структру: getattr(obj, name, [default]), где:
obj - объект, значение атрибута которого требуется получить;
name - имя атрибута, значение которого требуется получить;
[default] - значение по умолчанию, которое будет возвращено, если объект не располагает указанным атрибутом.
[default], также является необязательным, но в случае отсутствия возникнет AttributeError.
Чтобы добавить объекту атрибут, необходимо использовать встроенную функцию 'setattr'.
'setattr' имеет следующую структру: setattr(obj, name, value), где:
obj -  объект, который следует дополнить атрибутом;
name - строка с имем атрибута;
value - значение атрибута.
------------------------------------------------------------------------------------------------------------
В результате работы функции print#1 распечает 6, т.к. условие истинно.
Потому-что до print не происходит добавления атрибута в getattr(f, "x", None) и getattr является None.
По условию, если getattr является None, то функция в результате работы вернет переданное ей значение,
в данном случае первое переданное значение в функцию равно 6.
------------------------------------------------------------------------------------------------------------
В результате работы функции print#2 распечает 67, т.к. объекту был передан атрибут до print.
'''
