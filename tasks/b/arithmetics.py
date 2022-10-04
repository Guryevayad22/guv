"""
Вам даны три переменные x, y и z, в которые записаны два случайных целых и
одно случайное вещественное число, соответственно.

В этом задании вам запрещено заводить новые переменные и подключать модули.

Выведите по очереди:
- сами три числа через пробел
    > уже написано за вас
- [a] их сумму
- [b] их произведение
- [c] округленное вверх до целого произведение x и z
- [d] частное x и z
- [e] неполное частное при делении x на z
- [f] остаток от деления x на y
- [g] y в степени z
- [h] куб произведения трех их попарных сумм
- [i] число z с ровно пятью знаками после точки
    > подсказка: используйте форматную строку (f-string)

Запишите в переменную FLOATS, сколько среди пунктов [a]-[h] нецелых результатов
в смысле type(результата) == float.
"""
import math

from test.common.context import get_integer, get_float  # не обращайте внимание

x = get_integer()
y = get_integer()
z = get_float()

print(x, y, z)  # вывести три числа через пробел
a = x + y + z
print(a)

b = x * y * z
print(b)

c = x * z
math.ceil(c)
print(c)

d = x / z
print(d)

e = x / z
math.floor(e)
print(e)

p = x / z
f = p - math.floor(p)
print(f)

g = y ** z
print(g)

h = (x * y + x * z + z * y) ** 3
print(h)

i = round(z, 5)
print(i)
"""
# Место для вашего кода
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print(type(f))
print(type(g))
print(type(h))
"""
FLOATS = 8
